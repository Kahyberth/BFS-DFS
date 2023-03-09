class Nodo:

    def __init__(self,matriz,posR,estado,recorrido,nodos_visitados):
        self.matriz = matriz
        self.posR = posR
        self.estado = estado
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados

    #Funciones del Nodo
    def condicionGanadora(self):
        return self.estado[0] and self.estado[1] and self.estado[2]

    def marcar(self):
    #Condicion que evalua el desecho de 2KG
        if self.matriz[self.posR[1],self.posR[0]]==2 and not (self.estado[0]):
            self.estado[0] = True #Si se encuentra retorna TRUE
            self.nodos_visitados = [] #Permite devolverse

        if self.estado[0] and self.matriz[self.posR[1],self.posR[0]]==3 and not (self.estado[1]):
            self.estado[1] = True #Si se encuentra retorna TRUE
            self.nodos_visitados = [] #Permite devolverse

    #Condicion que evalua el punto de reciclaje
        if self.estado[1] and self.matriz[self.posR[1],self.posR[0]] == 5:
            self.estado[2] = True #Se encuentra el punto de reciclaje
        
    def validar_perder(self):
        x,y = self.posR[1],self.posR[0]
        return self.matriz[x,y]==1 #Pierde si se topa con un muro
    