import re

class Persona:
    def __init__(self, id, nombre, apellido, ruta_foto, email, contrasena, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.ruta_foto = ruta_foto
        self.email = email
        self.contrasena = contrasena
        self.edad = edad
    
    # Getters
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_ruta_foto(self):
        return self.ruta_foto
    
    def get_email(self):
        return self.email
    
    def get_edad(self):
        return self.edad
    
    # Setters
    def set_id(self, id):
        self.id = id
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def set_ruta_foto(self, ruta_foto):
        self.ruta_foto = ruta_foto
    
    def set_email(self, email):
        self.email = email
    
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena
    
    def set_edad(self, edad):
        self.edad = edad
    
    @staticmethod
    def registrar(id, nombre, apellido, ruta_foto, email, contrasena, edad, database):
        # Validar formato de correo electrónico
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "El correo electrónico no tiene un formato válido."
        
        # Validar longitud de contraseña
        if len(contrasena) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres."
        
        # Validar edad
        if edad < 18:
            return False, "Debes ser mayor de 18 años para registrarte."
        
        # Verificar si el correo ya existe
        if database.obtener_usuario_por_correo(email):
            return False, "Ya existe un usuario con este correo electrónico."
        
        # Crear y agregar nuevo usuario
        nuevo_usuario = Persona(id, nombre, apellido, ruta_foto, email, contrasena, edad)
        database.agregar_usuario(nuevo_usuario)
        return True, "Usuario registrado exitosamente."
    
    @staticmethod
    def iniciar_sesion(email, contrasena, database):
        usuario = database.obtener_usuario_por_correo(email)
        if usuario and usuario.contrasena == contrasena:
            return True, usuario
        return False, "Correo electrónico o contraseña incorrectos."