import tkinter as tk
import tkcalendar as tkc
import mysql.connector
import mysql

class VentanaLogin:

    def __init__(self):
        
        self.__controlador=None

        self.frame= tk.Tk()
        self.frame.geometry("500x300")
        self.frame.title("Login/Register")

        tk.Label(self.frame, text="Usuario").pack(pady=3)
        self.entry_nombre= tk.Entry(self.frame)
        self.entry_nombre.pack()

        tk.Label(self.frame, text="Contraseña").pack(pady=3)
        self.entry_contraseña= tk.Entry(self.frame)
        self.entry_contraseña.pack(pady=5)
        
        self.frame_botones=tk.Frame(self.frame)
        self.frame_botones.pack(pady=15)
        
        tk.Button(self.frame_botones, text="Iniciar Sesion", command= lambda: self.login() ).pack(side="right", padx=5)
        tk.Button(self.frame_botones, text="Registrarse", command= lambda: self.register()).pack(side="right", padx=5)
        
        self.label_result=tk.Label(self.frame, text="")
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

        self.__controlador.login(user, passw)

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
        
        self.entry_nombre= tk.Entry(self.frame_search)
        self.entry_nombre.pack(side="left")
        
        tk.Button(self.frame_search, text="Buscar", command= lambda: self.buscar()).pack(side="right", padx=4)
        
        self.frame_buttons=tk.Frame(self.frame)
        self.frame_buttons.pack(pady=10)
        
        tk.Button(self.frame_buttons, text="Registrar invernadero", command=lambda: self.abrir_registro()).pack(side="left")
        tk.Button(self.frame_buttons, text="Control invernadero", command=lambda: self.abrir_control_invernaderos()).pack(side="left")
        tk.Button(self.frame_buttons, text="Enfermedades").pack(side="left")
        
        tk.Label(self.frame, text="Invernaderos: ", font=("bold")).pack(pady=5)

        self.label_invernaderos=tk.Label(self.frame, text="")
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
        self.frame.geometry("500x400")
        self.frame.title("Registro de invernaderos")


        self.frame_side1=tk.Frame(self.frame)
        self.frame_side1.pack(side="left", padx=30)
        self.frame_side2=tk.Frame(self.frame)
        self.frame_side2.pack(side="left", padx=15)
        
        tk.Label(self.frame_side1, text="Nombre del invernadero").pack()
        self.entry_nombre=tk.Entry(self.frame_side1)
        self.entry_nombre.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Superficie (m^2)").pack()
        self.entry_superficie=tk.Entry(self.frame_side1)
        self.entry_superficie.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Tipo de cultivo").pack()
        opciones = ["Tomate","Lechuga","Papa","Zanahoria","Maíz","Fresa","Banano","Cacao","Café"]
        self.opcion_cultivo=tk.StringVar(self.frame_side1)
        self.opcion_cultivo.set(opciones[8])
        self.tipo_cultivo = tk.OptionMenu(self.frame_side1, self.opcion_cultivo, *opciones)
        self.tipo_cultivo.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Fecha de creacion").pack()
        self.entry_fecha= tkc.DateEntry(self.frame_side1, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entry_fecha.pack(pady=5)
        
        tk.Label(self.frame_side1, text="Responsable del invernadero").pack()
        self.entry_responsable=tk.Entry(self.frame_side1)
        self.entry_responsable.pack(pady=5)
        
        tk.Label(self.frame_side2, text="Capacidad de producccion").pack()
        self.entry_capacidad=tk.Entry(self.frame_side2)
        self.entry_capacidad.pack(pady=5)
        
        tk.Label(self.frame_side2, text="Sistema de riego").pack()
        opciones2 = ["Manual", "Automatizado", "Por goteo"]
        self.opcion_riego=tk.StringVar(self.frame_side2)
        self.opcion_riego.set(opciones2[0])
        self.sistema_riego = tk.OptionMenu(self.frame_side2, self.opcion_riego, *opciones2)
        self.sistema_riego.pack(pady=5)
        
        self.frame_botones=tk.Frame(self.frame_side2)
        self.frame_botones.pack(pady=15)
        
        self.button_guardar=tk.Button(self.frame_botones, text="Guardar", command= lambda: self.registrar() ).pack(side="right", padx=5)
        tk.Button(self.frame_botones, text="Cancelar", command= lambda: self.abrir_menu()).pack(side="right", padx=5)
        
        self.label_resultado=tk.Label(self.frame_side2, text="")
        self.label_resultado.pack(pady=15)
        
    def iniciar(self):
        self.frame.mainloop()
    
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
        self.button_guardar.config(command=lambda id_inver=id_invernadero: self.editar(id_inver))
    
    def editar(self):
        self.__controlador
    
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
        
        for invernadero in invernaderos:
            
            frame_div=tk.Frame(self.frame)
            frame_div.pack(pady=10)
            
            tk.Label(frame_div, text=invernadero[1]).pack(side="left", padx=15)
            tk.Button(frame_div, text="Editar", command= lambda id_inver=invernadero[0]: self.abrir_editor(id_inver)).pack(side="left", padx=5)
            tk.Button(frame_div, text="Eliminar").pack(side="left", padx=5)
    
    def iniciar(self):
        self.frame.mainloop()
    
    def set_controlador(self, controlador):
        self.__controlador=controlador
    
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