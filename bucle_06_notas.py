'''Ejercicio 6: Análisis de notas de alumnos
Crea un programa que almacene en una lista las notas de un grupo de alumnos. Utiliza un
bucle for para recorrer la lista y:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.'''

notas = [5, 4, 7, 1, 7]
contador_alumno = 0
total = 0
nota_alta = 0
nota_baja = None

for i in notas:
    print(f"Nota: {i}")
    total += i
    
    if(i >= 5):
        contador_alumno += 1
    if(i > nota_alta):
        nota_alta = i
    if(nota_baja is None or i < nota_baja):
        nota_baja = i

print(f"Han aprobado: {contador_alumno}")
print(f"Media: {total/len(notas)}")
print(f"Nota mas alta: {nota_alta}")
print(f"Nota mas baja: {nota_baja}")