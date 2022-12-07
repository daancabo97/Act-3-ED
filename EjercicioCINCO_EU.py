# 5. Escribir un programa que me compare dos numeros y me diga cual es mayor

print("EJEMPLO CON UN DICCIONARIO -- 1 ") 
print("--------------------------------")
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

numeros = {"Num 1": num1, "Num 2": num2}

if num1 == num2:
    print("Los dos numeros son iguales")
elif num1 > num2:
    print(f'{num1} es mayor que {num2}')
else:
    print(f'{num2} es mayor que {num1}')    
    
# 5. Escribir un programa que me compare dos numeros y me diga cual es mayor 

print("\n")
print("EJEMPLO CON UN DICCIONARIO -- 2 ") 
print("--------------------------------")
numeros = {'X': 1265, 'Y': 413}

print(f'numeros:{numeros}')

print("--------------------------------")
mayor = max(numeros.keys(), key=lambda X: numeros[X])

print(f'El mayor es el numero {mayor}')

print("\n")