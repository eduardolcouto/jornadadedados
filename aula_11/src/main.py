from time import sleep

from lib.classes.CsvSource import CsvSource
import schedule
# Função para verificar novos arquivos
def check_for_new_files():
    csv_source.check_for_new_files()

csv_source = CsvSource()

schedule.every(10).seconds.do(check_for_new_files)
while True:
    schedule.run_pending()
    sleep(1)