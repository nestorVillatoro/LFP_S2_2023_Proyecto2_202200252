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
lista_errores_sintacticos = []
lista_arbol = []

def instrucciones_sintactico(lista_lexemas):

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        print(lexema.operar(None))


        if lexema.operar(None).startswith('Claves'):
            lista_elementos = []
            lista_claves = []
            lista_claves.append(lexema.operar(None))
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                lista_claves.append(igual.operar(None))
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    lista_claves.append(corchete_izq.operar(None))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            lista_claves.append("'")
                            continue
                        elif lex.operar(None) == ',':
                            lista_claves.append(lex.operar(None))
                            continue
                        elif lex.operar(None) == ']':
                            lista_claves.append(lex.operar(None))
                            print(lista_elementos)
                            lista_arbol.append(lista_claves)
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                            
                        else:
                            lista_elementos.append(lex.lexema)
                            lista_claves.append(lex.lexema)
                else: 
                    print("Error sintáctico en la declaración de claves")
                    lista_errores.append(Errores(corchete_izq.lexema,"Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ']':
                            print("Final de la declaración de claves")
                            break
            else: 
                print("Error sintáctico en la declaración de claves")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de claves")
                        break

        if lexema.operar(None) == 'imprimir':
            lista_imprimir = []
            lista_imprimir.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                lista_imprimir.append(lexema.operar(None))
                if comillas.operar(None) == '"':
                    lista_imprimir.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_imprimir.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_imprimir.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_imprimir.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_imprimir.append(punto_coma.operar(None))
                                lista_arbol.append(lista_imprimir)
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en imprimir")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                
                        else: 
                            print("Error sintáctico en imprimir")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                            
                    else: 
                        print("Error sintáctico en imprimir")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                        
                else: 
                    print("Error sintáctico en imprimir")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
                    
            else: 
                print("Error sintáctico en imprimir")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                                  
        if lexema.operar(None) == 'promedio':
            lista_promedio = []
            lista_promedio.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_promedio.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_promedio.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_promedio.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_promedio.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_promedio.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_promedio.append(punto_coma.operar(None))
                                lista_arbol.append(lista_promedio)
                                return Promedio(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en promedio")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en promedio")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break    
                    else: 
                        print("Error sintáctico en promedio")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en promedio")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en promedio")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == "'''":
            texto = lista_lexemas.pop(0)
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == "'''":
                pass
                            
        if lexema.operar(None) == 'max':
            lista_max = []
            lista_max.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_max.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_max.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_max.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_max.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_max.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_max.append(punto_coma.operar(None))
                                lista_arbol.append(lista_max)
                                return Max(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en max")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en max")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: 
                        print("Error sintáctico en max")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en max")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en max")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == 'min':
            lista_min = []
            lista_min.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_min.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_min.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_min.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_min.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_min.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_min.append(punto_coma.operar(None))
                                lista_arbol.append(lista_min)
                                return Min(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en min")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en min")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: 
                        print("Error sintáctico en min")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en min")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en min")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == 'exportarReporte':
            lista_reporte = []
            lista_reporte.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_reporte.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_reporte.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_reporte.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_reporte.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_reporte.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_reporte.append(punto_coma.operar(None))
                                lista_arbol.append(lista_reporte)
                                return ExportarReporte(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en exportarReporte")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en exportarReporte")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: 
                        print("Error sintáctico en exportarReporte")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en exportarReporte")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en exportarReporte")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == 'sumar':
            lista_sumar = []
            lista_sumar.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_sumar.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_sumar.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_sumar.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_sumar.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_sumar.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_sumar.append(punto_coma.operar(None))
                                lista_arbol.append(lista_sumar)
                                return Sumar(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en sumar")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en sumar")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: 
                        print("Error sintáctico en sumar")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en sumar")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en sumar")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == 'datos':
            lista_datos = []
            lista_datos.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_datos.append(lexema.operar(None))
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    lista_datos.append(parentesis.operar(None))
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        lista_datos.append(punto_coma.operar(None))
                        lista_arbol.append(lista_datos)
                        return Datos(True, lexema.getFila(), lexema.getColumna())
                    else: 
                        print("Error sintáctico en datos")
                        lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                else: 
                    print("Error sintáctico en datos")
                    lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en datos")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None) == 'imprimirln':
            lista_imprimirln = []
            lista_imprimirln.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_imprimirln.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_imprimirln.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_imprimirln.append("'")
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            lista_imprimirln.append(parentesis.operar(None))
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                lista_imprimirln.append(punto_coma.operar(None))
                                return Imprimirln(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: 
                                print("Error sintáctico en imprimirln")
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        else: 
                            print("Error sintáctico en imprimirln")
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                            
                    else: 
                        print("Error sintáctico en imprimirln")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                        
                else: 
                    print("Error sintáctico en imprimirln")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en imprimirln")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        if lexema.operar(None).startswith('Registros'):
            lista_elementos = []
            lista_registros = []
            lista_ayuda = []
            lista_ayuda.append(lexema.operar(None))
            global contador
            contador = 0
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                lista_ayuda.append(igual.operar(None))
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    lista_ayuda.append(corchete_izq.operar(None))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)               
                        if lex.operar(None) == "{":
                            lista_ayuda.append(lex.operar(None))
                            continue
                        elif lex.operar(None) == '"':
                            lista_ayuda.append("'")
                            continue
                        elif lex.operar(None) == ',':
                            lista_ayuda.append(lex.operar(None))
                            continue
                        elif lex.operar(None) == '}':
                            lista_ayuda.append(lex.operar(None))
                            print(lista_elementos) 
                            var = ElementosRegistros(lista_elementos, lex.getFila(), lex.getColumna()) 
                            lista_elementos = []
                            lista_registros.append(var)
                            contador += 1
                        elif lex.operar(None) == "]":
                            lista_ayuda.append(lex.operar(None))
                            lista_arbol.append(lista_ayuda)
                            return DeclaracionRegistros(contador, palabra_reservada.lexema, lista_registros, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
                            lista_ayuda.append(lex.lexema)
                else: 
                    print("Error sintáctico en la declaración de Registros")
                    lista_errores.append(Errores(corchete_izq.lexema,"Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ']':
                            print("Final de la declaración de Registros")
                            break
            else: 
                print("Error sintáctico en la declaración de Registros")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de Registros")
                        break

        if lexema.operar(None) == 'conteo':
            lista_conteo = []
            lista_conteo.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_conteo.append(lexema.operar(None))
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    lista_conteo.append(parentesis.operar(None))
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        lista_conteo.append(punto_coma.operar(None))
                        lista_arbol.append(lista_conteo)
                        return Conteo(contador, lexema.getFila(), lexema.getColumna())
                    else: 
                        print("Error sintáctico en conteo")
                        lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                else: 
                    print("Error sintáctico en conteo")
                    lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en conteo")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        if lexema.operar(None) == 'contarsi':
            lista_contarsi = []
            lista_contarsi.append(lexema.operar(None))
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lista_contarsi.append(lexema.operar(None))
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    lista_contarsi.append("'")
                    texto = lista_lexemas.pop(0)
                    lista_contarsi.append(texto.lexema)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        lista_contarsi.append("'")
                        coma = lista_lexemas.pop(0)
                        if coma.operar(None) == ",":
                            lista_contarsi.append(coma.operar(None))
                            numero = lista_lexemas.pop(0)
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.operar(None) == ')':
                                lista_contarsi.append(parentesis.operar(None))
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.operar(None) == ';':
                                    lista_contarsi.append(punto_coma.operar(None))
                                    lista_arbol.append(lista_contarsi)
                                    return Contarsi(texto.lexema, numero.lexema, lexema.getFila(), lexema.getColumna())
                                else: 
                                    print("Error sintáctico en contarsi")
                                    lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                            else: 
                                print("Error sintáctico en contarsi")
                                lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                                while lista_lexemas:
                                    lex = lista_lexemas.pop(0)
                                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                    if lex.operar(None) == ';':
                                        break
                        else: 
                            print("Error sintáctico en contarsi")
                            lista_errores.append(Errores(coma.lexema,"Sintáctico", coma.getFila(), coma.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: 
                        print("Error sintáctico en contarsi")
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: 
                    print("Error sintáctico en contarsi")
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: 
                print("Error sintáctico en contarsi")
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                
    for i in range(len(lista_errores)):
        lista_errores_sintacticos.append(lista_errores[i])