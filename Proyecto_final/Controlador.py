import Modelo
import Vista



class ControladorPrincipal:
    
    def __init__(self):

        self.conexion = Modelo.ConexionBD()
        
        
        self.vista = Vista.VentanaLogin()
        self.controlador_por_vista = ControladorLogin(self.conexion, self)
        self.vista.set_controlador(self.controlador_por_vista)
        self.vista.iniciar()
    
    def abrir_menu(self):
        self.vista.cerrar()
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
        
        

class ControladorLogin:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_login = Modelo.ModeloLogin(conexion)
        self.controladorP=controladorP
        
    
    def login(self, user, passw):
        
        msg=self.modelo_login.login(user, passw)
        if(msg=="1"):
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
        
        msg=self.modelo_menu.get_invernaderos()
        if(msg=="0"):
            msg="No hay invernaderos registrados"
        return msg
    
    def get_por_nombre(self, nombre):
        
        invernaderos=self.modelo_menu.get_por_nombre(nombre)

        if(invernaderos=="0"):
            return "No existe ningun invernadero guardado con ese nombre."
        
    def abrir_registro(self):
        self.controladorP.abrir_registro()
        
        
class ControladorRegistro:
    
    def __init__(self, conexion, controladorP):
        
        self.modelo_menu = Modelo.ModeloRegistro(conexion)
        self.controladorP=controladorP
        
    def registrar(self, nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego):
        
        msg=self.modelo_menu.registrar(nom, superficie, tipo_cultivo, fecha_creacion, responsable, capacidad, sistema_riego)
        
        return msg
    
    def abrir_menu(self):
        
        self.controladorP.abrir_menu()
    

            