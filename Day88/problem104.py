'''
            Simple implementation of A*
                
            El algoritmo A* funciona de la siguiente manera:

            Comienza en el nodo inicial.
            Calcula la distancia estimada entre el nodo actual y el objetivo.
            Agrega el nodo actual a una lista de nodos abiertos.
            Mientras la lista de nodos abiertos no esté vacía:
            Elige el nodo con la distancia estimada más baja.
            Si el nodo actual es el objetivo, termina el algoritmo.
            Expande el nodo actual, agregando sus vecinos a la lista de nodos abiertos.
            Actualiza las distancias estimadas de los vecinos.


            Para implementar la búsqueda A* en Python, necesitamos definir las siguientes clases:

            Nodo: Representa un nodo en el mapa.
            Lista de abiertos: Representa una lista de nodos que aún no se han explorado.
            Lista de cerrados: Representa una lista de nodos que ya se han explorado.
'''

class Nodo:
    def __init__(self, x, y, cost, padre=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.padre = padre

class ListaAbierta:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)
    
    def eliminar(self, nodo):
        self.nodos.remove(nodo)

    def obtener_nodo_mas_cercano(self):
        return min(self.nodos, key=lambda nodo: nodo.cost)

class ListaCerrada:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)
    
    def contiene(self, nodo):
        return nodo in self.nodos

'''
# esta implementacion esta erronea 
def aStar(mapa, start, end):
    la = ListaAbierta()
    lc = ListaCerrada()

    # Comienza en el nodo inicial.
    la.agregar(start)

    while la.nodos:
        # nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
        nodo_actual = la.obtener_nodo_mas_cercano()
        la.eliminar(nodo_actual)

        # Si el nodo actual es el objetivo, termina el algoritmo
        if nodo_actual == end:
            return nodo_actual.padre

        # Expande el nodo actual
        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            # Calcula la distancia estimada hasta el nodo objetivo
            costo_estimado = nodo_actual.cost + nodo_vecino.cost

            # Si el nodo vecino no está en la lista de cerrados
            if not lc.contiene(nodo_vecino):
                # Si el nodo vecino no está en la lista de abiertos o tiene un costo menor
                if nodo_vecino not in la.nodos or costo_estimado < nodo_vecino.cost:
                    # Actualiza el padre del nodo vecino
                    nodo_vecino.padre = nodo_actual
                    # Actualiza el costo del nodo vecino
                    nodo_vecino.cost = costo_estimado
                    # Agrega el nodo vecino a la lista de abiertos
                    la.agregar(nodo_vecino)
        
        # Agrega el nodo actual a la lista de cerrados
        lc.agregar(nodo_actual)
'''
''' 
# implementacion #2 , tambien con errores
def aStar(mapa, start, end):
    la = ListaAbierta()
    lc = ListaCerrada()

    # Comienza en el nodo inicial.
    la.agregar(start)

    while la.nodos:
        # nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
        nodo_actual = la.obtener_nodo_mas_cercano()
        la.eliminar(nodo_actual)

        # Si el nodo actual es el objetivo, termina el algoritmo
        if nodo_actual == end:
            return nodo_actual

        # Expande el nodo actual
        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            # Calcula la distancia estimada hasta el nodo objetivo
            costo_estimado = nodo_actual.costo + 1  # asumiendo costo uniforme de 1 para cada movimiento

            # Si el nodo vecino no está en la lista de cerrados
            if not lc.contiene(nodo_vecino):
                # Si el nodo vecino no está en la lista de abiertos o tiene un costo menor
                if nodo_vecino not in la.nodos or costo_estimado < nodo_vecino.cost:
                    # Actualiza el padre del nodo vecino
                    nodo_vecino.padre = nodo_actual
                    # Actualiza el costo del nodo vecino
                    nodo_vecino.cost = costo_estimado
                    # Agrega el nodo vecino a la lista de abiertos
                    la.agregar(nodo_vecino)
        
        # Agrega el nodo actual a la lista de cerrados
        lc.agregar(nodo_actual)

    # Si no se encontró una ruta válida
    return None
'''

