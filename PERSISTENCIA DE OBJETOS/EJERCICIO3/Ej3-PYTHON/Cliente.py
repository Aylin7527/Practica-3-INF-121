class Cliente:
    def __init__(self, id, nombre, telefono):
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def __str__(self):
        return f"Cliente ID: {self.__id}, Nombre: {self.__nombre}, Teléfono: {self.__telefono}"