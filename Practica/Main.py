from Persona import Persona
from Lugar import Lugar
from Rol import Rol
from colorama import Fore, Style

class Main:
    @staticmethod
    def main():
        # Crear lugares
        lugar1 = Lugar("Cafetería Central", "Av. Principal 123", "1234-5678")
        lugar2 = Lugar("Biblioteca", "Av. Secundaria 456", "8765-4321")
        lugar3 = Lugar("Gimnasio", "Calle Deportes 789", "5555-5555")
        lugar4 = Lugar("Parque", "Calle Naturaleza 101", "9999-9999")

        # Crear personas
        persona1 = Persona("Andre", "Bran", Rol.ADMIN)
        persona1.agregar_lugar(lugar1)
        persona1.agregar_lugar(lugar2)

        persona2 = Persona("Ana", "Gómez", Rol.USUARIO)
        persona2.agregar_lugar(lugar3)
        persona2.agregar_lugar(lugar4)

        # Mostrar información
        print(persona1)
        persona1.mostrar_foto()  # Mostrar la foto seleccionada
        print("\n")
        print(persona2)
        persona2.mostrar_foto()  # Mostrar la foto seleccionada

# Ejecutar el programa
if __name__ == "__main__":
    Main.main()