import tkinter as tk
import mysql.connector
import mysql


#------------------CONEXIÓN BD--------------------
class ConexionBD:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tienda",
            port=3307,
            collation='utf8mb4_general_ci'
        )
        self.cursor = self.conexion.cursor()

    def ejecutar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        self.conexion.commit()

    def consultar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        return self.cursor.fetchall()


#-----------------OBJETOS----------------
class Cliente:
    
    def __init__(self, usuario, contraseña, nombre, apellidos, email):
        self.usuario=usuario
        self.contraseña=contraseña
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


class Enfermedad:

    def __init__(self, nombre, descripcion):
        self.nombre=nombre
        self.descripcion=descripcion


class Invernadero:

    def __init__(self, nombre, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego):

        self.nombre=nombre
        self.superficie=superficie
        self.tipo_cultivo=tipo_cultivo
        self.fecha_creacion=fecha_creacion
        self.responsable=responsable
        self.capacidad=capacidad
        self.sistema_riego=sistema_riego

#----------Interfaz de inicio de sesion---------------

class VentanaLogin:

    def __init__(self, root, conexion):

        self.root=root
        self.conexion=conexion

        self.frame= tk.Toplevel(self.root)
        self.frame.geometry(500, 500)
        self.frame.title("Login/Register")

        tk.Label(self.frame, text="Usuario").pack()
        self.entry_nombre= tk.Entry(self.frame).pack()

        tk.Label(self.frame, text="Contraseña")
        self.entry_contraseña= tk.Entry(self.frame).pack()

        tk.Button(self.frame, text="Iniciar Sesion", command= lambda: self.login() ).pack()
        tk.Button(self.frame, text="Registrarse", command= lambda: self.register()).pack()

    
    def login(self):

        user=self.entry_nombre.get()
        passw=self.entry_contraseña.get()

        existe= self.conexion("SELECT userCLIENTE, passwCLIENTE FROM cliente WHERE userCLIENTE=?", (user,))

        if(existe):
            if(existe[1]==passw):
                #Abre ventana que muestra los invernaderos del usuario

            else:
                print("Contraseña invalida")
        else:
            print("El usuario no existe")

    def register(self):

        user=self.entry_nombre.get()
        password=self.entry_contraseña.get()

        existe=self.conexion("SELECT userCLIENTE FROM cliente WHERE userCLIENTE=?", (user,))

        if(existe):
            print("Ese nombre de usuario ya esta registrado.")
        else:
            self.conexion("INSERT (userCLIENTE, passwCLIENTE) INTO cliente VALUES (%S, %S)", (user, password,))


        
