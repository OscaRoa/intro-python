import requests # Nos sirve para interactuar con páginas web
from bs4 import BeautifulSoup # Con este otro paquete nos ayuda a extraer contenido de un HTML
import matplotlib.pyplot as plt # La utilizaremos para hacer las gráficas de frecuencias

# Importamos las funciones del módulo de python que creamos
from utils import filtrar_palabras, palabras_mas_frecuentes

# URL's de las noticias de las cuales extraeremos datos
imparcial_url = "https://www.elimparcial.com/mexico/Ni-una-menos-Mujeres-se-manifiestan-contra-violencia-de-genero-20191125-0123.html"
telediario_url = "https://laguna.telediario.mx/nacional/hacen-pintas-y-destrozos-en-reforma-en-marcha-contra-violencia-de-genero"

# Lista de palabras a excluir para calcular las frecuencias de las palabras en las noticias
excluido = [
    "la", "las", "el", "los", "de", "del", "se", "en", "y", "su", "a", "que",
    "por", "como", "para", "al", "17", "han", "lo", "con", "esta", "durante", "sobre"
]

print("Obteniendo datos de las páginas...\n")

# Con el método get de requests obtenemos el contenido de las páginas que queremos usar
page_i = requests.get(imparcial_url)
page_t = requests.get(telediario_url)

print("Datos de las páginas obtenidos.\n")

# Por medio de BeautifulSoup nos será muy fácil extraer el texto de las noticias
# e ignorar todo lo demás del contenido que no nos interesa
soup_i = BeautifulSoup(page_i.content, 'html.parser')
soup_t = BeautifulSoup(page_t.content, 'html.parser')

##################################################
# Sección para la nota del periódico el Imparcial
##################################################

# Una vez tenemos nuestra variable con el contenido de la página tenemos que filtrar
# lo que nos interesa de todo el HTML
cuerpo_noticia_i = soup_i.find("div", class_="newsfull__body").find_all("p")

# Una vez filtrado el contenido relevante del HTML,
# quitamos las palabras auxiliares tales como artículos, preposiciones, conjunciones,
# pronombres personales, etc. Todo lo que no nos interese.
palabras_imparcial = filtrar_palabras(cuerpo_noticia_i, excluido)

# Conteo de palabras en la nota del periodico El Imparcial mediante un objeto Counter
top_15_imparcial = palabras_mas_frecuentes(palabras_imparcial, 15)

##################################################
# Sección para la nota del periódico Telediario
##################################################

cuerpo_noticia_t = soup_t.find("div", class_="field--text-paragraph").find_all("p")
palabras_telediario = filtrar_palabras(cuerpo_noticia_t, excluido)
top_15_telediario = palabras_mas_frecuentes(palabras_telediario, 15)

#####################################################
# Gráficas de frecuencias de palabras de ambas notas
#####################################################

# Finalmente creamos las gráficas de las palabras con sus frecuencias en una
# gráfica de barras con matplotlib para cada nota

# Grid de las gráficas
fig = plt.figure()
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)

# Datos a graficar
plt1.bar(top_15_imparcial.keys(), top_15_imparcial.values(), color = "lightgreen")
plt2.bar(top_15_telediario.keys(), top_15_telediario.values(), color = "lightblue")

# Títulos de la figura y de las gráficas
fig.suptitle("Frecuencia de palabras sobre la marcha feminista del 25 de Noviembre")
plt1.set(title = "Nota del periódico El Imparcial", ylabel = "frecuencia")
plt2.set(title = "Nota del periódico Telediario", ylabel = "frecuencia")

# Visualizar y guardar plot maximizado
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()
fig.savefig("graficas.png")
