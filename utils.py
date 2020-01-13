from collections import Counter # Viene incluido en Python y tiene estructuras de datos optimizadas

# Funciones para filtrar las palabras encontradas en la nota y para obtener las palabras
# mas frecuentes
def filtrar_palabras(cuerpo_noticia, palabras_excluidas):
    """
    Regresa una lista de palabras ya filtradas.

    Las palabras a filtrar se determinan por el argumento palabras_excluidas.
    """
    palabras_filtradas = []
    for elemento in cuerpo_noticia:
        palabras = elemento.text.lower().strip(",.").split()
        for palabra in palabras:
            if palabra not in palabras_excluidas:
                palabras_filtradas.append(palabra)

    return palabras_filtradas

def palabras_mas_frecuentes(palabras, top):
    """
    Regresa un diccionario con las palabras más frecuentes de una lista.

    El argumento top determina cuantas palabras se contarán.
    """
    c = Counter(palabras)

    return dict(c.most_common(top))