from ClassEmpleado import Empleado


class Empleado_Planta(Empleado):
    __sueldoB = float
    __antiguedad = int

    def __init__(self, dni, nombre, direccion, telefono, sueldoB, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoB = float(sueldoB)
        self.__antiguedad = int(antiguedad)

    def Datos_Empleado(self):
        datos = f'\nEmpleado de Planta:'
        datos += f'\n Nombre:{self.get_nombre()}, DNI:{self.get_dni()}'
        datos += f'\n Direccion:{self.get_direccion()}, Telefono:{self.get_telefono()}'
        datos += f'\n Sueldo Basico:{self.__sueldoB}, Años de Antiguedad:{self.__antiguedad}'
        return datos

    def sueldo_empleado(self):
        sueldo = float(self.__sueldoB + ((self.__sueldoB*0.01)*self.__antiguedad))
        return sueldo



