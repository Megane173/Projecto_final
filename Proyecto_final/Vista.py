import tkinter as tk
import tkcalendar as tkc
import mysql.connector
import mysql


# ----- Estilos -----
estilo_boton= {
    "bg": "#80e777",
    "fg": "black",
    "activebackground": "#e7dd4d",
    "relief": "groov",
    "font": ("Arial", 12, "normal"),
    "cursor": "hand2",
    "padx": 2,
    "pady": 5
}

estilo_boton_s_d= {
    "fg": "black",
    "activebackground": "#e7df6e",
    "relief": "groov",
    "font": ("Arial", 12, "normal"),
    "cursor": "hand2",
    "padx": 2,
    "pady": 5
}

estilo_boton_login = {
    "bg": "#48b84c",          
    "fg": "white",            
    "activebackground": "#cde85f",  
    "activeforeground": "black",
    "relief": "groov",
    "bd": 1,                  
    "highlightbackground": "#353535", 
    "highlightcolor": "#FFFFFF",
    "highlightthickness": 2,
    "font": ("Arial", 11, "bold"),
    "cursor": "hand2"
}

estilo_label1 = {
    "bg": "#48b84c",   
    "fg": "black",
    "relief": "solid",
    "bd": 1,
    "font": ("Arial", 11, "bold"),
    "padx": 8,
    "pady": 5
}

estilo_label2 = {
    "fg": "black",
    "relief": "solid",
    "bd": 1,
    "font": ("Arial", 12, "bold"),
    "padx": 4,
    "pady": 2
}

estilo_label3 = {
    "fg": "black",
    "font": ("Arial", 12, "bold"),
    "padx": 8,
    "pady": 5
}

estilo_label4 = {
    "fg": "black",
    "font": ("Arial", 12),
    "padx": 8,
    "pady": 5
}

estilo_entry = {
    "bg": "#fffdd0",
    "fg": "black",           
    "bd": 1,
    "font": ("Arial", 10),
    "relief": "sunken",
    "width": 25
}

class VentanaLogin:

    def __init__(self):
        
        self.__controlador=None

        self.frame= tk.Tk()
        self.frame.geometry("500x300")
        self.frame.title("Login/Register")

        tk.Label(self.frame, text="Usuario", **estilo_label1).pack(pady=3)
        self.entry_nombre= tk.Entry(self.frame, **estilo_entry)
        self.entry_nombre.pack()

        tk.Label(self.frame, text="Contraseña", **estilo_label1).pack(pady=3)
        self.entry_contraseña= tk.Entry(self.frame, **estilo_entry)
        self.entry_contraseña.pack(pady=5)
        
        self.frame_botones=tk.Frame(self.frame)
        self.frame_botones.pack(pady=15)
        
        tk.Button(self.frame_botones, text="Iniciar Sesion", command= lambda: self.login(), **estilo_boton_login).pack(side="right", padx=5)
        tk.Button(self.frame_botones, text="Registrarse", command= lambda: self.register(), **estilo_boton_login).pack(side="right", padx=5)
        
        self.label_result=tk.Label(self.frame, text="", **estilo_label4)
        self.label_result.pack(pady=5)
        
    def iniciar(self):
        self.frame.mainloop()
    
    def set_controlador(self, controlador):
        self.__controlador=controlador
    
    def get_controlador(self):
        return self.__controlador
    
    def login(self):

        user=self.entry_nombre.get()
        passw=self.entry_contraseña.get()

        msg=self.__controlador.login(user, passw)
        try:
            self.label_result.config(text=msg)
        except Exception:
            print(msg)

    def register(self):

        user=self.entry_nombre.get()
        password=self.entry_contraseña.get()

        msg=self.__controlador.register(user, password)
        
        print(msg+"asd")
        self.label_result.config(text=msg)
    
    def cerrar(self):
        
        self.frame.destroy()
    
