# Primera sección de la clase
# Intro a scripts
"""
Primera sección de la clase
Intro a scripts
"""
# Segunda sección
# Estructuras de control

if 3 > 5 and 3 > 2:
    print("Tres es mayor que cinco y que dos")

# edad = 18

# if edad > 18:
#     print("Loteria!")
# elif edad == 18:
#     print("Apenitas loteria!")
# else:
#     print("No loteria :(")

# Tercera seccion
# Funciones

def saludo(nombre):
    print("Hola", nombre)

def gana_loteria(edad):
    """
    Funcion que checa si la edad de la persona
    es valida para ganar la loteria
    """
    if edad > 18:
        print("Loteria!")
    elif edad == 18:
        print("Apenitas loteria")
    else:
        print("No loteria :(")

gana_loteria(18)
gana_loteria(29)
gana_loteria(3)