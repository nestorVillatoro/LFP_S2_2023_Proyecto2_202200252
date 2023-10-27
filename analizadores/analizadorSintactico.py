from errores import *
from instrucciones.declaracionClaves import *
from instrucciones.declaracionRegistros import *
from instrucciones.elementosRegistros import *
from instrucciones.imprimir import *
from instrucciones.promedio import *
from instrucciones.sumar import *
from instrucciones.max import *
from instrucciones.min import *
from instrucciones.exportarReportes import *
from instrucciones.contarsi import *
from instrucciones.datos import *
from instrucciones.conteo import *
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


        if lexema.operar(None).startswith('Claves'):
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
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
                            
        if lexema.operar(None) == 'promedio':
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
                                return Promedio(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'max':
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
                                return Max(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'min':
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
                                return Min(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'exportarReporte':
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
                                return ExportarReporte(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'sumar':
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
                                return Sumar(texto.lexema, lexema.getFila(), lexema.getColumna())
                            
        if lexema.operar(None) == 'datos':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Datos(True, lexema.getFila(), lexema.getColumna())
                            
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
                            
        if lexema.operar(None).startswith('Registros'):
            lista_elementos = []
            lista_registros = []
            global contador
            contador = 0
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
                            var = ElementosRegistros(lista_elementos, lex.getFila(), lex.getColumna()) 
                            lista_elementos = []
                            lista_registros.append(var)
                            contador += 1
                        elif lex.operar(None) == "]":
                            return DeclaracionRegistros(contador, palabra_reservada.lexema, lista_registros, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
                            #if lex.operar(None) == ']':
            else: #! para detectar errores sintácticos
                print("Error sintáctico en la declaración de Registros")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de Registros")
                        break

        if lexema.operar(None) == 'conteo':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Conteo(contador, lexema.getFila(), lexema.getColumna())
        
        if lexema.operar(None) == 'contarsi':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        coma = lista_lexemas.pop(0)
                        if coma.operar(None) == ",":
                            numero = lista_lexemas.pop(0)
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.operar(None) == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.operar(None) == ';':
                                    return Contarsi(texto.lexema, numero.lexema, lexema.getFila(), lexema.getColumna())
                
                        