class VentanaMenu:

    def __init__(self):

        self.__controlador=None

        self.frame= tk.Tk()
        self.frame.geometry("500x500")
        self.frame.title("Menu")

        self.frame_search=tk.Frame(self.frame)
        self.frame_search.pack(pady=5)
        
        self.entry_nombre= tk.Entry(self.frame_search, **estilo_entry)
        self.entry_nombre.pack(side="left")
        
        tk.Button(self.frame_search, text="Buscar", command= lambda: self.buscar(), **estilo_boton).pack(side="right", padx=4)
        
        self.frame_buttons=tk.Frame(self.frame)
        self.frame_buttons.pack(pady=10)
        
        tk.Button(self.frame_buttons, text="Registrar invernadero", command=lambda: self.abrir_registro(), **estilo_boton).pack(side="left")
        tk.Button(self.frame_buttons, text="Control invernadero", command=lambda: self.abrir_control_invernaderos(), **estilo_boton).pack(side="left")
        tk.Button(self.frame_buttons, text="Enfermedades", **estilo_boton).pack(side="left")
        
        tk.Label(self.frame, text="Invernaderos: ", **estilo_label3).pack(pady=5)

        self.label_invernaderos=tk.Label(self.frame, text="", **estilo_label3)
        self.label_invernaderos.pack()
        
    
    def iniciar(self):
        self.frame.mainloop()
    
    def set_controlador(self, controlador):
        self.__controlador=controlador 
    
    def get_invernaderos(self):
        return self.__controlador.get_invernaderos()
    
    def imprimir_invernaderos(self):
        self.label_invernaderos.config(text=self.get_invernaderos())

    def get_por_nombre(self):
        
        nombre=self.entry_nombre.get()
        msg=self.__controlador.get_por_nombre(nombre) 
        
        self.label_invernaderos.config(text=msg)
    
    def buscar(self):
        
        nombre=self.entry_nombre.get()
        msg=self.__controlador.get_por_nombre(nombre)
        self.label_invernaderos.config(text=msg)
    
    def abrir_control_invernaderos(self):
        
        self.__controlador.abrir_controlador_invernaderos()
    
    def abrir_registro(self):
        
        self.__controlador.abrir_registro()
        
        
    def cerrar(self):
        
        self.frame.destroy()
        

