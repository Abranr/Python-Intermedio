import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
from Database import Database
from Persona import Persona

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Perfil")
        self.root.geometry("500x400")
        
        # Configurar tema oscuro
        self.configurar_tema_oscuro()
        
        self.database = Database()
        self.usuario_actual = None
        
        # Ruta de la foto para nuevos registros
        self.ruta_foto = ""
        
        # Mostrar pantalla de inicio de sesión inicialmente
        self.mostrar_pantalla_login()
    
    def configurar_tema_oscuro(self):
        # Colores para el tema oscuro
        self.color_fondo = "#121212"  # Fondo principal
        self.color_componente = "#1E1E1E"  # Componentes como marcos
        self.color_texto = "#FFFFFF"  # Texto general
        self.color_texto_secundario = "#AAAAAA"  # Texto de menor importancia
        self.color_acento = "#2196F3"  # Color de acento (azul)
        self.color_error = "#CF6679"  # Color para errores
        
        # Configurar colores de la ventana principal
        self.root.configure(bg=self.color_fondo)
        
        # Estilos para ttk
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        # Configurar estilos de ttk
        self.style.configure('TFrame', background=self.color_fondo)
        self.style.configure('TLabel', background=self.color_fondo, foreground=self.color_texto)
        self.style.configure('TButton', background=self.color_componente, foreground=self.color_texto)
        self.style.configure('TEntry', fieldbackground=self.color_componente, foreground=self.color_texto)
        self.style.map('TButton', 
                  background=[('active', self.color_acento)],
                  foreground=[('active', self.color_texto)])
    
    def mostrar_pantalla_login(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Crear marco de inicio de sesión
        marco_login = tk.Frame(self.root, padx=20, pady=20, bg=self.color_fondo)
        marco_login.pack(fill="both", expand=True)
        
        # Título
        etiqueta_titulo = tk.Label(marco_login, text="Iniciar Sesión", font=("Arial", 18), 
                                  bg=self.color_fondo, fg=self.color_texto)
        etiqueta_titulo.pack(pady=10)
        
        # Correo
        etiqueta_email = tk.Label(marco_login, text="Correo Electrónico:", 
                                 bg=self.color_fondo, fg=self.color_texto)
        etiqueta_email.pack(anchor="w")
        
        self.entrada_email = tk.Entry(marco_login, width=30, bg=self.color_componente, 
                                    fg=self.color_texto, insertbackground=self.color_texto)
        self.entrada_email.pack(fill="x", pady=5)
        
        # Contraseña
        etiqueta_contrasena = tk.Label(marco_login, text="Contraseña:", 
                                      bg=self.color_fondo, fg=self.color_texto)
        etiqueta_contrasena.pack(anchor="w")
        
        self.entrada_contrasena = tk.Entry(marco_login, width=30, show="*", 
                                         bg=self.color_componente, fg=self.color_texto,
                                         insertbackground=self.color_texto)
        self.entrada_contrasena.pack(fill="x", pady=5)
        
        # Botón de inicio de sesión
        boton_login = tk.Button(marco_login, text="Iniciar Sesión", command=self.iniciar_sesion,
                              bg=self.color_acento, fg=self.color_texto,
                              activebackground=self.color_acento, activeforeground=self.color_texto)
        boton_login.pack(pady=10)
        
        # Enlace para registrarse
        enlace_registro = tk.Label(marco_login, text="¿No tienes cuenta? Regístrate", 
                                  fg=self.color_acento, bg=self.color_fondo, cursor="hand2")
        enlace_registro.pack()
        enlace_registro.bind("<Button-1>", lambda e: self.mostrar_pantalla_registro())
    
    def mostrar_pantalla_registro(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Crear marco de registro
        marco_registro = tk.Frame(self.root, padx=20, pady=20, bg=self.color_fondo)
        marco_registro.pack(fill="both", expand=True)
        
        # Título
        etiqueta_titulo = tk.Label(marco_registro, text="Registro", font=("Arial", 18),
                                  bg=self.color_fondo, fg=self.color_texto)
        etiqueta_titulo.pack(pady=10)
        
        # Crear un marco desplazable
        canvas = tk.Canvas(marco_registro, bg=self.color_fondo, highlightthickness=0)
        scrollbar = ttk.Scrollbar(marco_registro, orient="vertical", command=canvas.yview)
        marco_desplazable = tk.Frame(canvas, bg=self.color_fondo)
        
        marco_desplazable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=marco_desplazable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # ID
        etiqueta_id = tk.Label(marco_desplazable, text="Identificación:", 
                             bg=self.color_fondo, fg=self.color_texto)
        etiqueta_id.pack(anchor="w")
        
        self.entrada_id = tk.Entry(marco_desplazable, width=30, 
                                bg=self.color_componente, fg=self.color_texto,
                                insertbackground=self.color_texto)
        self.entrada_id.pack(fill="x", pady=5)
        
        # Nombre
        etiqueta_nombre = tk.Label(marco_desplazable, text="Nombre:", 
                                 bg=self.color_fondo, fg=self.color_texto)
        etiqueta_nombre.pack(anchor="w")
        
        self.entrada_nombre = tk.Entry(marco_desplazable, width=30, 
                                    bg=self.color_componente, fg=self.color_texto,
                                    insertbackground=self.color_texto)
        self.entrada_nombre.pack(fill="x", pady=5)
        
        # Apellido
        etiqueta_apellido = tk.Label(marco_desplazable, text="Apellido:", 
                                   bg=self.color_fondo, fg=self.color_texto)
        etiqueta_apellido.pack(anchor="w")
        
        self.entrada_apellido = tk.Entry(marco_desplazable, width=30, 
                                       bg=self.color_componente, fg=self.color_texto,
                                       insertbackground=self.color_texto)
        self.entrada_apellido.pack(fill="x", pady=5)
        
        # Edad
        etiqueta_edad = tk.Label(marco_desplazable, text="Edad:", 
                               bg=self.color_fondo, fg=self.color_texto)
        etiqueta_edad.pack(anchor="w")
        
        self.entrada_edad = tk.Entry(marco_desplazable, width=30, 
                                  bg=self.color_componente, fg=self.color_texto,
                                  insertbackground=self.color_texto)
        self.entrada_edad.pack(fill="x", pady=5)
        
        # Foto
        etiqueta_foto = tk.Label(marco_desplazable, text="Fotografía:", 
                               bg=self.color_fondo, fg=self.color_texto)
        etiqueta_foto.pack(anchor="w")
        
        marco_foto = tk.Frame(marco_desplazable, bg=self.color_fondo)
        marco_foto.pack(fill="x", pady=5)
        
        self.etiqueta_ruta_foto = tk.Label(marco_foto, text="No se ha seleccionado ningún archivo", 
                                        width=30, bg=self.color_fondo, fg=self.color_texto_secundario)
        self.etiqueta_ruta_foto.pack(side="left", fill="x", expand=True)
        
        boton_foto = tk.Button(marco_foto, text="Examinar", command=self.seleccionar_foto,
                            bg=self.color_acento, fg=self.color_texto,
                            activebackground=self.color_acento, activeforeground=self.color_texto)
        boton_foto.pack(side="right")
        
        # Correo
        etiqueta_email = tk.Label(marco_desplazable, text="Correo Electrónico:", 
                                bg=self.color_fondo, fg=self.color_texto)
        etiqueta_email.pack(anchor="w")
        
        self.entrada_registro_email = tk.Entry(marco_desplazable, width=30, 
                                           bg=self.color_componente, fg=self.color_texto,
                                           insertbackground=self.color_texto)
        self.entrada_registro_email.pack(fill="x", pady=5)
        
        # Contraseña
        etiqueta_contrasena = tk.Label(marco_desplazable, text="Contraseña:", 
                                     bg=self.color_fondo, fg=self.color_texto)
        etiqueta_contrasena.pack(anchor="w")
        
        self.entrada_registro_contrasena = tk.Entry(marco_desplazable, width=30, show="*", 
                                                bg=self.color_componente, fg=self.color_texto,
                                                insertbackground=self.color_texto)
        self.entrada_registro_contrasena.pack(fill="x", pady=5)
        
        # Botón de registro
        boton_registro = tk.Button(marco_desplazable, text="Registrarse", command=self.registrar,
                                 bg=self.color_acento, fg=self.color_texto,
                                 activebackground=self.color_acento, activeforeground=self.color_texto)
        boton_registro.pack(pady=10)
        
        # Enlace para iniciar sesión
        enlace_login = tk.Label(marco_desplazable, text="¿Ya tienes cuenta? Inicia sesión", 
                              fg=self.color_acento, bg=self.color_fondo, cursor="hand2")
        enlace_login.pack()
        enlace_login.bind("<Button-1>", lambda e: self.mostrar_pantalla_login())
    
    def mostrar_pantalla_perfil(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Crear marco de perfil
        marco_perfil = tk.Frame(self.root, padx=20, pady=20, bg=self.color_fondo)
        marco_perfil.pack(fill="both", expand=True)
        
        # Título
        etiqueta_titulo = tk.Label(marco_perfil, text="Perfil de Usuario", font=("Arial", 18),
                                 bg=self.color_fondo, fg=self.color_texto)
        etiqueta_titulo.pack(pady=10)
        
        # Información del usuario
        marco_info = tk.Frame(marco_perfil, bg=self.color_fondo)
        marco_info.pack(pady=10, fill="both", expand=True)
        
        # Foto
        try:
            imagen = Image.open(self.usuario_actual.ruta_foto)
            imagen = imagen.resize((100, 100), Image.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            
            etiqueta_foto = tk.Label(marco_info, image=foto, bg=self.color_fondo)
            etiqueta_foto.image = foto  # Mantener una referencia
            etiqueta_foto.grid(row=0, column=0, rowspan=5, padx=10)
        except Exception as e:
            etiqueta_foto = tk.Label(marco_info, text="No se pudo cargar la foto", 
                                   width=15, height=7, relief="solid", 
                                   bg=self.color_componente, fg=self.color_texto)
            etiqueta_foto.grid(row=0, column=0, rowspan=5, padx=10)
        
        # ID
        etiqueta_id = tk.Label(marco_info, text="Identificación:", font=("Arial", 10, "bold"),
                             bg=self.color_fondo, fg=self.color_texto)
        etiqueta_id.grid(row=0, column=1, sticky="w")
        
        valor_id = tk.Label(marco_info, text=self.usuario_actual.id,
                          bg=self.color_fondo, fg=self.color_texto)
        valor_id.grid(row=0, column=2, sticky="w")
        
        # Nombre
        etiqueta_nombre = tk.Label(marco_info, text="Nombre:", font=("Arial", 10, "bold"),
                                 bg=self.color_fondo, fg=self.color_texto)
        etiqueta_nombre.grid(row=1, column=1, sticky="w")
        
        valor_nombre = tk.Label(marco_info, text=self.usuario_actual.nombre,
                              bg=self.color_fondo, fg=self.color_texto)
        valor_nombre.grid(row=1, column=2, sticky="w")
        
        # Apellido
        etiqueta_apellido = tk.Label(marco_info, text="Apellido:", font=("Arial", 10, "bold"),
                                   bg=self.color_fondo, fg=self.color_texto)
        etiqueta_apellido.grid(row=2, column=1, sticky="w")
        
        valor_apellido = tk.Label(marco_info, text=self.usuario_actual.apellido,
                                bg=self.color_fondo, fg=self.color_texto)
        valor_apellido.grid(row=2, column=2, sticky="w")
        
        # Correo
        etiqueta_email = tk.Label(marco_info, text="Correo:", font=("Arial", 10, "bold"),
                                bg=self.color_fondo, fg=self.color_texto)
        etiqueta_email.grid(row=3, column=1, sticky="w")
        
        valor_email = tk.Label(marco_info, text=self.usuario_actual.email,
                             bg=self.color_fondo, fg=self.color_texto)
        valor_email.grid(row=3, column=2, sticky="w")
        
        # Edad
        etiqueta_edad = tk.Label(marco_info, text="Edad:", font=("Arial", 10, "bold"),
                               bg=self.color_fondo, fg=self.color_texto)
        etiqueta_edad.grid(row=4, column=1, sticky="w")
        
        valor_edad = tk.Label(marco_info, text=str(self.usuario_actual.edad),
                            bg=self.color_fondo, fg=self.color_texto)
        valor_edad.grid(row=4, column=2, sticky="w")
        
        # Botón de cerrar sesión
        boton_cerrar_sesion = tk.Button(marco_perfil, text="Cerrar Sesión", command=self.mostrar_pantalla_login,
                                      bg=self.color_acento, fg=self.color_texto,
                                      activebackground=self.color_acento, activeforeground=self.color_texto)
        boton_cerrar_sesion.pack(pady=10)
    
    def seleccionar_foto(self):
        filetypes = [("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")]
        self.ruta_foto = filedialog.askopenfilename(title="Seleccionar Foto", filetypes=filetypes)
        
        if self.ruta_foto:
            nombre_archivo = os.path.basename(self.ruta_foto)
            self.etiqueta_ruta_foto.config(text=nombre_archivo)
    
    def registrar(self):
        try:
            id = self.entrada_id.get()
            nombre = self.entrada_nombre.get()
            apellido = self.entrada_apellido.get()
            email = self.entrada_registro_email.get()
            contrasena = self.entrada_registro_contrasena.get()
            
            # Validar que la edad sea un número
            try:
                edad = int(self.entrada_edad.get())
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número entero.")
                return
            
            # Validar que todos los campos estén completos
            if not (id and nombre and apellido and email and contrasena and self.ruta_foto):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            
            # Registrar usuario
            exito, mensaje = Persona.registrar(id, nombre, apellido, self.ruta_foto, email, contrasena, edad, self.database)
            
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.mostrar_pantalla_login()
            else:
                messagebox.showerror("Error", mensaje)
        
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error: {str(e)}")
    
    def iniciar_sesion(self):
        email = self.entrada_email.get()
        contrasena = self.entrada_contrasena.get()
        
        # Validar que ambos campos estén completos
        if not (email and contrasena):
            messagebox.showerror("Error", "Ambos campos son obligatorios.")
            return
        
        # Intentar iniciar sesión
        exito, resultado = Persona.iniciar_sesion(email, contrasena, self.database)
        
        if exito:
            self.usuario_actual = resultado
            self.mostrar_pantalla_perfil()
        else:
            messagebox.showerror("Error", resultado)

# Configurar el estilo de las ventanas de diálogo
def personalizar_ventanas_dialogo():
    # Intentar reconfigurar el estilo de los diálogos (aunque esto tiene limitaciones)
    try:
        messagebox._show.config(bg="#121212", fg="#FFFFFF")
    except:
        pass  # Este enfoque puede no funcionar en todas las plataformas

if __name__ == "__main__":
    root = tk.Tk()
    personalizar_ventanas_dialogo()
    app = App(root)
    root.mainloop()