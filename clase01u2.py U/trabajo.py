from datetime import date

class persona:
    def __init__(self,
            rut: str,
            nombres: str,
            apellido: str,
            fecha_nacimiento: date,
            telefono: int,
            cod_area: int,
    ):
        self.rut: str = rut
        self.nombres: str = nombres
        self.apellido: str = apellido
        self.fecha_nacimiento: date = fecha_nacimiento
        self.telefono: int = telefono
        self.cod_area: int = cod_area
        
    def __str__(self):
        return f"{self.rut} {self.nombres} {self.apellido} {self.fecha_nacimiento} {self.cod_area} {self.telefono}"


personas: list[persona] = []

"""
CRUD
Create
read
update
delete
"""

def persona_existe(persona_nueva: persona) -> bool:
    for persona in personas:
        if persona.rut == persona_nueva.rut:
            print("Persona existe")
            return True
    print("Persona no existe")
    return False


def create_persona():
    rut: str = input("Ingrese el rut de la persona: ")
    nombres: str = input("Ingrese los nombres de la perosona: ")
    apellidos: str = input("Ingrese los apellidos de la persona: ")
    dia_nacimiento = int(input("Ingrese el dia de nacimiento de la persona: "))
    mes_nacimiento = int(input("Ingrese el mes de nacimiento de la persona: "))
    anio_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
    fecha_nacimiento: date = date(
        year=anio_nacimiento,
        month=mes_nacimiento,
        day=dia_nacimiento
    )


    cod_area: int = int(input("Ingrese el codigo de area del telefono de la perona: "))
    telefono: int = int(input("Ingrese el numero de telefono de la persona: "))
    persona = persona(
        rut=rut,
        nombres=nombres,
        apellidos=apellidos,
        fecha_nacimiento=fecha_nacimiento,
        cod_area=cod_area,
        telefono=telefono,
        persona=persona
    )
    if persona_existe(persona):
        return print(f"La persona con el rut {persona.rut} ya existe. Intente con otro rut")

def read_personas():
    for persona in personas:
        print(persona)

def update_personas():
    pass

def delete_personas():
    pass

while True:
    print(
        """
        ========================
        || Gestor de personas ||
        ========================
        1. Crear persona
        2. Listar personas
    """)