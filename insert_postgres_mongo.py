import pymongo
import json
from dao.Suicidio import Suicidio  # Importação da Classe Suicidio

client = pymongo.MongoClient("localhost", 27017) # 172.0.0.1

db = client.suicidio_world # Nome do Banco e da Coleção

suicidio = Suicidio() # Instanciamento do objeto
#suicidio.medida_dispersao_suicido('female')
array_medida_dispersao =  suicidio.node_suicidio('all')
#print(type(str(array_medida_dispersao)))
print(type(array_medida_dispersao))
for data in array_medida_dispersao:
    db.suicidios.insert_one(data)
    #db.suicidios.insert_many(data)
    nome = data["id"]
    print(nome)
    
    
