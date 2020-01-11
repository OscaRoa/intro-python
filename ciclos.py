# gatito = {
#     "nombre": "Michi",
#     "edad": 8,
#     "raza": "Callejero",
#     "vacunado": True,
#     "hambriento": True
# }

# def alimentar(gatito):
#     if gatito["hambriento"]:
#         gatito["hambriento"] = False
#         print("Le daremos comida :)")
#     else:
#         print("El gato ya comio")

# def tiene_hambre(gatito):
#     if gatito["hambriento"]:
#         print("El gato tiene hambre")
#     else:
#         print("El gato no tiene hambre")

# tiene_hambre(gatito)

# alimentar(gatito)

# tiene_hambre(gatito)



# calificaciones = {
#     "ccc": 10,
#     "neuro": 10,
#     "social": 10,
#     "clinica": 10
# }

# persona = {
#     "nombre": "Oscar",
#     "edad": 23,
#     "calificaciones": calificaciones
# }

# def obtener_calificaciones(persona):
#     if persona["calificaciones"]:
#         for i in persona["calificaciones"]:
#             print(i, persona["calificaciones"][i])
#     else:
#         print("No hay calificaciones")

# obtener_calificaciones(persona)

def promedio(numeros):
    total = sum(numeros)
    return total/len(numeros)

lista_1 = range(9)

promedio_lista_1 = promedio(lista_1)
print(promedio_lista_1)
