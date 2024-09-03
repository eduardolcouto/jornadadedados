from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, Session, foreign, relationship
from faker import Faker

faker = Faker('pt_BR')

engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cnpj = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"Fornecedor: {self.nome}"

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    preco = Column(Integer)
    descricao = Column(String)

    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship("Fornecedor")

    def __repr__(self):
        return f"Produto: {self.nome}"


def popular_banco(quantidade_de_registros = 10):
    engine = create_engine('sqlite:///banco.db', echo=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    fornecedores = []
    produtos = []
    with Session() as session:
        for _ in range(quantidade_de_registros):
            fornecedor = Fornecedor(nome=faker.company(), email=faker.email())
            fornecedores.append(fornecedor)

            for _ in range(faker.random_int(2,5)):
                produto = Produto(nome=faker.word(), preco=faker.random_int(10, 100), descricao=faker.text(), fornecedor=fornecedor)
                produtos.append(produto)

        session.add_all(fornecedores)
        session.add_all(produtos)
        session.commit()

        print("Fornecedor e Produto inseridos com")

def consulta_produtos_all():
    engine = create_engine('sqlite:///banco.db', echo=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        produtos = session.query(Produto).all()
        for produto in produtos:
            print(f"[{produto.id}] Produto: {produto.nome}, Preço: {produto.preco}, Descrição: {produto.descricao}, Fornecedor: {produto.fornecedor.nome}")

def consulta_produtos_sumarizado():
    engine = create_engine('sqlite:///banco.db', echo=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with (Session() as session):
        produtos = session.query(
            Fornecedor.nome,
            func.sum(Produto.preco).label('total'),
            func.count(Produto.id).label('qtd_produto')
        ).join(Produto, Fornecedor.id == Produto.fornecedor_id).group_by(Fornecedor.nome).order_by(Fornecedor.nome).all()

        # print(produtos)
        for produto in produtos:
            print(f"Fornecedor: {produto.nome}, Total: {produto.total}, Qtd Produtos: {produto.qtd_produto}")


if __name__ == '__main__':
    popular_banco(1000000)
    # consulta_produtos_sumarizado()