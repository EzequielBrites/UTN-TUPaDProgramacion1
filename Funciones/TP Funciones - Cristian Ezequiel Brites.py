# ============================================================================================
# Trabajo Practico - Funciones en python
# Alumno = Cristian Ezequiel Brites
# Dni = 44.148.302
# Comisión = 2
# ============================================================================================

# =====================================================
# Ejercicio 1 
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
# =====================================================

#crea funcion que imprime 'hola mundo'
def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo() # Llama a la función

# =====================================================
# Ejercicio 2
# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
# =====================================================

# funcion que recibe por parametro un nombre y devuelve un saludo personalizado
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

saludar_usuario(input("Ingrese su nombre: ")) # Llama a la función

# =====================================================
# Ejercicio 3
# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
# =====================================================

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(input("Ingrese su nombre "),
                    input("Ingrese su apellido "),
                    input("Ingrese su edad "),
                    input("Ingrese su residencia "))

# =====================================================
# Ejercicio 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
# =====================================================

import math # Importamos el modulo math para usar constante pi

def calcular_area_circulo(radio):
    return math.pi * radio**2 #Devuelve el area

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio #Devuelve el perimetro 

radio = int(input("Ingrese el radio de un circulo en cm "))
print(f"El área del circulo es {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)}")

# =====================================================
# Ejercicio 5
# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función..
# =====================================================

def segundos_a_horas(segundos):
    return segundos / 3600 #Devuelve cantidad de horas

segundos_a_horas(int(input("Ingrese la cantidad de segundos")))

# =====================================================
# Ejercicio 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
# =====================================================

def tabla_multiplicar(numero):
    for i in range(1,11): #multiplica el numero del 1 al 10 y a la vez imprime el resultado
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(int(input("Ingrese el número para obtener tabla de multiplicar")))

# =====================================================
# Ejercicio 7
# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
# =====================================================

def operaciones_basicas(a, b): # Devuelve suma, resta, multiplicacion y division de 2 numeros ingresados por parametro
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} x {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

operaciones_basicas(int(input("Ingrese el primer numero")),
                    int(input("Ingrese el segundo numero")))

# =====================================================
# Ejercicio 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# =====================================================

def calcular_imc(peso, altura): # Devuelve el IMC segun el peso y altura ingresados
    print(F"IMC = {peso / altura**2}")

peso = float(input("Ingrese el peso en kg"))
altura = float(input("Ingrese la altura en m"))
calcular_imc(peso,altura)

# =====================================================
# Ejercicio 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
# =====================================================

def celsius_a_fahrenheit(celsius): # Devuelve la temperatura en grados fahrenheit
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius_a_fahrenheit(float(input("Ingrese la temperatura en celsius (C°)")))

# =====================================================
# Ejercicio 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
# =====================================================

def calcular_promedio(a, b, c): # Devuelve el promedio de los 3 numeros ingresados
    promedio = (a + b + c) / 3
    return promedio

calcular_promedio(float(input("Ingrese el primer numero")),
                float(input("Ingrese el segundo numero")),
                float(input("Ingrese el tercer numero")))
