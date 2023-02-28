# Alumno: Gonzalez Magallanes Oliver Uriel
# Seminario de Solución de Problemas de Traductores de Lneguajes II
# Docente: Michel Emanuel Lopez Franco
# Analizador Lexico

import re

identificador = re.compile(r"[a-zA-Z]+([a-zA-Z]+[0-9])*")
entero = re.compile(r"[0-9]+")
real = re.compile(r"[0-9]+\.[0-9]+")
cadena = re.compile(r"[a-zA-Z]+[a-zA-Z]+")

tipo = {'int' : 'de tipo 4', 'float' : 'de tipo 4', 'void': 'de tipo 4'}
tipo_key = tipo.keys()

operadores = {'+' : 'OpSuma de tipo: 5',       '-' : 'OpSuma de tipo: 5',
              '*' : 'OpMul de tipo: 6',        '/' : 'OpMul de tipo: 6',
              '<' : 'OpRelac de tipo: 7',      '<=': 'OpRelac de tipo: 7',
              '>' : 'OpRelac de tipo: 7',      '>=': 'OpRelac de tipo: 7',
              '||': 'OpOr de tipo: 8',
              '&&': 'OpAnd de tipo: 9',
              '!' : 'OpNot de tipo: 10',
              '==': 'OpIgualdad de tipo: 11',  '!=': 'OpIgualdad de tipo: 11'}
operadores_key = operadores.keys()

simbolos = {';' : 'de tipo 12',
            ',' : 'de tipo 13',
            '(' : 'de tipo 14',
            ')' : 'de tipo 15',
            '{' : 'de tipo 16',
            '}' : 'de tipo 17',
            '=' : 'de tipo 18' }
simbolos_key = simbolos.keys()

reservadas = {'if' : 'de tipo 19',
              'while' : 'de tipo 20',
              'return' : 'de tipo 21', 
              'else' : 'de tipo 22',
              }
reservadas_key = reservadas.keys()

especial = {'$': 'de tipo 23'}
especial_key = especial.keys()

linea = []

print("----------------------------------------------------------")
while (linea != '0'):
        linea = input("\tIngrese una cadena: ")
        print("----------------------------------------------------------")
        print("\tAnalizando la cadena...\n")
        tokens=linea.split(' ')
        for token in tokens:
            if token in especial_key:
                print("\t",token,"Es un caracter especial",especial[token])
            elif token in reservadas_key:
                print("\t",token,"Es una palabra reservada",reservadas[token])
            elif token in simbolos_key:
                print("\t",token,"Es un simbolo",simbolos[token])
            elif token in operadores_key:
                print("\t",token,"Es un",operadores[token])
            elif token in tipo_key:
                print("\t",token,"Es un dato",tipo[token])
            elif cadena.match(linea):
                print("\t",token,"es una cadena de tipo: 3") 
            elif real.match(linea):
                print("\t",token, "es un real de tipo: 2")
            elif entero.match(linea):
                print("\t",token, "es un entero de tipo: 1")
            elif identificador.match(linea):
                print("\t",token, "es un identificador de tipo: 0")
            else:
                print("Sin coincidencias")           
            
        print("----------------------------------------------------------")