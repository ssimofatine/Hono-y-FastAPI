productos = [
    {"id": 1, "nombre": "Portátil Lenovo IdeaPad 5", "categoria": "portátiles",
    "precio": 749.99},
    {"id": 2, "nombre": "MacBook Air M3", "categoria": "portátiles", "precio": 1299.0},
    {"id": 3, "nombre": "Monitor LG UltraGear 27", "categoria": "monitores", "precio": 289.9},
    {"id": 4, "nombre": "Monitor Samsung Odyssey G5", "categoria": "monitores", "precio": 239.0},
    {"id": 5, "nombre": "Teclado mecánico Keychron K2", "categoria": "periféricos", "precio": 89.0},
    {"id": 6, "nombre": "Ratón Logitech MX Master 3", "categoria": "periféricos", "precio": 99.99},
    {"id": 7, "nombre": "SSD Samsung 990 PRO 1TB", "categoria": "componentes", "precio": 109.0},
    {"id": 8, "nombre": "Router TP-Link Archer AX55", "categoria": "redes", "precio": 84.99}
]
def obtener_productos():
    return productos

def obtener_producto(id):
    for producto in productos:
        if producto["id"] == id:
            return producto
    return None

def buscar_productos(texto):
    return [p for p in productos if texto.lower() in p["nombre"].lower()]