import json
import requests

class Suicidio:
    url = 'http://127.0.0.1:3040/suicidio/brazil/'
    
    def medida_dispersao_suicido(self, genero):
        url = self.url+"suicidio_medida_dispersao"
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
            if str(data_dispersao[i]['genero']) == str(genero) :
                print(data_dispersao[i])  


    """
        Node responsável pela extração dos dados
        no node
    """
    def node_suicidio(self, rota):
        url = self.url+str(rota)
        # payload = {'some': 'data'}
        payload = {}
        headers = {'content-type': 'application/json'}

        r = requests.get(url, data=json.dumps(payload), stream=True)
        data_dispersao = r.json()
        #print(r.json())
        #print(data_dispersao[0]['num_registro']
        #print(len(data_dispersao))
        #lenght = len(data_dispersao)
        return data_dispersao










"""
suicidio = Suicidio();
suicidio.medida_dispersao_suicido('female')
suicidio.node_suicidio('all')
"""