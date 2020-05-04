import json
import requests

class Heart:
    url = 'http://127.0.0.1:3040/heart/'
    
    # Método que salva os dados do Heart
    def salvarHeart(self, paramentros):
        url = self.url+"salvar/"
        # payload = {'some': 'data'}
        payload = {}
        headers = {'content-type': 'application/json'}

        r = requests.post(url, data=json.dumps(paramentros), stream=True)
        save = r.json()
        return save
        #print(r.json())
        #print(data_dispersao[0]['num_registro']
