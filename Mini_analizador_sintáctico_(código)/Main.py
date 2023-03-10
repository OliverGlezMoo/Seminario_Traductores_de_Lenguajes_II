# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:26:54 2023

@author: Oliver
"""

from operator import is_

from Pila import Stack
import Constantes

def main():
    print("------------------------")
    print("    Primer Ejercicio    ")
    print("------------------------")
    print("         Cadena         ")
    print("------------------------")
    primerEjercicio("hola+mundo$")
    print("------------------------")
    print("    Segundo Ejercicio   ")
    print("------------------------")
    print("         Cadena         ")
    print("------------------------")
    segundoEjercicio("a+b+c+d+e+f$")
    print("------------------------")

def primerEjercicio(texto):
    print(texto)
    pila = Stack()

    estado = Constantes.INICIAL
    d = 2
    lexema = ""

    i = 0
    while(i<len(texto)):
        c = texto[i]
        if(estado == Constantes.INICIAL):
            if (es_Letra(c) or c == '_'): 
                estado = Constantes.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(Constantes.SIMBOLO)
                pila.push(d)
                d+=1
                estado = Constantes.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(Constantes.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")
        elif(estado == Constantes.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = Constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Constantes.IDENTIFICADOR)
                pila.push(d)
                d += 1
                estado = Constantes.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1

def segundoEjercicio(texto):
    print(texto)
    pila = Stack()
    estado = Constantes.INICIAL 
    d2 = 2
    d3 = 3
    lexema = ""
    i = 0
    while(i<len(texto)):
        c = texto[i]
        if(estado == Constantes.INICIAL):
            if (es_Letra(c) or c == '_'): 
                estado = Constantes.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(Constantes.SIMBOLO)
                pila.push(d3)
                estado = Constantes.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(Constantes.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")
        elif(estado == Constantes.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = Constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Constantes.IDENTIFICADOR)
                pila.push(d2)
                estado = Constantes.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1

def isReal(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return True
    else:
        return False

def es_Letra(c):
    if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
        return True
    else:
        return False

main()