# Alumno: Gonzalez Magallanes Oliver Uriel
# Seminario de Solución de Problemas de Traductores de Lneguajes II
# Docente: Michel Emanuel Lopez Franco
# Mini Generador Lexico

import re

identificador = re.compile(r"[a-zA-Z]+([a-zA-Z]+[0-9])*")
numreal = re.compile(r"[0-9]+\.[0-9]+")

linea = []

print("----------------------------------------------------------")
while (linea != '0'):
        linea = input("\tIngrese una cadena: ")
        print("----------------------------------------------------------")
        print("\tAnalizando la cadena...\n")
        tokens=linea.split(' ')
        for token in tokens:    
            if identificador.match(linea):
                print("\t",token,"es un identificador del tipo: 0")
            elif numreal.match(linea):
                print("\t",token,"es un numero real del tipo: 2")
            else:
                print("\tSin coincidencias con ningun simbolo")           
            
        print("----------------------------------------------------------")