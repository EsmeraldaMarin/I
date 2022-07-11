from ast import arg
import sys
import csv
import argparse
import datetime as dt

datetime = dt.date.today()

opciones = """
Bienvenido al programa de control de cheques
--------------------------------------------
Por favor ingrese una opcion:
1- Ingreso de datos
2- Salir
"""

runtime = True
parser = argparse.ArgumentParser(
    description="just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def readFile(url_file):
    cheques = []
    file = open(url_file, 'r')
    csvFile = csv.reader(file)
    for row in csvFile:
        if row != []:
            data = {
                "NroCheque": row[0],
                "CodigoBanco": row[1],
                "CodigoSucursal": row[2],
                "NumeroCuentaOrigen": row[3],
                "NumeroCuentaDestino": row[4],
                "Valor": row[5],
                "FechaOrigen": row[6],
                "FechaPago": row[7],
                "DNI": row[8],
                "Tipo": row[9],
                "Estado": row[10]
            }
            cheques.append(data)

    file.close()
    return cheques


def buscar_por_dni(dni, tipo):
    busqueda = []
    cant_cheches_encontrados = 0
    cheques = readFile(url_file)
    for cheque in cheques:
        if cheque["DNI"] == dni:
            if cheque['Tipo'].lower() == tipo or tipo == "":
                cant_cheches_encontrados += 1
                busqueda.append(cheque)

    numeros_de_cheque = []
    for cheque in busqueda:
        numeros_de_cheque.append(cheque["NroCheque"])

    for num in numeros_de_cheque:
        if numeros_de_cheque.count(num) > 1:
            return False

    busqueda.append(cant_cheches_encontrados)
    return busqueda


def mostrarcheques(cheques):
    for contacto in cheques:
        print(contacto['Nombre'], contacto['Apellido'],
              contacto['Telefono'], contacto['Tipo'])


def grabar_csv(busqueda, dni):
    file = open(f"{dni}_{datetime}.csv", "w")
    csvfile = csv.writer(file)
    for row in busqueda:
        csvfile.writerow([
            row['NroCheque'],
            row['CodigoBanco'],
            row['CodigoSucursal'],
            row['NumeroCuentaOrigen'],
            row['NumeroCuentaDestino'],
            row['Valor'],
            row['FechaOrigen'],
            row['FechaPago'],
            row['DNI'],
            row['Tipo'],
            row['Estado']])
    file.close()
    print('Se grabo el archivo CSV')


if __name__ == '__main__':

    while runtime:
        print(opciones)
        op = int(input('\nIngrese una opcion: '))

        if op == 1:
            url_file = input(
                "Ingrese el nombre del archivo que contiene los cheques (sin extension): ")+".csv".lower()
            dni = input("Ingrese el dni del usuario a consultar: ").lower()
            tipo = input(
                "Ingrese el tipo de cheque a buscar EMITIDO o DEPOSITADO: ").lower()
            salida = input(
                "Ingrese si desea recibir la salida por PANTALLA o CSV: ").lower()
            """ try: """
            busqueda = buscar_por_dni(dni, tipo)
            try:
                if busqueda:
                    if salida == "pantalla":
                        print('------RESULTADOS------')
                        print(
                            f"\nSe encontraron {busqueda[-1]} cheques {tipo}s con dni {dni}\n")
                        busqueda.pop()
                        for res in busqueda:
                            print(f"-->  {res}\n")
                    elif salida == "csv":
                        busqueda.pop()
                        grabar_csv(busqueda, dni)
                    else:
                        print('Opcion invalida')
                else:
                    print('\n')
                    print('-' * 60)
                    print('Se encontraron cheques repetidos')
                    print('ERROR. Hay cheques duplicados')

            except:
                print("Ingreso un dni erroneo")

        elif op == 2:
            print("Usted selecciono la opcion de SALIR")
            runtime = False


""" parser.add_argument("-f", "--file", help="Nombre del archivo csv")
parser.add_argument("-dni", "--dni", help="DNI del cliente")
parser.add_argument("-s", "--salida", help="Salida: pantalla o csv")
parser.add_argument("-t", "--tipo", help="Tipo de cheque: EMITIDO o DEPOSITADO")

file = parser.parse_args().file
dni = parser.parse_args().dni
salida = parser.parse_args().salida
tipo = parser.parse_args().tipo
print("Archivo: ", file)
print("DNI: ", dni)
print("SALIDA: ", salida)
print("TIPO: ",tipo)

if salida.lower() == "pantalla":
    print(readFile())
else:
    print("grabado archivo") """
