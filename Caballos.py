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
                
    def iterar(self):
        actual = self.inicio
        
        while actual:
            velocidad = actual.vel
            print(actual.nombre)
            actual = actual.next
            yield velocidad
         
caballos = ListaDoblementeEnlazada()
for x in range(25):
    caballos.insertar(nombres[x])
    
for y in caballos.iterar():
    print(y)