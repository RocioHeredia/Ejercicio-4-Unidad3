from ClassEmpleado import Empleado
class Empleado_Contratado(Empleado):
    __fecha_I = str
    __fecha_F = str
    __cant_hora_T = int
    __valor_por_hora = float

    def __init__(self, dni, nombre, direccion, telefono, fecha_I, fecha_F,
                 cant_hora_T, valor_por_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_I = fecha_I
        self.__fecha_F = fecha_F
        self.__cant_hora_T = int(cant_hora_T)
        self.__valor_por_hora = int(valor_por_hora)

    def Datos_Empleado(self):
        datos = f'\nEmpleado Contratado:'
        datos += f'\n Nombre:{self.get_nombre()}, DNI:{self.get_dni()}'
        datos += f'\n Direccion:{self.get_direccion()}, Telefono:{self.get_telefono()}'
        datos += f'\n Fecha de Inicio:{self.__fecha_I}, Fecha de Finalizacion:{self.__fecha_F}'
        datos += f'\n Horas Trabajadas:{self.__cant_hora_T}, Valor por Hora:{self.__valor_por_hora}'
        return datos

    def sueldo_empleado(self):
        sueldo = float(self.__cant_hora_T * self.__valor_por_hora)
        return sueldo

    def get_horas_T(self):
        return self.__cant_hora_T

    def get_fecha_finalizo(self):
        return self.__fecha_F

    def get_fecha_inicio(self):
        return self.__fecha_I
    def set_horas_trabajadas(self, cant_horas):
        self.__cant_hora_T = cant_horas



