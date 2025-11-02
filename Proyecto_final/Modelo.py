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
            database="sistemainvernaderos",
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
class Usuario:
    
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

#----------Modelos---------------

class ModeloLogin:

    def __init__(self, conexion):

        self.conexion=conexion
    
    def login(self, user, passw):

        existe= self.conexion.consultar("SELECT userUSUARIO, passwUSUARIO FROM usuario WHERE userUSUARIO=%s", (user,))

        if(existe):
            if(existe[0][1]==passw):
                return "1"

            else:
                return "Contraseña invalida"
        else:
            return "Ese usuario no existe"

    def register(self, user, password):
        
        user=user.lower()
        existe=self.conexion.consultar("SELECT userUSUARIO FROM usuario WHERE userUSUARIO=%s", (user,))

        if(existe):
            return "Ese nombre de usuario ya esta registrado."
        else:
            self.conexion.ejecutar("INSERT INTO usuario (userUSUARIO, passwUSUARIO) VALUES (%s, %s)", (user, password,))
            return "1"

class ModeloMenu:
    
    def __init__(self, conexion):
        self.conexion=conexion
    
    def get_invernaderos(self):

        invernaderos= self.conexion.consultar("SELECT idINVERNADERO, nomINVERNADERO, responsableINVERNADERO, fechaCreacINVERNADERO FROM invernadero")
        
        msg=""
        
        if(invernaderos):          
            for invernadero in invernaderos:
                msg+=f"Id: {invernadero[0]} / Nombre: {invernadero[1]}"
                msg+=f"\nResponsable: {invernadero[2]}"
                msg+=f"\nFecha de creacion: {invernadero[3]}"+"\n\n"
        else:
            msg="0"
        
        return msg

    def get_por_nombre(self, nombre):

        invernaderos=self.conexion.consultar("SELECT idINVERNADERO, nomINVERNADERO, responsableINVERNADERO, fechaCreacINVERNADERO FROM invernadero WHERE nomINVERNADERO=%s", (nombre,))

        if(invernaderos):
            for invernadero in invernaderos:
                msg+=f"Id: {invernadero[0]} / Nombre: {invernadero[1]}"
                msg+=f"\nResponsable: {invernadero[2]}"
                msg+=f"\nFecha de creacion: {invernadero[3]}"+"\n"
            return msg
        else:
            return "0"

class ModeloRegistro:
    
    def __init__(self, conexion):
        self.conexion=conexion
    
    def registrar(self, nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego):
        
        
        sql="INSERT INTO invernadero (nomINVERNADERO, superfINVERNADERO, tipoCultivoINVERNADERO, fechaCreacINVERNADERO, responsableINVERNADERO, capacINVERNADERO, sistRiegoINVERNADERO)"
        sql+=" VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        try:
            self.conexion.ejecutar(sql, (nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego,))
        
        except Exception as e:
            print(f"Error: {e}")
            
        return "Registro de invernadero exitoso."
            
        
