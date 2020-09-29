# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:09:32 2020

@author: Rony

"""

class StackEmpty (Exception):
    def __init__(self):
        pass
class StackFull (Exception):
    def __init__(self):
        pass

class Queue:
    def __init__(self):
        self.reset()

    def reset(self):
        self.dnis=[]
        self.nombres=[]
        self.apellidos=[]
    def empty(self):
        return len(self.dnis) == 0
    def full(self):
        return False
    def ingresarNombre(self,x):
        self.nombres.append(x)
    def borrarN(self):
        try:
            return self.nombres.pop(0)
        except IndexError:
            raise StackEmpty()
        
    def ingresarApellidos(self,x):
        self.apellidos.append(x)
    def borrarA(self):
        try:
            return self.apellidos.pop(0)
        except IndexError:
            raise StackEmpty()
    def ingresarDNI(self,x):
        try:
            self.dnis.append(x)
        except MemoryError:
            raise StackFull()

    def borrarDNI(self):
        try:
            return self.dnis.pop(0)
        except IndexError:
            raise StackEmpty()

    def mostrarDatos(self):
        try:
            print('los datos en cola son: ', self.dnis, self.nombres, self.apellidos)
        except MemoryError:
            raise StackEmpty()
    def mostarPosicion(self):
        try:
            pos=self.dnis
            print(pos[0])
        except MemoryError:
            raise StackEmpty()
    def datos(self):
        return self.dnis
            
class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)
arbol=arbol()
datos=Queue()
while True:
    evento=input("evento ? ")
    if evento=="ingresar":
        try:
            datos.ingresarNombre(input("Nombre : "))
            datos.ingresarApellidos(input("Apellido : "))
            a=input("DNI:  ")
            nodo=a
            datos.ingresarDNI(a)
            if nodo.isdigit():
                nodo = int(nodo)
                arbol.root = arbol.insert(arbol.root, nodo)
            else:
                print("\nIngresa solo digitos...")
        except StackFull:
            print ('no hay espacio')
    elif evento=="atender":
        try:
            datos.borrarA()
            datos.borrarDNI()
            print ('se atiende a', datos.borrarN())
        except StackEmpty:
            print ('no hay clientes')
    elif evento=="valorar":
        try:
            nombre=input("ingrese su DNI: ")
            d=datos.datos()
            while d.count(nombre):
                opcion=input("Como califica su experiencia ? \n 1 : Bueno \n 2 : Malo \n ----------> ")
                if opcion == "1":
                    print("Su valoracion es: Bueno. \n Gracias por su valoracion positiva")
                    break
                elif opcion == "2":
                    print("Su valoracion es: Malo. \n Gracias por su valoracion")
                    break
                else:
                    print("opcion incorrecta")
        except StackEmpty: 
            print("usted no se encuentra en cola")
    elif evento == "buscar":
         nod = input("\nIngresa el nodo a buscar -> ")
         if nod.isdigit():
             nod = int(nod)
             if arbol.buscar(nod, arbol.root) == None:
                 print("\nNodo no encontrado...")
             else:
                 print("\nNodo encontrado -> ",arbol.buscar(nod, arbol.root), " si existe...")
         else:
             print("\nIngresa solo digitos...") 
    elif evento == "salir":
        break
    else:
        print('evento incorrecto')
        
