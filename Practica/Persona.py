from colorama import Fore, Style
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class Persona:
    def __init__(self, nombre: str, apellido: str, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.lugares_frecuentes = []
        self.foto = self.seleccionar_foto()

    def seleccionar_foto(self):
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de tkinter
        file_path = filedialog.askopenfilename(
            title="Seleccionar foto",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            return file_path
        return None

    def agregar_lugar(self, lugar):
        self.lugares_frecuentes.append(lugar)

    def mostrar_foto(self):
        if self.foto:
            img = Image.open(self.foto)
            img.show()

    def __str__(self):
        lugares_str = "\n".join([str(lugar) for lugar in self.lugares_frecuentes])
        return f"{Fore.BLUE}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}\n" \
               f"{Fore.BLUE}║ Persona: {self.nombre} {self.apellido}{Style.RESET_ALL}\n" \
               f"{Fore.BLUE}║ Rol: {self.rol.value}{Style.RESET_ALL}\n" \
               f"{Fore.BLUE}║ Foto: {self.foto if self.foto else 'No seleccionada'}{Style.RESET_ALL}\n" \
               f"{Fore.BLUE}║ Lugares Frecuentes:{Style.RESET_ALL}\n" \
               f"{lugares_str}\n" \
               f"{Fore.BLUE}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}"