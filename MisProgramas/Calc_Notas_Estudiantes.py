while True:
    # Pide al profesor cuántas notas va a registrar
    num_notas = int(input("Ingrese la cantidad de notas a registrar: "))

    # Registra las notas que el profesor ingrese por teclado y calcula el promedio
    total_notas = 0
    for i in range(num_notas):
        nota = float(input("Ingrese la nota {}: ".format(i + 1)))
        total_notas += nota

    # Calcula el promedio de las notas ingresadas
    promedio = total_notas / num_notas

    # Imprime el resultado según las condiciones dadas
    if promedio < 3:
        print(f"El estudiante reprobó. Nota {promedio}")
    elif promedio >= 3 and promedio < 4:
        print(f"El estudiante aprobó con el mínimo permitido. Nota {promedio}")
    elif promedio >= 4 and promedio < 5:
        print(f"El estudiante aprobó con buen promedio. Nota {promedio}")
    else:
        print(f"El estudiante aprobó con excelencia. Nota {promedio}")

    # Pregunta al usuario si desea calcular las notas de otro estudiante o finalizar el programa
    opcion = input("¿Desea calcular las notas de otro estudiante? (s/n): ")
    if opcion.lower() != 's':
        break  # Si la respuesta no es 's', finaliza el bucle y el programa.
