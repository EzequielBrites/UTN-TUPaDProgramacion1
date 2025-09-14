# ============================================================================================
# Trabajo Practico 4 - Estructuras Repetitivas
# Alumno = Cristian Ezequiel Brites
# Dni = 44.148.302
# ============================================================================================

# =====================================================
# Ejercicio 1 
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# =====================================================

# Creamos un ciclo for que se repita de 0 a 100 
for i in range(0,101,1): 
    print(i) # imprime el contador del ciclo 

# =====================================================
# Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
# =====================================================

numero = int(input("Ingrese un número entero"))
contador = 0
n = abs(numero) # abs() devuelve su valor positivo en caso de que sea número negativo

if numero == 0: # controla si el usuario ingresa el número 0
    contador = 1
else:
    while n > 0:
        n //= 10 # elimina el último dígito
        contador += 1

print(f"El numero {numero} tiene {contador} digitos")  #Mostramos en pantalla el resultado

# =====================================================
# Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
# =====================================================

numMinimo = int(input("Ingrese el número minimo"))
numMaximo = int(input("Ingrese el número máximo"))
acumulador = 0

# Controlamos que numMinimo sea el menor y numMaximo el mayor
if numMinimo > numMaximo:
    numMinimo, numMaximo = numMaximo, numMinimo # intercambiamos si estan invertidos

for i in range(numMinimo + 1, numMaximo): # Recorre los números entre los dos valores
    acumulador += i # Suma los valores 

print(f"La suma de los valores comprendidos entre {numMinimo} y {numMaximo} es: {acumulador}") #Muestra el resultado en pantalla

# =====================================================
# Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
# =====================================================

corte = 0
acumulador = 0
contador = 0
num = int(input("Ingrese un número entero"))
while num != corte:
    acumulador += num
    contador += 1
    num = int(input("Ingrese otro número entero"))
if contador == 0:
    print("No se ingresaron números")
else:
    print(f"El total acumulado fue : {acumulador}")

# =====================================================
# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
# =====================================================

import random

numero = int(input("Adivina el número entre 0 y 9"))
# Validar primer ingreso
while numero < 0 or numero > 9:
    numero = int(input("Número inválido, ingrese entre 0 y 9: "))

contador = 0
aleatorio = random.randint(0, 9) # Genera numero aleatorio entre 0 y 9

while numero != aleatorio:
    contador += 1
    numero = int(input("Incorrecto, intenta otra vez (0-9): "))
    # Validar cada intento
    while numero < 0 or numero > 9:
        numero = int(input("Número inválido, ingrese entre 0 y 9: "))

contador += 1 # Suma el ultimo intento
print(f"Correcto! el número aleatorio era {aleatorio} utilizó {contador} intentos")

# =====================================================
# Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
# =====================================================

for i in range(100,-1,-1): # Recorre valores del 100 al 0 inclusive de manera decreciente
    if i % 2 == 0: # Verifica si el número es par
        print(i) # Imprime el número en caos que sea par

# =====================================================
# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
# =====================================================

numMinimo = 0
numMaximo = int(input("Ingrese un número entero positivo"))
acumulador = 0

# Verifica si el número es mayor que 0
if numMaximo > 0:
    for i in range(numMinimo,numMaximo+1): # Recorre los números entre los dos valores
        acumulador += i # Suma los valores 
else:
    print("El número ingresado no es valido")

print(f"La suma de los valores comprendidos entre {numMinimo} y {numMaximo} es: {acumulador}") #Muestra el resultado en pantalla

# =====================================================
# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.
# =====================================================

pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(1,101): # Permite ingresar 100 números en bucle
    num = int(input(f"Ingrese el número entero n°{i}: "))
    if num % 2 == 0: # Valida si es par
        pares += 1
    else:
        impares += 1

    if num > 0: # Valida si es positivo 
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares} impares: {impares} positivos: {positivos} negativos: {negativos}")

# =====================================================
# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.
# =====================================================

acumulador = 0

for i in range(1,101):
    num = int(input(f"Ingrese el número entero n°{i}: "))
    acumulador += num

print(f"La media de los valores ingresados es : {acumulador/100}")

# =====================================================
# Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
# =====================================================

num = int(input("Ingrese un número entero: "))

# Convertimos a cadena, invertimos con slicing y volvemos a entero
num_invertido = int(str(num)[::-1])

print(f"El número invertido es: {num_invertido}") # Mostramos en pantalla el número invertido