# ============================================================================================
# Trabajo Practico 3 - Estructuras Condicionales
# Alumno = Cristian Ezequiel Brites
# Dni = 44.148.302
# ============================================================================================

# =====================================================
# Ejercicio 1 
# Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
# =====================================================

# El usuario ingresa su edad por teclado y la guardamos en la variable edad
edad = int(input("Ingrese su edad"))
# Creamos una variable con la mayoria de edad actual
mayoriaEdad = 18
# Con un if evaluamos si es mayor de edad
if edad >= mayoriaEdad:
    print("Es mayor de edad")

# =====================================================
# Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
# =====================================================

# El usuario ingresa su nota por teclado y la guardamos en la variable nota
nota = int(input("Ingrese su nota"))
# Creamos una variable con la nota necesaria para aprobar
notaAprobar = 6
# Verificamos si esta en condicion de aprobado o no
if nota >= notaAprobar:
    print("Aprobado")
else:
    print("Desaprobado")

# =====================================================
# Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# =====================================================

# El usuario ingresa su un número por teclado y lo almacenamos en la variable num
num = int(input("Ingrese un número"))

#Verificamos si el número ingresado es par o no
if (num % 2) == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# =====================================================
# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.
# =====================================================

# El usuario ingresa su edad por teclado y la guardamos en la variable edad
edad = int(input("Ingrese su edad"))
# Creamos variables con la edad máxima para cada categoria
ninio = 12
adolescente = 18
adultoJoven = 30
# Verificamos en que categoria se encuentra la edad ingresada
if edad < ninio:
    categoria = "Niño/a"
elif edad >= ninio and edad < adolescente:
    categoria = "Adolescente"
elif edad >= adolescente and edad < adultoJoven:
    categoria = "Adulto/a Joven"
else:
    categoria = "Adulto/a mayor"

# Verificamos que se haya ingresado un número positivo e imprimimos por pantalla la categoria a la que pertenece la edad ingresada
if edad >= 0:
    print(f"Pertenece a la categoría: {categoria}")
else: 
    print("El número ingresado no es válido")

# =====================================================
# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# =====================================================

# Ingresa la contraseña por teclado y la almacenamos en la variable contraseña
contraseña = input("Ingrese su contraseña")
# Evaluamos si la contraseña cumple con las condiciones (entre 8 y 14 caracteres)
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# =====================================================
# Ejercicio 6
# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay 
# sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# =====================================================
import random
from statistics import mode, median, mean

# Creamos una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
numerosAleatorios = [random.randint(1,100) for i in range(50)]
# Calculamos el promedio, la media y la moda de nuestra lista
mediana = median(numerosAleatorios)
media = mean(numerosAleatorios)
moda = mode(numerosAleatorios)

# Mostramos la lista y los calculos
print("Lista:", numerosAleatorios)
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

# Evaluamos si hay sesgo positivo, negativo o no hay sesgo.
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo Negativo")
else:
    print("Sin sesgo")

# =====================================================
# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
# =====================================================

# Solicitamos al usuario una frase o palabra
palabra = input("Ingrese una frase o palabra")
# Evaluamos si el string ingresado termina en vocal 
if palabra[-1].lower() in "aeiou":
    palabra += "!"
# Imprimimos por pantalla el string 
print(palabra)

# =====================================================
# Ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
# =====================================================

# Solicitamos que el usuario ingrese su nombre
nombre = input("Ingrese su nombre por favor")

# Mostramos el menú de opciones al usuario
opcion = int(input(
    "Ingrese un número (1, 2, 3) según la opción que prefiere:\n"
    "1. Nombre en MAYÚSCULAS\n"
    "2. Nombre en minúsculas\n"
    "3. Nombre con la primera letra mayúscula\n"
    "Opción: "
))
# Según la opcion ingresada imprime el nombre 
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("El número ingresado es incorrecto")

# =====================================================
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# =====================================================

# Solicitamos al usuario una magnitud de terremoto
magnitud = float(input("Ingrese la magnitud del terremoto y obtenga la categoría según la escala Richter"))
# Seleccionamos la categoria correcta según la magnitud ingresada
if magnitud < 0:
    print("El número ingresado es inválido")
elif magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud <5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud <6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
else:
    categoria = "Muy Fuerte (puede causar daños significativos)"
# Si la magnitud ingresada es válida imprimimos por pantalla
if magnitud >= 0:
    print(f"La categoría de la magnitud {magnitud} es: {categoria}")

# =====================================================
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
# =====================================================

# Solicitamos al usuario en que hemisferio se encuentra
hemisferio = input("¿En que hemisferio (N/S) se encuentra?")
# Solicitamos al usuario su mes actual
mes = int(input("¿En que mes (1-12) del año se encuentra?"))
# Solicitamos al usuario dia actual
dia = int(input("¿En que dia (1-31) del mes se encuentra?"))

# Determinar la estación según el hemisferio
if hemisferio == "N":  # Hemisferio norte
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes < 6 and mes > 3) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes < 9 and mes > 6) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes < 12 and mes > 9) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":  # Hemisferio sur
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes < 6 and mes > 3) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes < 9 and mes > 6) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes < 12 and mes > 9) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print("La estación en su ubicación es:", estacion)