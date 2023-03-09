import pygame
import tkinter as tk
from tkinter import PhotoImage, Tk,Button,filedialog,Label
from turtle import back
from Game import Game


class Gui:
        
    #Ventana
    window = Tk()
    window.geometry('1024x650')
    window.title('DUSCAT')    
    
   
    #Funciones
    def cargar():
        file = filedialog.askopenfilename(title="Open file")
        Game.cargarArchivo(file)

    def dfs():
        print(Game.dfs(Game.lst))
    
    def bfs():
        print(Game.bfs(Game.lst))
        
    #Botones
    cargarButton = Button(window,text="Buscar Archivo",bg="red",command=cargar)
    cargarButton.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.10)

    buttondfs = Button(window,text="Recorrido DFS",bg="red",command=dfs)
    buttondfs.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.10)
    
    buttonbfs = Button(window,text="Recorrido BFS",bg="red",command=bfs)
    buttonbfs.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.10)

    #Duscat
    imagen = PhotoImage(file="./img/duscat.png")
    img = Label(image = imagen,text ='Duscat Background')
    img.place(relx=0.6,rely=0.1,relwidth= 0.3,relheight= 0.8)

    #Esto hace que se reproduzca automáticamente la cancion
    pygame.mixer.init()

    pygame.mixer.music.load("./music/Pix - Space travel.mp3")
    pygame.mixer.music.play(loops=0)

    #Representa el boton para detener la musica
    def stop():
        pygame.mixer.music.stop()
    stopM = Button(window,text="Stop",bg="red",command=stop)
    stopM.place(relx=0.1,rely=0.8,relwidth=0.08,relheight=0.06)
    window.configure(bg="black")    

    window.mainloop()
    