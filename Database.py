class Database:
    def __init__(self):
        self.usuarios = []
        self.cargar_desde_archivo()
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.guardar_en_archivo()
    
    def obtener_usuario_por_correo(self, correo):
        for usuario in self.usuarios:
            if usuario.email == correo:
                return usuario
        return None
    
    def guardar_en_archivo(self):
        with open("Database.txt", "w") as archivo:
            for usuario in self.usuarios:
                archivo.write(f"{usuario.id},{usuario.nombre},{usuario.apellido},{usuario.ruta_foto},{usuario.email},{usuario.contrasena},{usuario.edad}\n")
    
    def cargar_desde_archivo(self):
        try:
            from Persona import Persona
            with open("Database.txt", "r") as archivo:
                for linea in archivo:
                    if linea.strip():
                        datos = linea.strip().split(',')
                        usuario = Persona(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], int(datos[6]))
                        self.usuarios.append(usuario)
        except FileNotFoundError:
            # El archivo no existe todavía, no hay problema
            pass