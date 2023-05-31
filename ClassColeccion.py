import numpy as np
from ClassEmpleado import Empleado
from ClassEmpleadoContratado import Empleado_Contratado
from ClassEmpleadoPlanta import Empleado_Planta
from ClassEmpleadoExterno import Empleado_Externo

class Coleccion:
    __actual = int
    __dimension = int
    __incremento = 5
    __empleados = object

    def __init__(self, dimension):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension
        self.__actual = 0

    def agregar_empleado(self, empleado):
        #Aca se verifica la dimension y si es igual al indice se informa que no se agregan mas empleados
        if self.__actual == self.__dimension:
            print("No se pueden agregar más empleados.")
        else:
            #se carga el empleado
            self.__empleados[self.__actual] = empleado
            self.__actual += 1

    def mostrar_arreglo(self):
        for empleado in self.__empleados[:self.__actual]:
            print(empleado.Datos_Empleado())

    def registrar_Horas(self, dni_buscado, cant_horas):
        i = 0
        while i < len(self.__empleados[:self.__actual]):
            empleado = self.__empleados[i]
            if str(empleado.get_dni()) == dni_buscado:
                if isinstance(empleado, Empleado_Contratado):
                    empleado.set_horas_trabajadas(int(empleado.get_horas_T()) + cant_horas)
                else:
                    print(f"El empleado con DNI {dni_buscado} no es un empleado contratado.")
            i += 1

    def total_tarea(self, tarea_buscada):
        total=0
        i = 0
        while i < len(self.__empleados[:self.__actual]):
            empleado = self.__empleados[i]
            if isinstance(empleado, Empleado_Externo):
                if str(empleado.get_tarea()).strip() == tarea_buscada.strip():
                    total = empleado.sueldo_empleado()
            i += 1
        print(f"El monto a pagar por la tarea {tarea_buscada} es de ${total}.")

    def ayuda_economica(self):
        print('LOS EMPLEADOS QUE NECESITAN LA AYUDA ECONOMICA SON: ')
        for empleado in self.__empleados[:self.__actual]:
            if float(empleado.sueldo_empleado()) < 150000:
                print(f'Nombre:{empleado.get_nombre()} \nDireccion:{empleado.get_direccion()}'
                      f'\nDNI:{empleado.get_dni()}')

    def calcular_sueldo(self):
        for empleado in self.__empleados[:self.__actual]:
            print(f'Nombre:{empleado.get_nombre()} \nTelefono:{empleado.get_telefono()} \nSueldo a Cobrar:{empleado.sueldo_empleado()}')
