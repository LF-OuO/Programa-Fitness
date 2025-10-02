import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class CalorieCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Calorías")
        self.root.geometry("600x800")
        
        print("🎯 CALCULADORA COMPLETA - SIN COLORES VACÍOS")
        
        # RUTA
        self.imagenes_folder = "imagenes"
        
        # Lista de imágenes
        self.backgrounds = [
            "bienvenida.jpg",
            "genero.jpg", 
            "tipo_cuerpo.jpg",
            "edad.jpg",
            "peso.jpg",
            "altura.jpg",
            "meta.jpg",
            "resultado.jpg"
        ]
        
        # Variables para almacenar datos
        self.genero = tk.StringVar()
        self.tipo_cuerpo = tk.StringVar()
        self.edad = tk.StringVar()
        self.peso = tk.StringVar()
        self.altura = tk.StringVar()
        self.meta = tk.StringVar()
        
        self.current_page = 0
        
        # USAR CANVAS
        self.canvas = tk.Canvas(root, width=600, height=800, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Cargar primera imagen
        self.load_current_image()
    
    def load_current_image(self):
        """Cargar y mostrar la imagen actual"""
        image_name = self.backgrounds[self.current_page]
        image_path = os.path.join(self.imagenes_folder, image_name)
        
        print(f"🖼️ Página {self.current_page}: {image_name}")
        
        if os.path.exists(image_path):
            try:
                # Cargar imagen
                image = Image.open(image_path)
                image = image.resize((600, 800), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                
                # LIMPIAR CANVAS
                self.canvas.delete("all")
                
                # MOSTRAR IMAGEN EN CANVAS
                self.current_photo = photo
                self.canvas.create_image(0, 0, anchor='nw', image=photo)
                
                # AGREGAR ELEMENTOS SEGÚN LA PÁGINA
                if self.current_page == 0:
                    self.add_page_0_elements()
                elif self.current_page == 1:
                    self.add_page_1_elements()
                elif self.current_page == 2:
                    self.add_page_2_elements()
                elif self.current_page == 3:
                    self.add_page_3_elements()
                elif self.current_page == 4:
                    self.add_page_4_elements()
                elif self.current_page == 5:
                    self.add_page_5_elements()
                elif self.current_page == 6:
                    self.add_page_6_elements()
                elif self.current_page == 7:
                    self.add_page_7_elements()
                
            except Exception as e:
                print(f"❌ ERROR: {e}")
        else:
            print("❌ ARCHIVO NO ENCONTRADO")
    
    def create_transparent_button(self, x, y, width, height, command):
        """Crear botón transparente usando Frame"""
        btn_frame = tk.Frame(
            self.root,
            bg='lightgray',  # Color temporal para DEBUG - CAMBIAR A '' CUANDO FUNCIONE
            highlightthickness=0,
            bd=0
        )
        self.canvas.create_window(x, y, window=btn_frame, width=width, height=height)
        
        # Hacer clickeable
        btn_frame.bind("<Button-1>", lambda e: command())
        btn_frame.bind("<Enter>", lambda e: btn_frame.config(cursor="hand2"))
        
        return btn_frame
    
    def add_page_0_elements(self):
        """Página 0 - BIENVENIDA"""
        print("   ➕ Agregando botón página 0")
        self.create_transparent_button(300, 625, 100, 50, self.next_page)
    
    def add_page_1_elements(self):
        """Página 1 - GÉNERO"""
        print("   ➕ Agregando botones página 1")
        # Botón MASCULINO
        self.create_transparent_button(210, 430, 120, 60, 
                                     lambda: self.seleccionar_genero("MASCULINO"))
        
        # Botón FEMENINO
        self.create_transparent_button(390, 430, 120, 60,
                                     lambda: self.seleccionar_genero("FEMENINO"))
    
    def add_page_2_elements(self):
        """Página 2 - TIPO DE CUERPO"""
        print("   ➕ Agregando botones página 2")
        # Botón ECTOMORFO
        self.create_transparent_button(115, 475, 130, 50,
                                     lambda: self.seleccionar_tipo_cuerpo("Ectomorfo"))
        
        # Botón MESOMORFO
        self.create_transparent_button(300, 475, 130, 50,
                                     lambda: self.seleccionar_tipo_cuerpo("Mesomorfo"))
        
        # Botón ENDOMORFO
        self.create_transparent_button(485, 475, 130, 50,
                                     lambda: self.seleccionar_tipo_cuerpo("Endomorfo"))
    
    def add_page_3_elements(self):
        """Página 3 - EDAD"""
        print("   ➕ Agregando elementos página 3")
        # Campo de entrada para edad
        self.entry_edad = tk.Entry(
            self.root,
            textvariable=self.edad,
            font=("Arial", 16),
            bg='white', bd=2, relief='solid', justify='center'
        )
        self.canvas.create_window(300, 370, window=self.entry_edad, width=200, height=40)
        self.entry_edad.focus()
        
        # Botón continuar
        self.create_transparent_button(300, 625, 100, 50, self.validar_edad)
    
    def add_page_4_elements(self):
        """Página 4 - PESO"""
        print("   ➕ Agregando elementos página 4")
        # Campo de entrada para peso
        self.entry_peso = tk.Entry(
            self.root,
            textvariable=self.peso,
            font=("Arial", 16),
            bg='white', bd=2, relief='solid', justify='center'
        )
        self.canvas.create_window(300, 370, window=self.entry_peso, width=200, height=40)
        self.entry_peso.focus()
        
        # Botón continuar
        self.create_transparent_button(300, 625, 100, 50, self.validar_peso)
    
    def add_page_5_elements(self):
        """Página 5 - ALTURA"""
        print("   ➕ Agregando elementos página 5")
        # Campo de entrada para altura
        self.entry_altura = tk.Entry(
            self.root,
            textvariable=self.altura,
            font=("Arial", 16),
            bg='white', bd=2, relief='solid', justify='center'
        )
        self.canvas.create_window(300, 370, window=self.entry_altura, width=200, height=40)
        self.entry_altura.focus()
        
        # Botón continuar
        self.create_transparent_button(300, 625, 100, 50, self.validar_altura)
    
    def add_page_6_elements(self):
        """Página 6 - META"""
        print("   ➕ Agregando botones página 6")
        # Botón BAJAR DE PESO
        self.create_transparent_button(300, 375, 200, 50,
                                     lambda: self.seleccionar_meta("Bajar de peso"))
        
        # Botón MANTENER PESO
        self.create_transparent_button(300, 445, 200, 50,
                                     lambda: self.seleccionar_meta("Mantener peso"))
        
        # Botón SUBIR DE PESO
        self.create_transparent_button(300, 515, 200, 50,
                                     lambda: self.seleccionar_meta("Subir de peso"))
    
    def add_page_7_elements(self):
        """Página 7 - RESULTADO"""
        print("   ➕ Agregando botón página 7")
        # Botón REINICIAR
        self.create_transparent_button(300, 675, 100, 50, self.reiniciar)
    
    # MÉTODOS DE FUNCIONALIDAD
    def seleccionar_genero(self, genero):
        self.genero.set(genero)
        print(f"Género seleccionado: {genero}")
        self.next_page()
    
    def seleccionar_tipo_cuerpo(self, tipo):
        self.tipo_cuerpo.set(tipo)
        print(f"Tipo de cuerpo seleccionado: {tipo}")
        self.next_page()
    
    def seleccionar_meta(self, meta):
        self.meta.set(meta)
        print(f"Meta seleccionada: {meta}")
        self.calcular_calorias()
        self.next_page()
    
    def validar_edad(self):
        try:
            edad = int(self.edad.get())
            if 10 <= edad <= 100:
                print(f"Edad ingresada: {edad}")
                self.next_page()
            else:
                messagebox.showerror("Error", "La edad debe estar entre 10 y 100 años")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una edad válida")
    
    def validar_peso(self):
        try:
            peso = float(self.peso.get())
            if 20 <= peso <= 300:
                print(f"Peso ingresado: {peso} kg")
                self.next_page()
            else:
                messagebox.showerror("Error", "El peso debe estar entre 20 y 300 kg")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un peso válido")
    
    def validar_altura(self):
        try:
            altura = float(self.altura.get())
            if 100 <= altura <= 250:
                print(f"Altura ingresada: {altura} cm")
                self.next_page()
            else:
                messagebox.showerror("Error", "La altura debe estar entre 100 y 250 cm")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una altura válida")
    
    def calcular_calorias(self):
        # Aquí puedes agregar tu lógica real de cálculo
        calorias = 1800
        print(f"Calorías calculadas: {calorias} KCAL")
    
    def next_page(self):
        if self.current_page < len(self.backgrounds) - 1:
            self.current_page += 1
            self.load_current_image()
    
    def reiniciar(self):
        # Reiniciar variables
        self.genero.set("")
        self.tipo_cuerpo.set("")
        self.edad.set("")
        self.peso.set("")
        self.altura.set("")
        self.meta.set("")
        
        # Volver al inicio
        self.current_page = 0
        self.load_current_image()
        print("🔁 Programa reiniciado")

if __name__ == "__main__":
    print("🚀 CALCULADORA COMPLETA - INICIANDO...")
    root = tk.Tk()
    app = CalorieCalculatorApp(root)
    root.mainloop()