# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:27:56 2023

@author: Oliver
"""

import Constantes
class Stack:
    items = []
    def __init__(self):
        self.items = []
        self.push(Constantes.SIGNOPESOS)
        self.push(Constantes.IDENTIFICADOR)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def mostrarPila(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print()