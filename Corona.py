import requests
import json
from datetime import datetime

hoje = datetime.now()
dia = hoje.strftime("%d/%m/%Y %H:%M:%S")

# Adicionar paises
# https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=250&cacheHint=true
#
#

url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22"
atributos = "%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true"



r1 = requests.get(url + "Confirmed" + atributos)
r2 = requests.get(url + "Recovered" + atributos)
r3 = requests.get(url + "Deaths" + atributos)

r4 = requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=250&cacheHint=true")

valor1 = json.loads(r1.text)
valor2 = json.loads(r2.text)
valor3 = json.loads(r3.text)
valor4 = json.loads(r4.text)



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

print(25*("_"))
print ()
for x in range(len(valor4['features'])):
    local = valor4['features'][x]['attributes']['Country_Region']
    confirmados= valor4['features'][x]['attributes']['Confirmed']

    print(local + ":" , confirmados)
