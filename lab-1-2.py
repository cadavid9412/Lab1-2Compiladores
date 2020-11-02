# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:13:25 2020

@author: Sebastian
"""


class Automata:
    def __init__(self,cadena):
        self.cadena=cadena
        
    
    
    def leerArchivo(self):
        with open('prueba.txt', 'r') as f:
            for linea in f:
                linea=f.readline()
                
                
                
                



class listaSimpleLigada:
    nodoSimple=0
    primero=0
    ultimo=0
    
    def __init__(self,primero,ultimo):
        self.primero=0
        self.ultimo=0
        
    def esVacia(self,primero):
        if primero==0:
            return True
        else:
            return False
        
    def primerNodo(self):
        return primero
    
    def ultimoNodo(self):
        return ultimo
    
    def finDeRecorrido(self,nodoSimple ):
        if nodoSimple=="null":
            return True
        else: 
            return False
    def recorre (self):
        nodo=nodoSimple(0,0,1,0)
        while finDeRecorrido(nodo)==False:
            print(nodo.retornPosicionMemoria())
            print (nodo.retornaClase(),nodo.retornaValor())
    
    def insertar(self,listaSimpleLigada,nodoSimple):
        nodo=nodoSimple(0,0,ultimo,0)
        conectar(ultimo con nuevo)
    
    def conectar(self,nodoSimple,nodoSimple2):
        nodoSimple.asignaPosicionMemoria(nodoSimple2.retornPosicionMemoria())
        nodoSimple2.asignaPosicionMemoria(ultimo)
        
        
        
        

class nodoSimple:
    clase=0
    valor=0
    posicionMemoria=0
    liga=0
    
    def __init__(self,clase,valor,posicionMemoria,liga):
        self.clase=clase
        self.valor=valor 
        self.posicionMemoria=posicionMemoria
        self.liga=liga
    
    def retornaClase():
        return clase;
    def retornaValor():
        return valor;
    def retornaNodoSimple():
        return nodoSimple;
    def retornPosicionMemoria():
        return posicionMemoria;
    
    def asignaClase(tipo):
        clase=tipo
    def asignaValor(tipo):
        valor=tipo
    def asignaNodoSimple(tipo):
        nodoSimple=tipo
    def asignaPosicionMemoria(tipo):
        posicionMemoria=tipo
    
    
    
    
    
    
    
            
        