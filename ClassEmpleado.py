class Empleado:
    __DNI = str
    __nombre = str
    __direccion = str
    __telefono = str

    def __init__(self, dni, nombre, direccion, telefono):
        self.__DNI = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__DNI

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono