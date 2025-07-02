"""Dado un diccionario de ventas donde las claves
son categorías de productos y los valores son listas
con los montos de cada venta, calcula el total de ventas
 por categoría y el total general.
Entrada:
ventas = {
    "Electrónica": [200, 150, 300],
    "Ropa": [50, 60, 40],
    "Hogar": [80, 120]
}
Salida esperada:
totales = {"Electrónica": 650, "Ropa": 150, "Hogar": 200}
total_general = 1000"""

ventas = {
    "Electrónica": [200, 150, 300],
    "Ropa": [50, 60, 40],
    "Hogar": [80, 120]
}

totales = {}
totales_general = 0
suma_total = 0

for clave, valor in ventas.items():
    productos = clave
    vendido = valor
    totales_general = sum(vendido)
    totales[productos] = totales_general
    suma_total += sum(vendido)

print(f"totales = {totales}")
print(f"vendido en general = {suma_total}")

