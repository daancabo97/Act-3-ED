# 5. Escribir un programa que me compare dos numeros y me diga cual es mayor 

# EJEMPLO CON UN DICCIONARIO -- "EL EJERCICIO ASIGNADO POR LA PROFE"

numeros = {'X': 1265, 'Y': 413}

print(numeros)
print('--------------------------------')

mayor = max(numeros.keys(), key=lambda A: numeros[A])

print(f'El mayor es el numero {mayor}')


# MISMO EJEMPLO AHORA UTILIZANDO UNA LISTA  -- "EJERCICIO QUE QUERIA PROBAR CON UNA LISTA"

# numeros = [90, 25]
# min = max = numeros[0]
# for numero in numeros:
#     if numero < min:
#         min = numero
#     elif numero > max:
#         max = numero 
# print("El numero menor es " + str(min)) 
# print("El numero mayor es " + str(max))

