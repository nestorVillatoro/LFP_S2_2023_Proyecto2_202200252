import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import filedialog, messagebox
import subprocess
from analizadores.analizadorLexico import *
from analizadores.analizadorSintactico import *
import os

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto 2 - LFP")

        # Barra de números de línea
        self.line_number_bar = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto principal
        self.text_widget = tkst.ScrolledText(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')

        self.text_widget.bind('<Key>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)

        # Consola de salida
        self.output_console = tkst.ScrolledText(self.root, wrap=tk.WORD)
        self.output_console.pack(expand=True, fill='both')
        self.output_console.config(state='disabled')

        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_command(label="Guardar Como", command=self.save_file_as)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        # Botón para analizar
        self.menu_bar.add_command(label="Analizar", command=self.analyze_code)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.menu_bar.add_cascade(label="Reportes", menu=self.file_menu)
        self.file_menu.add_command(label="Reporte de errores", command=self.reporte_de_errores)
        self.file_menu.add_command(label="Reporte de tokens", command=self.reporte_de_tokens)
        self.file_menu.add_command(label="Árbol de derivación", command=self.arbol)

    global verificador 
    verificador= False
    def open_file(self):
        global file_path
        global verificador
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.bizdata")])
        verificador = True
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.data = content
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.update_line_numbers()
        self.data = self.text_widget.get(1.0, tk.END)

    def reporte_de_errores(self):
        texto = ""
        for i in range(len(lista_errores_lexicos)):
            objeto = lista_errores_lexicos[i]
            texto += "<tr>"+"\n"
            texto += "<td>"+str(objeto.lexema)+"</td>"+"\n"
            texto += "<td>"+str(objeto.fila)+"</td>"+"\n"
            texto += "<td>"+str(objeto.columna)+"</td>"+"\n"
            texto += "</tr>"+"\n"

        for i in range(len(lista_errores_sintacticos)):
            objeto = lista_errores_sintacticos[i]
            texto += "<tr>"+"\n"
            texto += "<td>"+str(objeto.lexema)+"</td>"+"\n"
            texto += "<td>"+str(objeto.fila)+"</td>"+"\n"
            texto += "<td>"+str(objeto.columna)+"</td>"+"\n"
            texto += "</tr>"+"\n"

        archivo = open('reporteDeErrores.html', 'w+')
        archivo.write('''
<html lang="es" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Reporte de errores</title>
        <meta name="viwport" content="width=divice-width, initial-scale=1">
    </head>

    <body>
    <header>
        <h1>Reporte de errores</h1>
    </header>
            ''') 
        archivo.write('''
        <table border = "1">
            <tr>
                <th>Token</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>'''
            +texto+'''
        </table>
        <footer>
            <address>
                <br>Pagina creada por Nestor Enrique Villatoro Avendaño - 202200252<br/>
                Para el proyecto 2 del laboratorio de lenguajes formales y de programacion
            </address>
        </footer>
    </body>
</html>
                                  ''')

        archivo.close()
        print("Archivo generado como reporteDeErrores.html")
        messagebox.showinfo("Análisis exitoso", "Archivo generado exitosamente.")

    def reporte_de_tokens(self):
        texto = ""
        for i in range(len(lista_lexemas_reporte)):
            objeto = lista_lexemas_reporte[i]
            texto += "<tr>"+"\n"
            texto += "<td>"+str(objeto.tipo)+"</td>"+"\n"
            texto += "<td>"+str(objeto.lexema)+"</td>"+"\n"
            texto += "<td>"+str(objeto.fila)+"</td>"+"\n"
            texto += "<td>"+str(objeto.columna)+"</td>"+"\n"
            texto += "</tr>"+"\n"

        
        archivo = open('reporteDeTokens.html', 'w+')
        archivo.write('''
<html lang="es" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Reporte de tokens</title>
        <meta name="viwport" content="width=divice-width, initial-scale=1">
    </head>

    <body>
    <header>
        <h1>Reporte de tokens</h1>
    </header>
            ''') 
        archivo.write('''
        <table border = "1">
            <tr>
                <th>Tipo</th>
                <th>Lexema</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>'''
            +texto+'''
        </table>
        <footer>
            <address>
                <br>Pagina creada por Nestor Enrique Villatoro Avendaño - 202200252<br/>
                Para el proyecto 2 del laboratorio de lenguajes formales y de programacion
            </address>
        </footer>
    </body>
</html>
                                  ''')

        archivo.close()
        print("Archivo generado como reporteDeTokens.html")
        messagebox.showinfo("Análisis exitoso", "Archivo generado exitosamente.")

    def arbol(self):
        contador = 0
        text = ""
        text += f"\tarbol" + "[" + f"style = filled" + f",fillcolor = gray" + f",fontcolor = black" + "]\n"
        text += f"\tarbol" + f"[label = \"Árbol de derivación" + "\"]\n"
        for i in range(len(lista_arbol)):
            text += f"\ttipo{i}" + "[" + f"style = filled" + f",fillcolor = crimson" + f",fontcolor = black" + "]\n"
            text += f"\ttipo{i}" + f"[label = \"{str(lista_arbol[i].pop(0))}" + "\"]\n"
            text += f"\tarbol -> tipo{i}\n"
            for j in range(len(lista_arbol[i])):
                contador+= 1
                objeto = lista_arbol[i][j]
                text += f"\telemento{contador}" + "[" + f"style = filled" + f",fillcolor = crimson" + f",fontcolor = black" + "]\n"
                text += f"\telemento{contador}" + f"[label = \"{str(objeto)}" + "\"]\n"
                text += f"\ttipo{i} -> elemento{contador}\n"


        r = open("arbol.dot", "w", encoding="utf-8")
        r.write("digraph G {\n\n")
        r.write(text)
        r.write("}")
        r.close()
        os.system("cmd /c dot -Tsvg arbol.dot > arbol.svg")
    
    def save_file(self):
        if verificador == True:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w+') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
        else:
            file_path2 = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.bizdata")])
            if file_path2:
                content = self.text_widget.get(1.0, tk.END)
                with open(file_path2, 'w') as file:
                    file.write(content)
                messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def save_file_as(self):
        file_path2 = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.bizdata")])
        if file_path2:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path2, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def update_line_numbers(self, event=None):
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count

    def analyze_code(self):
        # Obtén el código del área de texto
        code = self.text_widget.get(1.0, tk.END)
        imprimir_consola = ''
        datos = ''
        try:
            # Ejecuta el análisis léxico
            instrucciones_lexico = instruccion(code)
            lista_instrucciones = []
            while True:
                instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
                if instrucciones_lenguaje:
                    lista_instrucciones.append(instrucciones_lenguaje)
                else:
                    break

            #! Ejecutar instrucciones

            for elemento in lista_instrucciones:
                if isinstance(elemento, DeclaracionClaves):
                    lista = elemento.ejecutarT()
                    for i in range(len(lista)):
                        datos += lista[i] + " "
                    datos += "\n"
                    continue

                elif isinstance(elemento, Imprimir):
                    imprimir_consola += elemento.ejecutarT()

                elif isinstance(elemento, Imprimirln):
                    imprimir_consola += elemento.ejecutarT()

                elif isinstance(elemento, Conteo):
                    imprimir_consola += str(elemento.ejecutarT()) + "\n"

                elif isinstance(elemento, Promedio):
                    x = 0
                    palabrap = str(elemento.ejecutarT())
                    for i in range(len(lista)):
                        if palabrap == lista[i]:
                            print("Elemento encontrado")
                            for j in range(len(lista2)):
                                lista3 = lista2[j].ejecutarT()
                                x += lista3[i]
                            promedio = (x/len(lista2))
                            imprimir_consola += str(promedio) + "\n"

                elif isinstance(elemento, Sumar):
                    suma = 0
                    palabras = str(elemento.ejecutarT())
                    for i in range(len(lista)):
                        if palabras == lista[i]:
                            print("Elemento encontrado")
                            for j in range(len(lista2)):
                                lista3 = lista2[j].ejecutarT()
                                suma += lista3[i]
                            imprimir_consola += str(suma) + "\n"

                elif isinstance(elemento, Max):
                    lista4 = []
                    palabram = str(elemento.ejecutarT())
                    for i in range(len(lista)):
                        if palabram == lista[i]:
                            print("Elemento encontrado")
                            for j in range(len(lista2)):
                                lista3 = lista2[j].ejecutarT()
                                lista4.append(lista3[i])
                            
                            imprimir_consola += str(max(lista4)) + "\n"

                elif isinstance(elemento, Min):
                    lista5 = []
                    palabram = str(elemento.ejecutarT())
                    for i in range(len(lista)):
                        if palabram == lista[i]:
                            print("Elemento encontrado")
                            for j in range(len(lista2)):
                                lista3 = lista2[j].ejecutarT()
                                lista5.append(lista3[i])
                            
                            imprimir_consola += str(min(lista4)) + "\n"

                elif isinstance(elemento, ExportarReporte):
                    palabrae = str(elemento.ejecutarT())
                    texto = ""
                    texto2 = ""

                    for aux in range(len(lista)):
                        texto += "<th>"+str(lista[aux])+"</th>" + "\n"
                    
                    for aux2 in range(cant):
                        texto2 += "<tr>" + "\n"
                        lista3 = lista2[aux2].ejecutarT()
                        for aux3 in range(len(lista3)):
                            texto2 += "<td>"+str(lista3[aux3])+"</td>" + "\n"
                        texto2 += "<tr>" + "\n"


                    archivo = open('ExportarReporte.html', 'w+')
                    archivo.write('''
<html lang="es" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Exportar Reporte</title>
        <meta name="viwport" content="width=divice-width, initial-scale=1">
    </head>

    <body>
    <header>
        <h1>Exportar Reporte</h1>
    </header>
            ''')
                    
                    archivo.write('''
        <table border = "1">
            <tr>
                <th colspan="'''+str(len(lista))+'''" scope="rowgroup">'''+str(palabrae)+'''</th>
            </tr>
            ''')
                    
                    archivo.write('''
            <tr>
            '''
                + texto +'''
            </tr>'''
            +texto2+'''
        </table>
        <footer>
            <address>
                <br>Pagina creada por Nestor Enrique Villatoro Avendaño - 202200252<br/>
                Para el proyecto 2 del laboratorio de lenguajes formales y de programacion
            </address>
        </footer>
    </body>
</html>
                                  ''')

                    archivo.close()

                elif isinstance(elemento, Contarsi):
                    contadorsi = 0
                    palabrac = str(elemento.ejecutarT())
                    numc = elemento.ejecutarN()
                    for i in range(len(lista)):
                        if palabrac == lista[i]:
                            print("Elemento encontrado")
                            for j in range(len(lista2)):
                                lista3 = lista2[j].ejecutarT()
                                if lista3[i] == numc:
                                    contadorsi += 1
                            imprimir_consola += str(contadorsi) + "\n"
                    
                elif isinstance(elemento, DeclaracionRegistros):  
                    lista2 = elemento.ejecutarT()
                    cant = elemento.obtenerCant()
                    for i in range(len(lista2)):
                        lista3 = lista2[i].ejecutarT()
                        for j in range(len(lista3)):
                            datos += str(lista3[j]) + " "
                        datos += "\n"
                    continue

                elif isinstance(elemento, Datos): 
                    booleano = elemento.ejecutarT()
                    if booleano == True:
                        imprimir_consola += datos

            print(imprimir_consola)
            for error in lista_errores:
                print(error.operar(None))

                    # Muestra el resultado en la consola de salida
            self.output_console.config(state='normal')
            self.output_console.delete(1.0, tk.END)
            self.output_console.insert(tk.END, imprimir_consola)
            self.output_console.config(state='disabled')
            messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")

        except Exception as e:
            messagebox.showerror(f"Ocurrió un error al analizar el código: {str(e)}")
            print("Ocurrió un error al analizar el código: ", e)



    def run_analysis(self, code):
        # Aquí puedes realizar el análisis del código, por ejemplo, usando subprocess
        try:
            # Ejemplo: Ejecutar un comando de consola y capturar la salida
            result = subprocess.check_output(["python", "-c", code], universal_newlines=True, stderr=subprocess.STDOUT)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()