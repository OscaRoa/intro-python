import openpyxl

print("Abriendo libro...")

wb = openpyxl.load_workbook("censuspopdata.xlsx")

sheet = wb["Population by Census Tract"]

print("Leyendo filas...")

datos_censo = {}

for fila in range(2, sheet.max_row + 1):
    fila_str = str(fila)
    estado = sheet['B' + fila_str].value
    condado = sheet['C' + fila_str].value
    poblacion = sheet['D' + fila_str].value

    datos_censo.setdefault(estado, {})
    datos_censo[estado].setdefault(condado, {"tramos": 0, "poblacion": 0})
    datos_censo[estado][condado]["tramos"] += 1
    datos_censo[estado][condado]["poblacion"] += int(poblacion)

arizona = datos_censo["AZ"]
poblacion_arizona = 0

for condado in arizona:
    poblacion_arizona += arizona[condado]["poblacion"]
    print("La poblacion de", condado, "es de", arizona[condado]["poblacion"], "personas")

print("La poblacion total de Arizona es de", poblacion_arizona, "personas")