class VentanaRegistro:

    def __init__(self):
        
        self.__controlador=None

        self.frame= tk.Tk()
        self.frame.geometry("550x400")
        self.frame.title("Registro de invernaderos")


        self.frame_side1=tk.Frame(self.frame)
        self.frame_side1.pack(side="left", padx=30)
        self.frame_side2=tk.Frame(self.frame)
        self.frame_side2.pack(side="left", padx=15)
        
        tk.Label(self.frame_side1, text="Nombre del invernadero", **estilo_label3).pack()
        self.entry_nombre=tk.Entry(self.frame_side1, **estilo_entry)
        self.entry_nombre.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Superficie (m^2)", **estilo_label3).pack()
        self.entry_superficie=tk.Entry(self.frame_side1, **estilo_entry)
        self.entry_superficie.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Tipo de cultivo", **estilo_label3).pack()
        opciones = ["Tomate","Lechuga","Papa","Zanahoria","Maíz","Fresa","Banano","Cacao","Café"]
        self.opcion_cultivo=tk.StringVar(self.frame_side1)
        self.opcion_cultivo.set(opciones[8])
        self.tipo_cultivo = tk.OptionMenu(self.frame_side1, self.opcion_cultivo, *opciones)
        self.tipo_cultivo.pack(pady=5)
        self.tipo_cultivo.config(bg="#fffdd0", fg="black", font=("Arial", 10), relief="sunken", padx=4, pady=2)
                            
        
        tk.Label(self.frame_side1, text="Fecha de creacion", **estilo_label3).pack()
        self.entry_fecha= tkc.DateEntry(self.frame_side1, width=20, background='#fffdd0', foreground='black', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entry_fecha.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Responsable del invernadero", **estilo_label3).pack()
        self.entry_responsable=tk.Entry(self.frame_side1, **estilo_entry)
        self.entry_responsable.pack(pady=5)
        
        tk.Label(self.frame_side2, text="Capacidad de producccion", **estilo_label3).pack()
        self.entry_capacidad=tk.Entry(self.frame_side2, **estilo_entry)
        self.entry_capacidad.pack(pady=5)
        
        tk.Label(self.frame_side2, text="Sistema de riego", **estilo_label3).pack()
        opciones2 = ["Manual", "Automatizado", "Por goteo"]
        self.opcion_riego=tk.StringVar(self.frame_side2)
        self.opcion_riego.set(opciones2[0])
        self.sistema_riego = tk.OptionMenu(self.frame_side2, self.opcion_riego, *opciones2)
        self.sistema_riego.pack(pady=5)
        self.sistema_riego.config(bg="#fffdd0", fg="black", font=("Arial", 10), relief="sunken", padx=4, pady=2)
        
        self.frame_botones=tk.Frame(self.frame_side2)
        self.frame_botones.pack(pady=15)
        
        self.button_guardar=tk.Button(self.frame_botones, text="Guardar", command= lambda: self.registrar(), **estilo_boton_s_d, bg="#7cd67f")
        self.button_guardar.pack(side="right", padx=5)
        tk.Button(self.frame_botones, text="Cancelar", command= lambda: self.abrir_menu(), **estilo_boton_s_d, bg="#FF8282").pack(side="right", padx=5)
        
        self.label_resultado=tk.Label(self.frame_side2, text="", **estilo_label4)
        self.label_resultado.pack(pady=15)
        
        tk.Button(self.frame_side2, text="REGRESAR", command=lambda: self.regresar(), **estilo_boton_s_d, bg="#F8BB38").pack(side="right", pady=35)
        
    def iniciar(self):
        self.frame.mainloop()
    
    def regresar(self):
        self.__controlador.regresar()
    
    def set_controlador(self, controlador):
        self.__controlador=controlador
    
    def get_controlador(self):
        return self.__controlador
    
    def registrar(self):
        
        nom=self.entry_nombre.get()
        superficie=self.entry_superficie.get()
        tipo_cultivo=self.opcion_cultivo.get()
        fecha_creacion=self.entry_fecha.get()
        responsable=self.entry_responsable.get()
        capacidad=self.entry_capacidad.get()
        sistema_riego=self.opcion_riego.get()
        msg=self.__controlador.registrar(nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego)
        print(msg)
        self.label_resultado.config(text=msg)
    
    def llenar_para_editar(self, id_invernadero):
        inver=self.__controlador.get_invernaderos(id_invernadero)
        
        self.entry_nombre.insert(0, inver[0][1])
        self.entry_superficie.insert(0, inver[0][2])
        self.opcion_cultivo.set(inver[0][3])
        self.entry_fecha.set_date( inver[0][4])
        self.entry_responsable.insert(0, inver[0][5])
        self.entry_capacidad.insert(0, inver[0][6])
        self.opcion_riego.set(inver[0][7])
    
    
    def cambiar_boton_guardar(self, id_invernadero):
        self.button_guardar.config(text="Actualizar")
        self.button_guardar.config(command=lambda id_inver=id_invernadero: self.actualizar(id_inver))
    
    def actualizar(self, id_inver):
        
        nom=self.entry_nombre.get()
        superficie=self.entry_superficie.get()
        tipo_cultivo=self.opcion_cultivo.get()
        fecha_creacion=self.entry_fecha.get()
        responsable=self.entry_responsable.get()
        capacidad=self.entry_capacidad.get()
        sistema_riego=self.opcion_riego.get()
        
        msg=self.__controlador.actualizar(nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_inver)
        self.label_resultado.config(text=msg)
    
    def abrir_menu(self):
        self.__controlador.abrir_menu()
        
    def cerrar(self):
        self.frame.destroy()
        
    
class VentanaControladorInvernaderos:
    
    def __init__(self):
        
        self.__controlador=None
        self.frame=tk.Tk()
        self.frame.geometry("500x500")
        
    def llenar_vista(self, invernaderos):
        
        if(invernaderos):
            for invernadero in invernaderos:
                
                frame_div=tk.Frame(self.frame)
                frame_div.pack(pady=10)
                
                tk.Label(frame_div, text=invernadero[1], **estilo_label2).pack(side="left", padx=15)
                tk.Button(frame_div, text="Actualizar", command= lambda id_inver=invernadero[0]: self.abrir_editor(id_inver), **estilo_boton_s_d, bg="#7cd67f").pack(side="left", padx=5)
                tk.Button(frame_div, text="Eliminar", command= lambda id_inver=invernadero[0]: self.eliminar(id_inver), **estilo_boton_s_d, bg="#FF8282").pack(side="left", padx=5)
                
            self.label_Result=tk.Label(self.frame, text="", **estilo_label3)
            self.label_Result.pack(pady=10)
        else:
            self.label_Result=tk.Label(self.frame, text="No hay invernaderos registrados...", **estilo_label3)
            self.label_Result.pack(pady=10)
        tk.Button(self.frame, text="REGRESAR", command=lambda: self.regresar(), **estilo_boton_s_d, bg="#F8BB38").pack(side="right", padx=35, pady=5)
    
    def actualizar_vista(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        invernaderos = self.__controlador.get_invernaderos()
        self.llenar_vista(invernaderos)
    
    def regresar(self):
        self.__controlador.regresar()
        
    def iniciar(self):
        self.frame.mainloop()
    
    def set_controlador(self, controlador):
        self.__controlador=controlador
        
    def eliminar(self, id_inver):
        msg=self.__controlador.eliminar(id_inver)
        self.actualizar_vista()
        self.label_Result.config(text=msg)
        
    def get_controlador(self):
        return self.__controlador
    
    def get_invernaderos(self):
        return self.__controlador.get_invernaderos()
    
    def abrir_editor(self, id_invernadero):
        
        self.__controlador.abrir_editor(id_invernadero)
        
    def abrir_menu(self):
        self.__controlador.abrir_menu()
        
    def cerrar(self):
        self.frame.destroy()