import pymongo
import json

class SuicidioMongoDao:

    def connection(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["suicidio_world"] # Banco de Dados
        mycol = mydb["suicidios"]       # Collection
        return mycol

    # Lista todos oos Documentos só do Brazil
    def listAllBrazil(self):
        db_suicidio = SuicidioMongoDao() # Instância Objeto da Classe
        connected = db_suicidio.connection() # Realiza a conexão com o MongoDB
        return connected.find({"country":"Brazil"}) # Retorna valor
    
    # Lista todos os Documentos conforme o Parâmetro
    def listAllFilter(self, parametro):
        db_suicidio = SuicidioMongoDao() # Instância Objeto da Classe
        connected = db_suicidio.connection() # Realiza a conexão com o MongoDB
        return connected.find(parametro) # Retorna valor - Parâmetro deve ser um Dicionário

    def searchSuicidio(self, codigo):
        db_suicidio = SuicidioMongoDao() # Instância Objeto da Classe
        connected = db_suicidio.connection() # Realiza a conexão com o MongoDB
        return connected.find_one({"id":codigo}) # Retorna valor - Parâmetro deve ser um Dicionário

db_suicidio = SuicidioMongoDao()
#array_suicidio = db_suicidio.listAllBrazil()
#parametro = {{"country":"Brazil"},{"sex":"male"}}
"""
array_suicidio = db_suicidio.listAllFilter(dict({"sex":"male"}))
for register in array_suicidio:
    print(register)
"""
array_suicidio = db_suicidio.searchSuicidio("201")
print(array_suicidio)

