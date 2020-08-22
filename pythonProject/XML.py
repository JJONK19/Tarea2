import xml.etree.ElementTree as ET
print("--------------------------------------------------------------------------------------------")
print("ARCHIVOS .JSON    TIPO DE ESTRUCTURA: ARBOL")
print("--------------------------------------------------------------------------------------------")

Archivo = ET.parse('ArchivoXML.xml')
raiz = Archivo.getroot()

for nodo in raiz:
    for subnodo in nodo:
        print(subnodo.text)