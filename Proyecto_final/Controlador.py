import Modelo
import Vista



class ControladorPrincipal:
    
    def __init__(self):

        self.conexion = Modelo.ConexionBD()
        self.id_usuario= None #Id de usuario logueado
        
        self.vista = Vista.VentanaLogin()
        self.controlador_por_vista = ControladorLogin(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        self.vista.iniciar()
    
    def abrir_menu(self):
        self.vista.cerrar()
        print(self.id_usuario)
        self.vista = Vista.VentanaMenu()
        self.controlador_por_vista = ControladorMenu(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        self.vista.imprimir_invernaderos()
        self.vista.iniciar()
    
    def abrir_registro(self):
        self.vista.cerrar()
        self.vista = Vista.VentanaRegistro()
        self.controlador_por_vista = ControladorRegistro(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        self.vista.iniciar()
        
    def abrir_controlador_invernaderos(self):       
        self.vista.cerrar()
        self.vista = Vista.VentanaControladorInvernaderos()
        self.controlador_por_vista = ControladorInvernaderos(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        invernaderos=self.vista.get_invernaderos()
        self.vista.llenar_vista(invernaderos)
        self.vista.iniciar()
    
    def abrir_editor(self, id_invernadero):       
        self.vista.cerrar()
        self.vista = Vista.VentanaRegistro()
        self.controlador_por_vista = ControladorEditor(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        self.vista.llenar_para_editar(id_invernadero)
        self.vista.iniciar()
        

class ControladorLogin:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_login = Modelo.ModeloLogin(conexion)
        self.controladorP=controladorP
        
    
    def login(self, user, passw):
        
        msg=self.modelo_login.login(user, passw)
        if(isinstance(msg, int)):
            self.controladorP.id_usuario=msg
            self.controladorP.abrir_menu()
        else:
            return msg
    
    def register(self, user, passw):
        
        msg=self.modelo_login.register(user, passw)
        if(msg=="1"):
            return "Registro exitoso."
        else:
            return msg

        
        
class ControladorMenu:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_menu = Modelo.ModeloMenu(conexion)
        self.controladorP=controladorP
    
    def get_invernaderos(self):
        
        id_usuario=self.controladorP.id_usuario
        msg=self.modelo_menu.get_invernaderos(id_usuario)
        if(msg=="0"):
            msg="No hay invernaderos registrados"
        return msg
    
    def get_por_nombre(self, nombre):
        
        invernaderos=self.modelo_menu.get_por_nombre(nombre)

        if(invernaderos=="0"):
            return "No existe ningun invernadero guardado con ese nombre."
        
    def abrir_registro(self):
        self.controladorP.abrir_registro()
        
    def abrir_controlador_invernaderos(self):
        self.controladorP.abrir_controlador_invernaderos()
        
        
class ControladorRegistro:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_menu = Modelo.ModeloRegistro(conexion)
        self.controladorP=controladorP
        
    def registrar(self, nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego):
        
        id_usuario=self.controladorP.id_usuario
        msg=self.modelo_menu.registrar(nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego, id_usuario)
        
        return msg
    
    def abrir_menu(self):
        self.controladorP.abrir_menu()
    
class ControladorInvernaderos:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_cont_inver = Modelo.ModeloControladorInvernaderos(conexion)
        self.controladorP=controladorP
        
    def abrir_editor(self, id_invernadero):
        self.controladorP.abrir_editor(id_invernadero)
        
    def get_invernaderos(self):
        
        id_usuario=self.controladorP.id_usuario
        return self.modelo_cont_inver.get_invernaderos(id_usuario)
        
class ControladorEditor:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_editor = Modelo.ModeloEditor(conexion)
        self.controladorP=controladorP
        
    def abrir_menu(self):
        self.controladorP.abrir_menu()
    
    def get_invernaderos(self, id_invernadero):
        
        invernadero=self.modelo_editor.get_invernadero(id_invernadero)
        
        return invernadero