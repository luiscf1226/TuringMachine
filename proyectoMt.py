from turingParserClass import TuringParserClass
import csv

#variables globales de estados 
estadosListas = []
palabraLista=[]
estado_actual_mt=''
estado_nuevo_mt=''
indice_mt=''
movimiento_mt=''
estado_seguir_mt=''


def cargarCSV(archivo):
    global estadosListas  
    print("Cargando csv: " + archivo)
    try:
        #Leer el csv para cargar el objeto por cada fila, delimeter csv
        with open(archivo + ".csv", newline='', encoding='utf-8-sig') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if row[0] != 'estado actual': 
                    estadoA, charS, charE, movimiento, estadoNuevo = row[:5]
                    rowAdd = TuringParserClass(estadoA, charS, charE, movimiento, estadoNuevo)
                    estadosListas.append(rowAdd)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Ocurrió un error:", e)

    imprimirListas()

#Imprimir los estados de la MT
def imprimirListas():
    for objeto in estadosListas:
        print(objeto)  

def pedirPalabras():
    global palabraLista  

    if len(estadosListas) != 0:
        palabra = input("Por favor, ingrese la palabra: ")
        #se ocupa agregar vacio o BLANK al principio o final almenos una vez
        palabraLista = ['B'] + list(palabra) + ['B']
        #indice,estado actual de la MT
        estado_actual_mt = estadosListas[0].getEstadoActual()
        indice = 1
        terminar = False

        while not terminar:
            transicion_encontrada = False
            for i, estado in enumerate(estadosListas):
                if estado.getCharEnString() == palabraLista[indice] and estado.getEstadoActual() == estado_actual_mt:
                    transicion_encontrada = True
                    movimiento_mt = estado.getMovimiento()
                    palabraLista[indice] = estado.getCharEscribir()
                    estado_actual_mt = estado.getEstadoNuevo()  

                    print(f"Iteración: {i}, Movimiento: {movimiento_mt}")

                    #validaciones de movimiento
                    if movimiento_mt == 'R':
                        indice += 1 
                        #aumentar el indica que la cadena se movió hacia la derecha
                    elif movimiento_mt == 'L':
                        indice -= 1
                        #disminuir el indica que la cadena se movió hacia la izquierda
                    elif movimiento_mt == 'H':
                        terminar = True
                        #indica que la MT entró en un estado terminal para la cadena
                        break

            if not transicion_encontrada:
                print("No se encontró una transición válida para el estado actual y el carácter leído.")
                break

            imprimirPalabras()
            print("Estado Actual de la MT:", estado_actual_mt)
            print("Movimiento Final:", movimiento_mt)
        #limpia las variables uilizadas
        palabraLista.clear() 
        estado_actual_mt = None  
        indice = 0  
        terminar = False  

#imprime las palabras
def imprimirPalabras():
    palabra_concatenada = ''.join(palabraLista)
    print(palabra_concatenada)

def SeleccionarMenu():
    while True:
        print("\n1. Cargar csv")
        print("2. Escribir y probar palabra")
        print("3. Salir del programa")
        try:
            option = int(input("Por favor seleccione una opción: "))
            if option in [1, 2, 3]:
                return option
            else:
                print("Por favor, ingrese una opción válida (1, 2, o 3).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def menuPrincipal():
    while True:
        option = SeleccionarMenu()
        if option == 1:
            archivo = input("Escriba el nombre del csv sin la extensión: ")
            cargarCSV(archivo)
        elif option == 2:
            pedirPalabras()
        elif option == 3:
            print("Saliendo del programa.")
            break

def main():
    menuPrincipal()

if __name__ == '__main__':
    main()
