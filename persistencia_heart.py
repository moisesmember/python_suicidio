import csv
from dao.Heart import Heart  # Importação da Classe Heart
#from source_data.ExportData import ExportData # Importação da Classe de Extração do CSV

arquivo = open('csv/heart.csv')
linhas = csv.reader(arquivo)
#print(list(linhas)) 
print(dict(linhas))  

heart_dict = {
                "age":1, 
                "sex":12, 
                "chest_pain_type":2, 
                "trestbps":2, 
                "chol":2, 
                "fbs":2, 
                "restecg":2, 
                "thalach", 
                "exang", 
                "oldpeak", 
                "slope", 
                "ca", 
                "thal", 
                "target"
                }
"""
for linha in linhas:
    print(linha)
    
    heart_dict = {
                    "age", 
                    "sex", 
                    "chest_pain_type", 
                    "trestbps", 
                    "chol", 
                    "fbs", 
                    "restecg", 
                    "thalach", 
                    "exang", 
                    "oldpeak", 
                    "slope", 
                    "ca", 
                    "thal", 
                    "target"
                }"""
    #heart_dict.popitem(linha)

