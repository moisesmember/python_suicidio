import csv
import psycopg2

class ExportData:
    # Método responsável por extrair os dados e fazer a leitura
    def extraction_csv_heart(self):
        arquivo = open('../csv/heart.csv')
        linhas = csv.reader(arquivo)
        return linhas     
        """   
        for linha in linhas:
            print(linha)
        """
    





"""
cdv = ExportData()
#cdv.extraction_csv_heart()
for linha in cdv.extraction_csv_heart():
    print(linha)
"""

