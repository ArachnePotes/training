from problem104 import Nodo, ListaAbierta, ListaCerrada, aStar

class Mapa:
    def __init__(self):
        self.conexiones = {}

    def agregar_conexion(self, nodo1, nodo2, costo):
        if nodo1 not in self.conexiones:
            self.conexiones[nodo1] = []
        if nodo2 not in self.conexiones:
            self.conexiones[nodo2] = []
        
        self.conexiones[nodo1].append((nodo2, costo))
        self.conexiones[nodo2].append((nodo1, costo))

    def obtener_vecinos(self, nodo):
        if nodo in self.conexiones:
            return [nodo_costo[0] for nodo_costo in self.conexiones[nodo]]
        else:
            return []

# Crear un mapa
mapa = Mapa()

# Definir conexiones
mapa.agregar_conexion('a', 'b', 1)
mapa.agregar_conexion('a', 'c', 3)
mapa.agregar_conexion('b', 'd', 2)
mapa.agregar_conexion('c', 'd', 2)

# Definir los nodos de inicio y fin
start = Nodo('a', 0, 0, None)  # Nodo inicial
end = Nodo('d', 0, 0, None)    # Nodo final

# Ejecutar el algoritmo A*
ruta = aStar(mapa, start, end)

# Imprimir la ruta encontrada
if ruta:
    path = []
    nodo = ruta
    while nodo:
        path.append((nodo.x, nodo.y))
        nodo = nodo.padre
    print("Ruta encontrada:", "->".join(reversed(path)))
else:
    print("No se encontró una ruta válida.")
