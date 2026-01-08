'''Ejercicio 6: Análisis de notas de alumnos
Crea un programa que almacene en una lista las notas de un grupo de alumnos. Utiliza un
bucle for para recorrer la lista y:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.'''
def notasAlumnos(notas):
    contador_alumno = 0

    for i in notas:
        if(i >= 5):
            contador_alumno += 1

    return contador_alumno

notas = [5, 4, 7, 1, 7]
print(f"Han aprobado: {notasAlumnos(notas)}")
