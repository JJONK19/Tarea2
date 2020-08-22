import json
print("--------------------------------------------------------------------------------------------")
print("ARCHIVOS .JSON    TIPO DE ESTRUCTURA: LISTAS")
print("--------------------------------------------------------------------------------------------")

def LecturaJSON():
    archivo = open('ArchivoJson.Json')
    carga = json.load(archivo)
    archivo.close()
    print(carga)
    return archivo

prueba = LecturaJSON()
for nombre in prueba:
    print(nombre)

import xml.etree.ElementTree as ET
print("--------------------------------------------------------------------------------------------")
print("ARCHIVOS .JSON    TIPO DE ESTRUCTURA: ARBOL")
print("--------------------------------------------------------------------------------------------")

Archivo = ET.parse('ArchivoXML.xml')
raiz = Archivo.getroot()

for nodo in raiz:
    for subnodo in nodo:
        print(subnodo.text)



import csv
print("--------------------------------------------------------------------------------------------")
print("ARCHIVOS .CSV    TIPO DE ESTRUCTURA: TABLA")
print("--------------------------------------------------------------------------------------------")

with open('ArchivoCSV.csv') as csv1:

    i = 0
    for row in csv1:
        if i == 0:
            print(f'{", ".join(row)}')
            i += 1
        else:
            print(f'\t{row[0]}  {row[1]}  {row[2]} {row[3]}.')
            i += 1
