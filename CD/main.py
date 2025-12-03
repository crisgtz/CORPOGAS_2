from Registro_empleados import (
    guardar_entrada,
    cambiar_visibilidad_manual
)
from Consultar_enteradas import consultar_entradas
from Grafica import menu_graficas
from Registro_empleados import menu_configurar_horarios  # menú de turnos
from Login import registrar_usuario, iniciar_sesion

def menu_principal():
    # Primero, pedir al usuario que inicie sesión o se registre
    while True:
        print("=== Bienvenido al Sistema ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            if iniciar_sesion(usuario, contraseña):
                break
            else:
                print("Credenciales incorrectas. Intenta de nuevo.")
        elif opcion == "2":
            usuario = input("Nuevo usuario: ")
            contraseña = input("Nueva contraseña: ")
            registrar_usuario(usuario, contraseña)
            print("Registro completado. Ahora puedes iniciar sesión.")
        elif opcion == "3":
            print("Saliendo del sistema...")
            return

        else:
            print("Opción no válida, intenta de nuevo.")

    # Una vez que el usuario esté autenticado, mostramos el menú principal
    while True:
        print("\n=== SISTEMA DE ENTRADAS DE EMPLEADOS ===")
        print("1. Registrar entrada de empleado")
        print("2. Consultar entradas")
        print("3. Ver gráficas")
        print("4. Configurar horarios de turnos")
        print("5. Cambiar visibilidad V/F de un registro")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            empleado = input("Empleado: ")
            print("\nSelecciona el turno:")
            print("1. Turno 1")
            print("2. Turno 2")
            print("3. Turno 3")

            turno = input("Turno (1-3): ")
            fecha_hora = input("Fecha y hora de entrada (AAAA-MM-DD HH:MM:SS): ")

            guardar_entrada(empleado, turno, fecha_hora)

        elif opcion == "2":
            consultar_entradas()

        elif opcion == "3":
            menu_graficas()

        elif opcion == "4":
            menu_configurar_horarios()

        elif opcion == "5":
            print("\n--- CAMBIAR VISIBILIDAD DEL REGISTRO ---")
            print("1. Cambiar a V (Visible)")
            print("2. Cambiar a F (Oculto)")

            sub = input("Elige una opción: ")

            if sub not in ["1", "2"]:
                print("Opción inválida.")
                continue

            try:
                reg = int(input("ID del registro a modificar: "))
                nuevo_valor = "V" if sub == "1" else "F"
                cambiar_visibilidad_manual(reg, nuevo_valor)
            except:
                print("ID inválido.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()