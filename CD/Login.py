import hashlib
import os


CARPETA = r"D:\crisg\GitHub\trabajo\CORPOGAS_2"

# Crear carpeta si no existe
os.makedirs(CARPETA, exist_ok=True)

# Archivo dentro de la carpeta
ARCHIVO_USUARIOS = os.path.join(CARPETA, "usuarios.txt")

# Comprobar si el archivo existe, y si no, crearlo
if not os.path.exists(ARCHIVO_USUARIOS):
    open(ARCHIVO_USUARIOS, "a").close()

def hash_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

def registrar_usuario(nombre_usuario, contraseña):
    hash_contra = hash_contraseña(contraseña)
    with open(ARCHIVO_USUARIOS, 'a') as archivo:
        archivo.write(f'{nombre_usuario},{hash_contra}\n')
    print("Usuario registrado exitosamente.")

def iniciar_sesion(nombre_usuario, contraseña):
    hash_contra = hash_contraseña(contraseña)
    try:
        with open(ARCHIVO_USUARIOS, 'r') as archivo:
            for linea in archivo:
                usuario, contra_hash = linea.strip().split(',')
                if usuario == nombre_usuario and contra_hash == hash_contra:
                    print("Inicio de sesión exitoso.")
                    return True
        print("Nombre de usuario o contraseña incorrectos.")
        return False
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return False

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario = input("Nuevo usuario: ")
            contraseña = input("Nueva contraseña: ")
            registrar_usuario(usuario, contraseña)

        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            iniciar_sesion(usuario, contraseña)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()