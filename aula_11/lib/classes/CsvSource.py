import os.path

from lib.classes.FilesSources import FilesSources


class CsvSource(FilesSources):

    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data','csv_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        currents_files = os.listdir(self.folder_path)
        new_files = [file for file in currents_files if file not in self.previous_files and file.endswith('.csv')]

        if new_files:
            print("No arquivo encontrado: ", new_files)
            self.previous_files = currents_files
        else:
            print("Nenhum arquivo novo")
            self.get_data()


    def transform_data_to_df(self):
        pass

    def get_data(self):
        print("get_data")


''