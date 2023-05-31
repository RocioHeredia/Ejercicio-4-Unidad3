from ClassEmpleado import Empleado


class Empleado_Externo(Empleado):
    __tarea = str
    __monto_viatico = int
    __fecha_I = str
    __fecha_F = str
    __costo_obra = int
    __monto_seg_vida = int

    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_I, fecha_F, monto_viatico, costo_obra,
                 monto_seg_vida):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__monto_viatico = int(monto_viatico)
        self.__fecha_I = fecha_I
        self.__fecha_F = fecha_F
        self.__costo_obra = int(costo_obra)
        self.__monto_seg_vida = int(monto_seg_vida)

    def Datos_Empleado(self):
        datos = f'\nEmpleado Externo:'
        datos += f'\n Nombre:{self.get_nombre()}, DNI:{self.get_dni()}'
        datos += f'\n Direccion:{self.get_direccion()}, Telefono:{self.get_telefono()}'
        datos += f'\n Tarea:{self.__tarea}'
        datos += f'\n Monto Viatico:{self.__monto_viatico}'
        datos += f'\n Fecha de Inicio:{self.__fecha_I}, Fecha de Finalizacion:{self.__fecha_F}'
        datos += f'\n Costo de Obra:{self.__costo_obra}'
        datos += f'\n Monto de seguro de vida:{self.__monto_seg_vida}'
        return datos

    def get_fecha_finalizo(self):
        return self.__fecha_F

    def get_tarea(self):
        return self.__tarea

    def sueldo_empleado(self):
        sueldo = float(self.__costo_obra - self.__monto_viatico - self.__monto_seg_vida)
        return sueldo




