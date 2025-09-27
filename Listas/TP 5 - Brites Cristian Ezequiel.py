# ============================================================================================
# Trabajo Practico 5 - Listas
# Alumno = Cristian Ezequiel Brites
# Dni = 44.148.302
# ============================================================================================

# =====================================================
# Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
# =====================================================

# Lista con 10 notas de estudiantes
notas = [8, 6, 5, 7, 8.5, 9, 10, 7, 9.5, 3]
# Obtiene cantidad de notas para detener el bucle
cantidad_notas = len(notas) 
# Acumula notas para sacar promedio
suma_notas = 0 
mayor_nota = notas[0] # Inicializa con la primer nota para comparar
menor_nota = notas[0] # # Inicializa con la primer nota para comparar
for i in range(cantidad_notas):
    print(f"Nota {i}: {notas[i]}") # Imprime la lista completa nota por nota
    suma_notas += notas[i] # Acumula todas las notas
    if notas[i] >= mayor_nota: # Compara cada nota para obtener la mayor
        mayor_nota = notas[i]
    elif notas[i] < menor_nota: # Compara cada nota para obtener la menor
        menor_nota = notas[i]
# Imprime por pantalla la nota más alta, más baja y el promedio
print(f"Nota mas alta: {mayor_nota}")
print(f"Nota mas baja: {menor_nota}")
print(f"Promedio: {suma_notas / cantidad_notas}")

# =====================================================
# Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
# =====================================================
productos = []

# Cargar 5 productos
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

# Ordenar alfabéticamente (ignorar mayúsculas/minúsculas)
productos_ordenados = sorted(productos, key=str.lower)

# Mostrar lista ordenada
print("\nLista ordenada de productos:")
for i, producto in enumerate(productos_ordenados, start=1):
    print(f"{i}. {producto}")

# Pedir qué producto eliminar (por número en la lista)
opcion = int(input("\n¿Qué producto desea eliminar? (1, 2, 3, etc): "))

# Eliminar producto usando pop (ajustando índice)
eliminado = productos_ordenados.pop(opcion - 1)
print(f"\nSe eliminó: {eliminado}")

# Muestra lista actualizada
print("\nLista actualizada:")
for i, producto in enumerate(productos_ordenados, start=1):
    print(f"{i}. {producto}")

# =====================================================
# Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
# =====================================================

import random
numeros = []
numeros_pares = []
numeros_impares = []
# Genera una lista con  15 números enteros al azar entre 1 y 100
for i in range(1,16):
    numeros.append(random.randint(1, 100))
# Recorre la lista y separa pares de impares
for i, numero in enumerate(numeros):
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
# Imprime en pantalla cantidad de pares e impares y la lista completa
print("Lista completa:", numeros)
print(f"Cantidad de números pares: {len(numeros_pares)}")
print(f"Cantidad de números impares: {len(numeros_impares)}")

# =====================================================
# Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
# =====================================================

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetir = []
# Recorre la lista y crea una nueva sin valores repetidos
for i, dato in enumerate(datos):
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)

# Muestra lista actualizada
print("\nLista actualizada:")
for i, dato in enumerate(datos_sin_repetir):
    print(f"{dato}")

# =====================================================
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# •Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# •Mostrar la lista final actualizada.
# =====================================================

estudiantes = ["Ezequiel", "Cristian", "Hernesto", "Milagros", "Camila", "Rocio", "Magali", "Carlos"]

opcion = int(input("¿Qué opción desea realizar?\n1= Eliminar estudiante\n2= Agregar estudiante\n"))

if opcion == 1:
    print("\nSeleccione el estudiante a eliminar (por número):")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i}: {estudiante}")
    
    eliminar = int(input("Número del estudiante: "))
    
    if 0 <= eliminar < len(estudiantes):
        eliminado = estudiantes.pop(eliminar)
        print(f"\nSe eliminó: {eliminado}")
    else:
        print("Índice inválido.")

elif opcion == 2:
    estudiante = input("\nNombre del estudiante que desea agregar: ")
    estudiantes.append(estudiante)
    print(f"\nSe agregó: {estudiante}")

# Mostrar lista final
print("\nLista de estudiantes actualizada:")
for i, estudiante in enumerate(estudiantes):
    print(f"{i}: {estudiante}")

# =====================================================
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).
# =====================================================

numeros = [1, 5, 7, 8, 4, 5, 9] # Lista con 7 numeros aleatorios
numeros = [numeros[-1]] + numeros[:-1] # Rota los numeros
print("Lista rotada:", numeros)

# =====================================================
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
# =====================================================

# Matriz con temperaturas minimas y maximas de una semana
temperaturas = [
    [12, 22],
    [9, 18],
    [18, 25],
    [22, 35],
    [15, 28],
    [12, 27],
    [14, 26]
]

minimas = [fila[0] for fila in temperaturas] # Lista con temperaturas minimas
maximas = [fila[1] for fila in temperaturas] # Lista con temperaturas maximas
# Lista con las amplitudes por dia
amplitudes = [fila[1] - fila[0] for fila in temperaturas] 

mayor_amplitud = max(amplitudes) # Guarda la mayor amplitud
dia_mayor_amplitud = amplitudes.index(mayor_amplitud)+1  # Guarda el dia que se registro mayor amplitud + 1 porque los dias comienzan en 1

promedio_min = sum(minimas) / len(minimas) # Calcula promedio temperaturas minimas
promedio_max = sum(maximas) / len(maximas) # Calcula promedio temperaturas maximas

print(f"Promedio de mínimas: {promedio_min:.2f}")
print(f"Promedio de máximas: {promedio_max:.2f}")
print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C en el día {dia_mayor_amplitud}")

# =====================================================
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia
# =====================================================

notas = [
    [8, 7.5, 9],
    [9, 9.5, 8],
    [7, 5, 8],
    [5, 8, 9.5],
    [6, 7, 8.5]
]
# Promedio por estudiante 
print("Promedio por estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio = sum(fila) / len(fila)
    print(f"Estudiante {i}: {promedio:.2f}")

# Promedio por materia 
print("\nPromedio por materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    columna = [fila[j] for fila in notas]  # extraer la materia j de todos los estudiantes
    promedio = sum(columna) / len(columna)
    print(f"Materia {j+1}: {promedio:.2f}")

# =====================================================
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.
# =====================================================

# Crear tablero vacío
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

print("Bienvenido al juego Ta-Te-Ti")
print("Este es el tablero inicial:")

# Mostrar tablero inicial
for fila in tablero:
    print(" ".join(fila))
print()

# Bucle de turnos (máx 9 jugadas)
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")

    # Pedir fila y columna
    fila = int(input("Ingrese la fila (1-3): ")) - 1
    columna = int(input("Ingrese la columna (1-3): ")) - 1

    # Verificar casilla libre
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("⚠ Casilla ocupada, pierdes el turno.")

    # Mostrar tablero después de la jugada
    for fila in tablero:
        print(" ".join(fila))
    print()

