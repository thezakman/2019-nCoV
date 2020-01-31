import requests
import json
from datetime import datetime

hoje = datetime.now()
#dia = hoje.strftime("%d/%m/%Y")
dia = hoje.strftime("%d/%m/%Y %H:%M:%S")

url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22"
atributos = "%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true"



r1 = requests.get(url + "Confirmed" + atributos)
r2 = requests.get(url + "Recovered" + atributos)
r3 = requests.get(url + "Deaths" + atributos)


valor1 = json.loads(r1.text)
valor2 = json.loads(r2.text)
valor3 = json.loads(r3.text)

infectados = valor1['features'][0]['attributes']['value']
recuperados = valor2['features'][0]['attributes']['value']
mortes = valor3['features'][0]['attributes']['value']


print("\n[*] Coronavirus (2019-nCoV)")
print(25*("_"))
print("Data: " + str(dia))
print(25*("-"))
print("\n[Infectados]: " + str(infectados))
print("[Recuperados]: " + str(recuperados))
print("[Mortes]: " + str(mortes) + "\n")