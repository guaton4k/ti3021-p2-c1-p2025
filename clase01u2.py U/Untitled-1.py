class Cliente:
    def __init__(self, nombre: str, rut: str, edad: int):
        self.__nombre: str = nombre
        self.__rut: str = rut
        self__edad: int = edad

def nombre(self):
    return self.__nombre

Cliente1: Cliente = Cliente(
    nombre="Felipe Villaroel",
    rut="21789567-k",
    edad=21
)

print(Cliente1.nombre)