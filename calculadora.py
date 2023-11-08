import argparse
import os

# suma de 2 números
def suma(num1, num2):
    return num1 + num2

# resta de 2 números
def resta(num1, num2):
    return num1 - num2

# multiplicacion de 2 números
def multiplicacion(num1, num2):
    return num1 * num2

# división de 2 números
def division(num1, num2):
    return num1 / num2
 
parser = argparse.ArgumentParser(description='Calculadora recibiendo parámetros')
parser.add_argument('-o', '--operacion', help='Tipo de Operacion')
parser.add_argument('-n1', '--numero1', help='Primer operador')
parser.add_argument('-n2', '--numero2', help='Segundo operador')
args = parser.parse_args()
    
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = args.operacion 
num1 = args.numero1
num2 = args.numero2

if isinstance(num1, int) and isinstance(num2, int):
    num1 = int(num1)
    num2 = int(num2)
    print(f'Operación: {opcion}')
    print(f'Operador 1: {num1}')
    print(f'Operador 2: {num2}')
else:
    num1 = 0
    num2 = 0

if num1 == 0 and num2 == 0:
    opcion = os.environ['operacion']
    num1 = int(os.environ['operador1'])
    num2 = int(os.environ['operador2'])

    print(f'Operación: {opcion}')
    print(f'Operador 1: {num1}')
    print(f'Operador 2: {num2}')

if opcion == '1':
    print("Opcion elegida Suma")
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == '2':
    print("Opcion elegida Resta")
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == '3':
    print("Opcion elegida Multiplicación")
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == '4':
    print("Opcion elegida División")
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opción inválida")