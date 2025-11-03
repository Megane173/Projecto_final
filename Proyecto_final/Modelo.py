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

        existe= self.conexion.consultar("SELECT userUSUARIO, passwUSUARIO, idUSUARIO FROM usuario WHERE userUSUARIO=%s", (user,))

        if(existe):
            if(existe[0][1]==passw):
                return existe[0][2]

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
    
    def get_invernaderos(self, id_usuario):

        sql="SELECT idINVERNADERO, nomINVERNADERO, responsableINVERNADERO, fechaCreacINVERNADERO FROM invernadero WHERE idUSUARIO=%s"
        invernaderos= self.conexion.consultar(sql, (id_usuario,))
        
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
    
    def registrar(self, nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_usuario):
        
        
        sql="INSERT INTO invernadero (nomINVERNADERO, superfINVERNADERO, tipoCultivoINVERNADERO, fechaCreacINVERNADERO, responsableINVERNADERO, capacINVERNADERO, sistRiegoINVERNADERO, idUSUARIO)"
        sql+=" VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
        msg="Registro de invernadero exitoso."
        try:
            self.conexion.ejecutar(sql, (nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_usuario,))
        except Exception as e:
            print(f"Error: {e}")
            msg="Registro de invernadero fallido"
        return msg
            
        

class ModeloEditor:
    
    def __init__(self, conexion):
        self.conexion=conexion
    
    def get_invernadero(self, id_invernadero):
        
        sql="SELECT * from invernadero WHERE idINVERNADERO=%s"
        
        try:
            invernadero=self.conexion.consultar(sql, (id_invernadero,))       
        except Exception as e:
            print(f"Error: {e}")
        
        return invernadero    
    
    def actualizar(self, nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_usuario, id_inver):
        
        sql="UPDATE invernadero SET nomINVERNADERO=%s, superfINVERNADERO=%s, tipoCultivoINVERNADERO=%s, "
        sql+="fechaCreacINVERNADERO=%s, responsableINVERNADERO=%s, capacINVERNADERO=%s, sistRiegoINVERNADERO=%s, idUSUARIO=%s WHERE idINVERNADERO=%s"
        
        msg="Actualizacion del invernadero exitoso." 
        try:
            self.conexion.ejecutar(sql, (nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_usuario, id_inver,))
        
        except Exception as e:
            print(f"Error: {e}")
            msg="No se pudo efectuar la\nactualizacion del invernadero"
        
        return msg
             
        
class ModeloControladorInvernaderos:
    
    def __init__(self, conexion):
        self.conexion=conexion
        
    def get_invernaderos(self, id_usuario):

        sql="SELECT idINVERNADERO, nomINVERNADERO, responsableINVERNADERO FROM invernadero WHERE idUSUARIO=%s"
        invernaderos= self.conexion.consultar(sql, (id_usuario,))
        
        return invernaderos
    
    def eliminar(self, id_inver):
        
        sql="DELETE FROM invernadero WHERE idINVERNADERO=%s"
        
        msg="Eliminacion exitosa"   
        try:
            ejecucion=self.conexion.ejecutar(sql, (id_inver,))
        except Exception as e:
            print(f"Error: {e}")
            msg="Eliminacion fallida"
            
        return msg
        
