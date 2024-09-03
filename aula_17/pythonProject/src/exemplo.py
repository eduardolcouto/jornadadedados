from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from faker import Faker


faker = Faker()
engine = create_engine('sqlite:///banco.db', echo=True)

print("Conexão com o banco de dados realizada com sucesso!")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)

    def __repr__(self):
        return f"Usuário: {self.nome}"

Base.metadata.create_all(engine)

print("Tabela criada com sucesso!")

usuario = Usuario(nome=faker.name(), idade=faker.random_int(18, 56), email=faker.email())
# print(usuario)
Session = sessionmaker(bind=engine)
with Session() as session:
    session.add(usuario)
    session.commit()

    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"[{usuario.id}] Usuários: {usuario.nome}, Idade: {usuario.idade}, email: {usuario.email}")

    print("Usuário inserido com sucesso!")


