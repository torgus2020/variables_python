#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....
    suma = numero_1 + numero_2
    # Imprimir en pantalla el resultado de la suma
    # print(....)
    print(suma)
    print("el resultado de la suma es:", suma)
    # Repita el procedimiento para realizar la resta
    resta = numero_2 - numero_1
    print(resta)
    print("el resultado de la resta es:", resta)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print(numero_1, numero_2)
    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma= numero_2 + numero_1
    print(suma)
    print("el resultado de sumar", numero_1, "y", numero_2, "es:", suma)
    # Resta
    resta= numero_2 - numero_1
    print(resta)
    print("el resultado de restar", numero_2, "y", numero_1, "es:", resta)
    # División
    division= numero_2 / numero_1
    print(division)
    print("el resultado de la división entre", numero_2, "y", numero_1, "es:", division)
    # Multiplicación
    multiplicacion= numero_1 * numero_2
    print(multiplicacion)
    print("el resltado de", numero_1, "*", numero_2, "es:", multiplicacion)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print(nombre, apellido)
    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo = nombre + " " + apellido
    print(nombre_completo)
    # Imprimir la cantidad de letras que posee su nombre completo
    nombre_completo_len = len("nombre_completo")
    print(nombre_completo, "tiene", nombre_completo_len, "caracteres")


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    caracter_inicial = palabra_1[0], palabra_2[0], palabra_3[0]
    print(caracter_inicial)
    print(palabra_1[0],palabra_2[0],palabra_3[0])


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    sub_text_1 = palabra_1[:3]
    print(sub_text_1)
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    palabra_2_len = len(palabra_2)
    sub_text_2 = palabra_2[palabra_2_len-3:]
    print(sub_text_2)
    # Formar una nueva palabra con los recortes solicitados
    sub_text_final = sub_text_1 + sub_text_2
    # Imprima en pantalla los resultados
    print(sub_text_1, sub_text_2)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
