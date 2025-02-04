# programa para determinar el mayor y el menorde tres numeros

# pedir al usuario que ingrese tres numeros
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el primer numero: "))
num3 = float(input("ingrese el primer numero: "))

#terminar el mayor de los tres numeros
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
    
#determinar el menor de los tres numeros
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <=num3:
    menor = num2
else:
    menor = num3
    
# imprimir los resultados
print(f"el mayor de los tres numeros es: {mayor}")
print(f"el menor de los tres numeros es: {menor}")

