#Importaciones
import numpy as np
from Nodo import Nodo
from time import sleep
import random
#file = np.loadtxt("./Matriz/Matriz2.txt", dtype=np.float)
#Clase juego

class Game:
    
    '''
    Kahyberth Stiven Gonzalez Sayas:202060121
    Maria Camila Muñoz:202067738
    Daniel Stiven Ramirez:202067524
    Ingenieria De Sistemas
    ██████╗░██████╗░░█████╗░██╗░░░██╗███████╗░█████╗░████████╗░█████╗░
    ██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
    ██████╔╝██████╔╝██║░░██║░╚████╔╝░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║
    ██╔═══╝░██╔══██╗██║░░██║░░╚██╔╝░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║
    ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░
    '''

    #Matrices y listas Funcionales
    lst = np.matrix
    color = ['\033[1;32m','\033[1;34m','\033[1;33m','\033[1;31m','\033[1;35m','\033[1;36m','\033[1;37m','\n']
    cord = ['x','y','xI','yI'] #Coordenadas

    #Funcion para abrir el archivo
    def cargarArchivo(file):
        Game.lst = np.loadtxt(file,dtype=int)

    '''
    ██████╗░███████╗░██████╗
    ██╔══██╗██╔════╝██╔════╝
    ██║░░██║█████╗░░╚█████╗░
    ██║░░██║██╔══╝░░░╚═══██╗
    ██████╔╝██║░░░░░██████╔╝
    ╚═════╝░╚═╝░░░░░╚═════╝░
    '''
    #Recorrido DFS
    def dfs(matrix):
        print(matrix)
        nodes_created = 0
        expanded_nodes = 0

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j]==4:
                    posR = (j,i)
                    matrix[i][j]=0
                    break
            
        #Main_node
        main_node = Nodo(
            matrix,
            posR,
            [False,False,False],
            [posR],
            [posR]
        )

        pila = [main_node]

        while len(pila)>0:
            nodo = pila.pop(-1)
            expanded_nodes+=1
            if(nodo.condicionGanadora()):
                for i in range(len(nodo.recorrido)):
                    sleep(1)
                    print(Game.color[random.randint(0,6)],'>'*random.randint(0,8),'Recorrido: ',nodo.recorrido[i])
                return nodo.recorrido,nodes_created,expanded_nodes
                
            #Coordenadas del robot || Robot coordinates
            Game.cord[0] = nodo.posR[0]
            Game.cord[1] = nodo.posR[1]

            #Generador de Hijos || Sons Generator 

            #Arriba || UP
            Game.cord[2] = Game.cord[0]
            Game.cord[3] = Game.cord[1] - 1

            if(Game.cord[3]>= 0 and not( (Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]]!=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    pila.append(son)
            

            #Abajo || Down
            Game.cord[2] = Game.cord[0]
            Game.cord[3] = Game.cord[1] + 1

            if(Game.cord[3]<matrix.shape[0] and not((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]] !=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    pila.append(son)
        
            #Izquierda || Left
            Game.cord[2] = Game.cord[0]-1
            Game.cord[3] = Game.cord[1]

            if(Game.cord[2]>=0 and not ((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]] !=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    pila.append(son)
            

            #Derecha || Right
            Game.cord[2] = Game.cord[0]+ 1
            Game.cord[3] = Game.cord[1]

            if(Game.cord[2]<matrix.shape[1] and not((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]]!=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    pila.append(son)
        return "No hay Solucion",nodes_created,expanded_nodes



    '''
    ██████╗░███████╗░██████╗
    ██╔══██╗██╔════╝██╔════╝
    ██████╦╝█████╗░░╚█████╗░
    ██╔══██╗██╔══╝░░░╚═══██╗
    ██████╦╝██║░░░░░██████╔╝
    ╚═════╝░╚═╝░░░░░╚═════╝░
    '''
    def bfs(matrix):
        print(matrix)
        nodes_created = 0
        expanded_nodes = 0

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j]==4:
                    posR = (j,i)
                    matrix[i][j]=0
                    break
            
        #Main_node
        main_node = Nodo(
            matrix,
            posR,
            [False,False,False],
            [posR],
            [posR]
        )

        cola = [main_node]

        while len(cola)>0:
            nodo = cola.pop(0)
            expanded_nodes+=1
            if(nodo.condicionGanadora()):
                for i in range(len(nodo.recorrido)):
                    sleep(1)
                    print(Game.color[random.randint(0,6)],'>'*random.randint(0,8),'Recorrido: ',nodo.recorrido[i])
                return nodo.recorrido,nodes_created,expanded_nodes
                
            #Coordenadas del robot || Robot coordinates
            Game.cord[0] = nodo.posR[0]
            Game.cord[1] = nodo.posR[1]

            #Generador de Hijos || Sons Generator 

            #Arriba || UP
            Game.cord[2] = Game.cord[0]
            Game.cord[3] = Game.cord[1] - 1

            if(Game.cord[3]>= 0 and not( (Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]]!=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    cola.append(son)
            

            #Abajo || Down
            Game.cord[2] = Game.cord[0]
            Game.cord[3] = Game.cord[1] + 1

            if(Game.cord[3]<matrix.shape[0] and not((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]] !=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    cola.append(son)
        
            #Izquierda || Left
            Game.cord[2] = Game.cord[0]-1
            Game.cord[3] = Game.cord[1]

            if(Game.cord[2]>=0 and not ((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]] !=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    cola.append(son)
            

            #Derecha || Right
            Game.cord[2] = Game.cord[0]+ 1
            Game.cord[3] = Game.cord[1]

            if(Game.cord[2]<matrix.shape[1] and not((Game.cord[2],Game.cord[3]) in nodo.nodos_visitados) and nodo.matriz[Game.cord[1],Game.cord[0]]!=1):
                nodos_visitados = nodo.nodos_visitados.copy()
                nodos_visitados.append((Game.cord[2],Game.cord[3]))
                recorrido = nodo.recorrido.copy()
                recorrido.append((Game.cord[2],Game.cord[3]))
                estado = nodo.estado.copy()

                son = Nodo(
                    nodo.matriz,
                    (Game.cord[2],Game.cord[3]),
                    estado,
                    recorrido,
                    nodos_visitados
                )
                nodes_created+=1
                son.marcar()
                if not(son.validar_perder()):
                    cola.append(son)
        return "No hay Solucion",nodes_created,expanded_nodes