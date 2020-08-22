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
