import csv
from ClassEmpleadoPlanta import Empleado_Planta
from ClassEmpleadoContratado import Empleado_Contratado
from ClassEmpleadoExterno import Empleado_Externo
from ClassColeccion import Coleccion

def cargar_datos(nombre_archivo, tipo_empleado, arreglo):
    archivo = open(nombre_archivo, encoding='utf-8-sig')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        empleado = tipo_empleado(*fila)
        arreglo.agregar_empleado(empleado)

def menu():
    print('1. Registrar horas')
    print('2. Total de tarea')
    print('3.  Ayuda Económica')
    print('4. Calcular sueldo')
    print('0. Salir')

def item1(arreglo):
    dni_ingresado = str(input('Ingrese DNI del empleado: '))
    cant_horas = int(input('Ingrese horas trabajadas: '))
    arreglo.registrar_Horas(dni_ingresado, cant_horas)

def item2(arreglo):
    tarea = str(input('Ingrese Nombre de Tarea: '))
    arreglo.total_tarea(tarea)

def item3(arreglo):
    arreglo.ayuda_economica()

def item4(arreglo):
    arreglo.calcular_sueldo()

if __name__ == '__main__':
    dimension_arreglo = int(input('Ingrese el Tamaño del Arreglo: '))
    arreglo = Coleccion(dimension_arreglo)
    cargar_datos('contratados.csv', Empleado_Contratado, arreglo)
    cargar_datos('planta.csv', Empleado_Planta, arreglo)
    cargar_datos('externos.csv', Empleado_Externo, arreglo)
    #arreglo.mostrar_arreglo()
    opcion = None
    while opcion != 0:
        menu()
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            item1(arreglo)

        elif opcion == 2:
            item2(arreglo)

        elif opcion == 3:
            item3(arreglo)

        elif opcion == 4:
            item4(arreglo)
        elif opcion == 0:
            print('Saliendo...')
            break
        else:
            opcion=int(input('Ingrese una opcion Valida: '))