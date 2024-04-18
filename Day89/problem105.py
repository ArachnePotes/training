import numpy

class Mapa:
    '''
    Usage:

    mi_map = Mapa( [] ,2,0)
    mi_map.show() 
    '''
    def __init__(self,mapa_arr,dimentions,filler={'None':0, 'elsewere':1,'Debug': 5 ,'custom':[] }):
        self.mapa_arr = mapa_arr
        self.dimentions = int(dimentions)
        self.fill = filler

    '''
    def agregar_conexion(self, nodo1, nodo2, costo):
        if nodo1 not in self.conexiones:
            self.conexiones[nodo1] = []
        if nodo2 not in self.conexiones:
            self.conexiones[nodo2] = []
        
        self.conexiones[nodo1].append((nodo2, costo))
        self.conexiones[nodo2].append((nodo1, costo))
    '''
    def obtener_vecinos(self):
        pass
    
    def fill_map(self,option):
        map_0 = list(self.mapa_arr[0].split(','))
        map_1 = list(self.mapa_arr[1].split(','))
        map_2 = list(self.mapa_arr[1].split(',')) 
        map_3 = list(self.mapa_arr[2].split(',')) 
        map_4 = list(self.mapa_arr[3].split(','))
        map_5 = list(self.mapa_arr[4].split(',')) 
        map_6 = list(self.mapa_arr[5].split(',')) 
        map_7 = list(self.mapa_arr[6].split(',')) 
        map_8 = list(self.mapa_arr[7].split(',')) 
        map_9 = list(self.mapa_arr[8].split(',')) 
        map_10 = list(self.mapa_arr[9].split(',')) 
        
        d= {'map_1' : map_1[1::] ,
        'map_2' : map_2[1::] ,
        'map_3' : map_3[1::] ,
        'map_4' : map_4[1::] ,
        'map_5' : map_5[1::],
        'map_6' : map_6[1::],
        'map_7' : map_7[1::],
        'map_8' : map_8[1::],
        'map_9' : map_9[1::],
        'map_10' : map_10[1::],
        }
        
        
        map_global = [map_0,map_1,map_2,map_3,map_4,map_5,map_6]
        if  option == 'elsewere':
            print(f"""
                  \'we are here\'
                    dimensiones anexadas {self.dimentions}
                    {map_0} {map_1} {map_1[0]} {0}
                    """
                  )
            for i in map_1:
                    if i in ['x','[',']','a','"','"']:
                        print(map_1)
                    else:
                        map_1[int(i)] = '0'
            print(f"""
                  \'we are here\'
                    dimensiones anexadas {self.dimentions}
                    {map_0} {map_1} {map_1[0]} {1}
                    estamos evaluando tantas veces como caracteres queremos evadir
                    """
                  )
            result = []
            s = "map_"
            counter = 1
            while(counter<len(map_1)):#probando con el primero
                mapx = (s + str(counter) )
                print(mapx)
                for i in d[mapx]:
                    if i in ['x','[',']','a','"','"','b','c','d','e','f','g','h','i','j',]:
                        print(f"{map_0} { d[mapx]} {mapx}")
                    else: 
                        d[mapx][int(i)]  = 0
                        counter += 1
                        layer = d[mapx]
                        print(layer)
                        result.append(layer)
            for i in map_global:
                print(i)
        if option == None:
            remove_x = list(filter(lambda x: (x!='x'),map_1))
            print(remove_x)
        
        return True    

    def show(self):
        pass
        

# Crear un mapa
tuto = [ 'x','y','z']
x = 'flag' 
mix_map = ['border',                        
'[,0,x,2,3,4,5,6,7,8,9,],[,a,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,b,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,c,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,d,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,e,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,f,]' ,
'[,x,1,2,3,4,5,x,7,8,9,],[,g,]' ,
'[,0,1,2,3,x,5,6,7,8,9,],[,h,]' ,
'[,0,1,2,x,4,5,6,7,8,9,],[,i,]' ,
'[,0,1,2,3,4,5,6,7,8,9,],[,j,]' ,  
]
mi_map = Mapa( mix_map ,1,'none')

mi_map.fill_map('elsewere')
mi_map.fill_map('debug')

mi_map.show() 

'''
# Definir conexiones
mapa.agregar_conexion('a', 'b', 1)
mapa.agregar_conexion('a', 'c', 3)
mapa.agregar_conexion('b', 'd', 2)
mapa.agregar_conexion('c', 'd', 2)

# Definir los nodos de inicio y fin
start = Nodo('a', 0, 0, None)  # Nodo inicial
end = Nodo('d', 1, 1, None)    # Nodo final
'''



# Ejecutar el algoritmo A*
#ruta = aStar(mapa, start, end)
'''
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

# section
    
'''
Lista abierta: [('a', 0)]
Lista cerrada: []
Explorando nodo actual: ('a', 0)
No se encontró una ruta válida.
'''