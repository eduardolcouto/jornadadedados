from ..lib.classes.FilesSources import AbstractDataSource

class CsvSource(AbstractDataSource):
    def __init__(self):
        super().__init__()
        self.previous_files = []
        self.start()
    
    def save_data(self):
        pass

    def transform_data_to_df(self):
        pass

    def get_data(self):
        pass

    def start(self):
        pass

