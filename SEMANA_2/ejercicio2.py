def filtrar_aprobados(calificaciones):
    aprobados = []
    contador = 0
    for i in range(len(calificaciones)):
        if contador % 2 != 0:
            if calificaciones[i] >= 3:
                aprobados.append(calificaciones[i])
        contador += 1
    return aprobados


def ejecutar():
    datos = input("ingrese las notas separadas por espacio: ").split(" ")
    calificaciones = []
    contador = 0
    for valor in datos:
        if contador % 2 != 0:
            calificaciones.append(float(valor))
        else:
            calificaciones.append(valor)
        contador += 1
    resultado = filtrar_aprobados(calificaciones)
    print("las notas que aprobaron son:", resultado)
ejecutar()
