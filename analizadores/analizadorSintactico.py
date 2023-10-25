from errores import *
from instrucciones.declaracionClaves import *
from instrucciones.declaracionRegistros import *
from instrucciones.elementosRegistros import *
from instrucciones.imprimir import *
from instrucciones.imprimirln import *
global n_linea
global n_columna
global lista_lexemas_sintacticos
global instrucciones_sintacticas
lista_errores = []


def instrucciones_sintactico(lista_lexemas):

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        print(lexema.operar(None))


        if lexema.operar(None) == 'Claves':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            print(igual.operar(None))
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        print(lex.operar(None))
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == ']':
                            print(lista_elementos)
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
            else: #! para detectar errores sintácticos
                print("Error sintáctico en la declaración de claves")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de claves")
                        break

        if lexema.operar(None) == 'imprimir':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'imprimirln':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimirln(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'Registros':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == "{":
                            continue
                        elif lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == '}':
                            print(lista_elementos)
                            return ElementosRegistros(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        elif lex.operar(None) == "]":
                            break
                        else:
                            lista_elementos.append(lex.lexema)
                            #if lex.operar(None) == ']':
            else: #! para detectar errores sintácticos
                print("Error sintáctico en la declaración de claves")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de claves")
                        break