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
