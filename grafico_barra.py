import pandas as pd
import matplotlib
import matplotlib.pyplot as pyplot
import numpy as np
from dao.Suicidio import Suicidio  # Importação da Classe Suicidio

suicidio = Suicidio() # Instanciamento do objeto
#suicidio.medida_dispersao_suicido('female')
array_medida_dispersao =  suicidio.node_suicidio('suicidio_medida_dispersao')

array_total_suicidio_male = []     # Guardará os totais de suicidios do gênero Masculino
array_total_suicidio_female = []   # Guardará os totais de suicidios do gênero Feminimo 
label_array_categorias = []  # Guardará as categorias

# Responsável por carregar o List dos Suicídios do Genero Masculino e Categoria de Faixa etária
for i in range(len(array_medida_dispersao)): 
    if str(array_medida_dispersao[i]['genero']) == "male" :
        array_total_suicidio_male.append(int(array_medida_dispersao[i]['total_suicidio']))
        label_array_categorias.append(str(array_medida_dispersao[i]['faixa_etaria']))

# Responsável por carregar o List dos Suicídios do Genero Feminino
for i in range(len(array_medida_dispersao)): 
    if str(array_medida_dispersao[i]['genero']) == "female" :
        array_total_suicidio_female.append(int(array_medida_dispersao[i]['total_suicidio']))

x = np.arange(len(label_array_categorias)) # Label de Categorias
width = 0.35 # largura das colunas 

fig, ax = pyplot.subplots()
generoMasculino = ax.bar(x - width/2, array_total_suicidio_male, label='Masculino')
generoFeminino = ax.bar(x - width/2, array_total_suicidio_female, label='Feminino')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Nº Total de Suicidios')
ax.set_title('Número de Suicidio de 1985 a 2015 por Faixa Etária')
ax.set_xticks(x)
ax.set_xticklabels(label_array_categorias)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(generoMasculino)
autolabel(generoFeminino)

fig.tight_layout()

pyplot.show()