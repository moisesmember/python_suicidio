import json
import requests

url = 'http://127.0.0.1:3040/suicidio/brazil/'

"""
url = 'http://127.0.0.1:3040/suicidio/brazil/dispersao'
# payload = {'some': 'data'}
payload = {}
headers = {'content-type': 'application/json'}

r = requests.get(url, data=json.dumps(payload), stream=True)
data_dispersao = r.json()
#print(r.json())
#print(data_dispersao[0]['num_registro']

print(len(data_dispersao))
lenght = len(data_dispersao)

#for i in range(lenght): print(data_dispersao[i])  
for i in range(lenght): 
    #print(data_dispersao[i]['genero'])
    if str(data_dispersao[i]['genero']) == "male" :
        print(data_dispersao[i])  

"""


def medida_dispersao_suicido(self, rota):
    url = self.url+str(rota)
    # payload = {'some': 'data'}
    payload = {}
    headers = {'content-type': 'application/json'}

    r = requests.get(url, data=json.dumps(payload), stream=True)
    data_dispersao = r.json()
    #print(r.json())
    #print(data_dispersao[0]['num_registro']

    print(len(data_dispersao))
    lenght = len(data_dispersao)

    #for i in range(lenght): print(data_dispersao[i])  
    for i in range(lenght): 
        #print(data_dispersao[i]['genero'])
        if str(data_dispersao[i]['genero']) == "male" :
            print(data_dispersao[i])  