'''
# implementacion #3
def aStar(mapa, start, end):
    la = ListaAbierta()
    lc = ListaCerrada()

    # Comienza en el nodo inicial.
    la.agregar(start)

    while la.nodos:
        # nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
        nodo_actual = la.obtener_nodo_mas_cercano()
        la.eliminar(nodo_actual)

        # Si el nodo actual es el objetivo, termina el algoritmo
        if nodo_actual == end:
            return nodo_actual

        # Expande el nodo actual
        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            # Calcula la distancia estimada hasta el nodo objetivo
            costo_estimado = nodo_actual.cost + 1  # asumiendo costo uniforme de 1 para cada movimiento

            # Si el nodo vecino no está en la lista de cerrados
            if not lc.contiene(nodo_vecino):
                # Si el nodo vecino no está en la lista de abiertos o tiene un costo menor
                if nodo_vecino not in la.nodos or costo_estimado < nodo_vecino.cost:
                    # Actualiza el padre del nodo vecino
                    nodo_vecino.padre = nodo_actual
                    # Actualiza el costo del nodo vecino
                    nodo_vecino.cost = costo_estimado
                    # Agrega el nodo vecino a la lista de abiertos
                    la.agregar(nodo_vecino)
        
        # Agrega el nodo actual a la lista de cerrados
        lc.agregar(nodo_actual)

    # Si no se encontró una ruta válida
    return None
'''
''''
# implementacion #4 
def aStar(mapa, start, end):
    la = ListaAbierta()
    lc = ListaCerrada()

    # Comienza en el nodo inicial.
    la.agregar(start)

    while la.nodos:
        # nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
        nodo_actual = la.obtener_nodo_mas_cercano()
        la.eliminar(nodo_actual)

        # Si el nodo actual es el objetivo, termina el algoritmo
        if nodo_actual == end:
            return end  # Devolver el nodo final

        # Expande el nodo actual
        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            # Calcula la distancia estimada hasta el nodo objetivo
            costo_estimado = nodo_actual.cost + 1  # asumiendo costo uniforme de 1 para cada movimiento

            # Si el nodo vecino no está en la lista de cerrados
            if not lc.contiene(nodo_vecino):
                # Si el nodo vecino no está en la lista de abiertos o tiene un costo menor
                if nodo_vecino not in la.nodos or costo_estimado < nodo_vecino.cost:
                    # Actualiza el padre del nodo vecino
                    nodo_vecino.padre = nodo_actual
                    # Actualiza el costo del nodo vecino
                    nodo_vecino.cost = costo_estimado
                    # Agrega el nodo vecino a la lista de abiertos
                    la.agregar(nodo_vecino)
        
        # Agrega el nodo actual a la lista de cerrados
        lc.agregar(nodo_actual)

    # Si no se encontró una ruta válida
    return None
'''
# implementacion #5 
def aStar(mapa, start, end):
    la = ListaAbierta()
    lc = ListaCerrada()

    # Comienza en el nodo inicial.
    la.agregar(start)

    while la.nodos:
        print("Lista abierta:", [(nodo.x, nodo.y) for nodo in la.nodos])
        print("Lista cerrada:", [(nodo.x, nodo.y) for nodo in lc.nodos])

        # nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
        nodo_actual = la.obtener_nodo_mas_cercano()
        print("Explorando nodo actual:", (nodo_actual.x, nodo_actual.y))
        la.eliminar(nodo_actual)

        # Si el nodo actual es el objetivo, termina el algoritmo
        if nodo_actual == end:
            return end  # Devolver el nodo final

        # Expande el nodo actual
        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            print("Explorando vecino:", (nodo_vecino.x, nodo_vecino.y))

            # Calcula la distancia estimada hasta el nodo objetivo
            costo_estimado = nodo_actual.cost + 1  # asumiendo costo uniforme de 1 para cada movimiento

            # Si el nodo vecino no está en la lista de cerrados
            if not lc.contiene(nodo_vecino):
                # Si el nodo vecino no está en la lista de abiertos o tiene un costo menor
                if nodo_vecino not in la.nodos or costo_estimado < nodo_vecino.cost:
                    # Actualiza el padre del nodo vecino
                    nodo_vecino.padre = nodo_actual
                    # Actualiza el costo del nodo vecino
                    nodo_vecino.cost = costo_estimado
                    # Agrega el nodo vecino a la lista de abiertos
                    la.agregar(nodo_vecino)
        
        # Agrega el nodo actual a la lista de cerrados
        lc.agregar(nodo_actual)

    # Si no se encontró una ruta válida
    return None



# la idea es separar el caso de prueba  del algoritmo
#from problem104 import Nodo, ListaAbierta, ListaCerrada, aStar

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
end = Nodo('d', 1, 1, None)    # Nodo final

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

'''
Lista abierta: [('a', 0)]
Lista cerrada: []
Explorando nodo actual: ('a', 0)
No se encontró una ruta válida.
'''