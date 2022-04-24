# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 01:17:04 2022

@author: Oscar Antonio García Avila  19310457  6E1
"""
import random
import numpy as np
import cv2
 

nombres = ['Tormenta China','Paco','Perez','Tony','Soprano','Michael','Dwight','Barry','Pollo','Vito','Boba','Falcone','Paul','George','Ringo','John','Max','Elton','Grogu','Chewie','R2','Alfred','Tim','Tulio','Spencer']

class Nodo:
    def __init__(self, dato):
        self.nombre = dato
        self.vel = random.randint(1, 10)
        self.next = None
        self.ant = None
        
        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.contador = 0
        
    def insertar(self, dato):
        nodo = Nodo(dato)
        
        if self.inicio is None:
            self.inicio = nodo
            self.fin = self.inicio
        else:
            nodo.ant = self.fin
            self.fin.next = nodo
            self.fin = nodo
            
        self.contador += 1
                
    def insertarGanador(self, nombre, vel):
        nodo = Nodo(nombre)
        nodo.vel=vel
        
        if self.inicio is None:
            self.inicio = nodo
            self.fin = self.inicio
        else:
            nodo.ant = self.fin
            self.fin.next = nodo
            self.fin = nodo
            
        self.contador += 1
        
    def mostrar(self):
        actual = self.inicio
        for y in range(5):
            print(actual.vel, actual.nombre)
            actual = actual.next
    
    def mostrarTodos(self):
        actual = self.inicio
        for y in range(36):
            print(actual.vel, actual.nombre)
            actual = actual.next

    def carreras1a5(self):
        actual = self.inicio
        #final=actual.next.next.next.next.next.nombre
        #siguienta=actual.next.next.next.next.next.next
        intercambio = True
        
        while intercambio:
            intercambio= False
            actual=self.inicio
            for i in range(4):
                #print(actual.vel,",",actual.next.vel)
                #self.mostrar()
                if actual.vel < actual.next.vel:
                    if(self.inicio==actual):
                        self.inicio=self.inicio.next
                        actual.next=self.inicio.next
                        actual.ant=self.inicio
                        self.inicio.ant=None
                        self.inicio.next.ant=actual
                        self.inicio.next=actual
                        intercambio=True

                        
                    elif(actual.next==self.fin):
                        self.fin.next=actual
                        self.fin.ant=actual.ant
                        actual.ant.next=self.fin
                        actual.ant=self.fin
                        actual.next=None
                        self.fin=actual
                        intercambio=True
                        
                    
                    else:
                        temp=actual.next
                        actual.ant.next=temp
                        temp.ant=actual.ant
                        temp.next.ant=actual
                        actual.next=temp.next
                        temp.next=actual
                        actual.ant=temp
                        intercambio=True
                        
                            
                    
                #print(actual.vel,",")    
                else:
                    actual=actual.next
               #print(actual.vel,"next")   
                
                
carrera1 = ListaDoblementeEnlazada()
carrera2 = ListaDoblementeEnlazada()
carrera3 = ListaDoblementeEnlazada()
carrera4 = ListaDoblementeEnlazada()
carrera5 = ListaDoblementeEnlazada()
for x in range(5):
    carrera1.insertar(nombres[x])
    carrera2.insertar(nombres[x+5])
    carrera3.insertar(nombres[x+10])
    carrera4.insertar(nombres[x+15])
    carrera5.insertar(nombres[x+20])

carrera1.mostrar()
print("------CARRERA 1--------")
carrera1.carreras1a5()
carrera1.mostrar()
print("***********************************************")
carrera2.mostrar()
print("------CARRERA 2--------")
carrera2.carreras1a5()
carrera2.mostrar()
print("***********************************************")
carrera3.mostrar()
print("------CARRERA 3--------")
carrera3.carreras1a5()
carrera3.mostrar()
print("***********************************************")
carrera4.mostrar()
print("------CARRERA 4--------")
carrera4.carreras1a5()
carrera4.mostrar()
print("***********************************************")
carrera5.mostrar()
print("------CARRERA 5--------")
carrera5.carreras1a5()
carrera5.mostrar()

print("////////////////////////////////////////////////")
carrera6 = ListaDoblementeEnlazada()
carrera6.insertarGanador(carrera1.inicio.nombre,carrera1.inicio.vel)
carrera6.insertarGanador(carrera2.inicio.nombre,carrera2.inicio.vel)
carrera6.insertarGanador(carrera3.inicio.nombre,carrera3.inicio.vel)
carrera6.insertarGanador(carrera4.inicio.nombre,carrera4.inicio.vel)
carrera6.insertarGanador(carrera5.inicio.nombre,carrera5.inicio.vel)
carrera6.mostrar()
print("------CARRERA 6--------")
carrera6.carreras1a5()
carrera6.mostrar()
print("----------------------------")

print("////////////////////////////////////////////////")
carrera7 = ListaDoblementeEnlazada()

if(carrera1.inicio.nombre==carrera6.inicio.nombre):
    carrera7.insertarGanador(carrera1.inicio.next.nombre,carrera1.inicio.next.vel)
    carrera7.insertarGanador(carrera1.inicio.next.next.nombre,carrera1.inicio.next.next.vel)
    
if(carrera2.inicio.nombre==carrera6.inicio.nombre):
    carrera7.insertarGanador(carrera2.inicio.next.nombre,carrera2.inicio.next.vel)
    carrera7.insertarGanador(carrera2.inicio.next.next.nombre,carrera2.inicio.next.next.vel)

if(carrera3.inicio.nombre==carrera6.inicio.nombre):
    carrera7.insertarGanador(carrera3.inicio.next.nombre,carrera3.inicio.next.vel)
    carrera7.insertarGanador(carrera3.inicio.next.next.nombre,carrera3.inicio.next.next.vel)
    
if(carrera4.inicio.nombre==carrera6.inicio.nombre):
    carrera7.insertarGanador(carrera4.inicio.next.nombre,carrera4.inicio.next.vel)
    carrera7.insertarGanador(carrera4.inicio.next.next.nombre,carrera4.inicio.next.next.vel)
    
if(carrera5.inicio.nombre==carrera6.inicio.nombre):
    carrera7.insertarGanador(carrera5.inicio.next.nombre,carrera5.inicio.next.vel)
    carrera7.insertarGanador(carrera5.inicio.next.next.nombre,carrera5.inicio.next.next.vel)



carrera7.insertarGanador(carrera6.inicio.next.nombre,carrera6.inicio.next.vel)

if(carrera1.inicio.nombre==carrera6.inicio.next.nombre):
    carrera7.insertarGanador(carrera1.inicio.next.nombre,carrera1.inicio.next.vel)
    
if(carrera2.inicio.nombre==carrera6.inicio.next.nombre):
    carrera7.insertarGanador(carrera2.inicio.next.nombre,carrera2.inicio.next.vel)

if(carrera3.inicio.nombre==carrera6.inicio.next.nombre):
    carrera7.insertarGanador(carrera3.inicio.next.nombre,carrera3.inicio.next.vel)
    
if(carrera4.inicio.nombre==carrera6.inicio.next.nombre):
    carrera7.insertarGanador(carrera4.inicio.next.nombre,carrera4.inicio.next.vel)
    
if(carrera5.inicio.nombre==carrera6.inicio.next.nombre):
    carrera7.insertarGanador(carrera5.inicio.next.nombre,carrera5.inicio.next.vel)


carrera7.insertarGanador(carrera6.inicio.next.next.nombre,carrera6.inicio.next.next.vel)

carrera7.mostrar()
print("------CARRERA 7--------")
carrera7.carreras1a5()
carrera7.mostrar()
print("----------------------------")


listaProceso = ListaDoblementeEnlazada()

listaProceso.insertarGanador(carrera6.inicio.nombre,carrera6.inicio.vel)

actual = carrera7.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera6.inicio
actual = actual.next.next.next
for x in range(2):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

actual = carrera5.inicio
actual = actual.next
for x in range(4):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera4.inicio
actual = actual.next
for x in range(4):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera3.inicio
actual = actual.next
for x in range(4):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

actual = carrera2.inicio
actual = actual.next
for x in range(4):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera1.inicio
actual = actual.next
for x in range(4):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

#listaProceso.mostrarTodos()

# Crea una imagen en negro
img = np.zeros((800,1200,3), np.uint8)

# Dibuja una línea vertical
img = cv2.line(img,(500,50),(500,750),(255,0,255),5)


cv2.putText(img,'Nodo Raiz',(250,100), 0, 0.5,(0,255,0),2,cv2.LINE_AA)
cv2.putText(img,'Nodos Internos',(250,180), 0, 0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,'Nodo Frontera, Nodo Hoja',(250,260), 0, 0.5,(0,255,246),2,cv2.LINE_AA)
cv2.putText(img,'------Caballo mas rapido',(600,45), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.putText(img,'------2do Caballo mas rapido',(600,75), 0, 0.5,(255,255,180),2,cv2.LINE_AA)


cv2.putText(img,'CARRERA 1',(800,740), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,660),(890,770),(0,255,0),1)

cv2.putText(img,'CARRERA 2',(800,630), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,650),(890,540),(0,255,0),1)

cv2.putText(img,'CARRERA 3',(800,520), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,530),(890,420),(0,255,0),1)

cv2.putText(img,'CARRERA 4',(800,400), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,410),(890,300),(0,255,0),1)

cv2.putText(img,'CARRERA 5',(800,280), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,290),(890,180),(0,255,0),1)

cv2.putText(img,'CARRERA 6',(800,160), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,170),(890,115),(0,255,0),1)

cv2.putText(img,'CARRERA 7',(800,100), 0, 0.5,(255,255,180),2,cv2.LINE_AA)
cv2.rectangle(img,(480,110),(890,55),(0,255,0),1)

for i in range(25):
    img = cv2.circle(img,(500,40+30*i), 11, (255,255,255), -1)  

img = cv2.circle(img,(500,40), 11, (0,255,0), -1)  
img = cv2.circle(img,(500,760), 11, (0,255,246), -1)  

actual = listaProceso.inicio
for i in range(25):
    cv2.putText(img,str(actual.vel),(492,45+30*i), 0, 0.5,(255,0,0),2,cv2.LINE_AA)
    cv2.putText(img,actual.nombre,(520,45+30*i), 0, 0.6,(255,255,0),2,cv2.LINE_AA)
    actual=actual.next

# Mostrar la imagen
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()