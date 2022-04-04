# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 01:17:04 2022

@author: @author: Oscar Antonio García Avila  19310457  6E1
"""
import random

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
print("----------------------------")
carrera1.carreras1a5()
carrera1.mostrar()
print("***********************************************")
carrera2.mostrar()
print("----------------------------")
carrera2.carreras1a5()
carrera2.mostrar()
print("***********************************************")
carrera3.mostrar()
print("----------------------------")
carrera3.carreras1a5()
carrera3.mostrar()
print("***********************************************")
carrera4.mostrar()
print("----------------------------")
carrera4.carreras1a5()
carrera4.mostrar()
print("***********************************************")
carrera5.mostrar()
print("----------------------------")
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
print("----------------------------")
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
print("----------------------------")
carrera7.carreras1a5()
carrera7.mostrar()
print("----------------------------")
print("----------------------------")

listaProceso = ListaDoblementeEnlazada()

listaProceso.insertarGanador(carrera6.inicio.nombre,carrera6.inicio.vel)

actual = carrera7.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

actual = carrera6.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

actual = carrera5.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera4.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera3.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

actual = carrera2.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next
    
actual = carrera1.inicio
for x in range(5):
    listaProceso.insertarGanador(actual.nombre,actual.vel)
    actual = actual.next

listaProceso.mostrarTodos()