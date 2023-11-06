import argparse

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
parser.add_argument('-n1', '--numero1', type=int, help='Primer operador')
parser.add_argument('-n2', '--numero2', type=int, help='Segundo operador')
args = parser.parse_args()

print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = args.operacion # input("Indique una opción (1/2/3/4): ")
num1 = args.numero1
num2 = args.numero2
#num1 = float(input("Primer número: "))
#num2 = float(input("Segundo número: "))

print(opcion)

if opcion == '1':
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == '2':
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == '3':
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == '4':
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opción inválida")