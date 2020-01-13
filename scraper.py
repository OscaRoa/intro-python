import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter

imparcial_url = "https://www.elimparcial.com/mexico/Ni-una-menos-Mujeres-se-manifiestan-contra-violencia-de-genero-20191125-0123.html"
telediario_url = "https://laguna.telediario.mx/nacional/hacen-pintas-y-destrozos-en-reforma-en-marcha-contra-violencia-de-genero"
excluido = [
    "la", "las", "el", "los", "de", "del", "se", "en", "y", "su", "a", "que",
    "por", "como", "para", "al", "17", "han", "lo", "con", "esta", "durante", "sobre"
]

print("Obteniendo datos de las páginas...\n")

page_i = requests.get(imparcial_url)
page_t = requests.get(telediario_url)

print("Datos de las páginas obtenidos.\n")

soup_i = BeautifulSoup(page_i.content, 'html.parser')
soup_t = BeautifulSoup(page_t.content, 'html.parser')

# Conteo de palabras en la nota del periodico El Imparcial
cuerpo_noticia_i = soup_i.find("div", class_="newsfull__body").find_all("p")
print(cuerpo_noticia_i)
for i in cuerpo_noticia_i:
    print(i)

palabras_imparcial = []

for elemento in cuerpo_noticia_i:
    lista_palabras_i = elemento.text.strip().lower().split()
    for palabra in lista_palabras_i:
        if palabra not in excluido:
            palabras_imparcial.append(palabra)

c_imparcial = Counter(palabras_imparcial)
top_15_imparcial = dict(c_imparcial.most_common(20))

plt.bar(top_15_imparcial.keys(), top_15_imparcial.values())
plt.show()

# Conteo de palabras en la nota del periodico Telediario
cuerpo_noticia_t = soup_t.find("div", class_="field--text-paragraph").find_all("p")
palabras_telediario = []

for elemento in cuerpo_noticia_t:
    lista_palabras_t = elemento.text.strip().lower().split()
    for palabra in lista_palabras_t:
        if palabra not in excluido:
            palabras_telediario.append(palabra)

c_telediario = Counter(palabras_telediario)
top_15_telediario = dict(c_telediario.most_common(20))

plt.bar(top_15_telediario.keys(), top_15_telediario.values())
plt.show()