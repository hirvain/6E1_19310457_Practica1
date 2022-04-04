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




caballosGanadores = ListaDoblementeEnlazada()
#caballosGanadores.insertar(caballos1.inicio.nombre,caballos1.inicio.vel)
print("----------------------------")


