# Lista donde se guardan los estudiantes
estudiantes = []


def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def evaluar_estado(promedio):

    if promedio >= 4:
        return "Aprobado"
    elif promedio >= 3:
        return "En recuperación"
    else:
        return "Reprobado"


def registrar_estudiante():

    print("\n--- Registro de estudiante ---")

    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))

    n1 = float(input("Ingrese la nota 1 (0 a 5): "))
    n2 = float(input("Ingrese la nota 2 (0 a 5): "))
    n3 = float(input("Ingrese la nota 3 (0 a 5): "))

    promedio = calcular_promedio(n1, n2, n3)
    estado = evaluar_estado(promedio)

    print("\n===== RESULTADO DEL ESTUDIANTE =====")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Nota 3:", n3)
    print("Promedio:", round(promedio,2))
    print("Estado académico:", estado)

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio,
        "estado": estado
    }

    estudiantes.append(estudiante)


def mostrar_estudiantes():

    print("\n===== LISTADO DE ESTUDIANTES =====")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    for i, est in enumerate(estudiantes, start=1):

        print(
            f"{i}. {est['nombre']} - "
            f"Edad: {est['edad']} - "
            f"Promedio: {est['promedio']:.2f} - "
            f"Estado: {est['estado']}"
        )


# MENÚ
while True:

    print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")