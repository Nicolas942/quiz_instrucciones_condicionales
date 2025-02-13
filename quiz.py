# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = int(input("Ingrese el valor correspondiente al primer lado de la figura: "))
b = int(input("Ingrese el valor correspondiente al Segundo lado de la figura: "))
c = int(input("Ingrese el valor correspondiente al tercer lado de la figura: "))

# processing

if a + b > c and a + c > b and b + c > a:
    r = 'Si se puede formar un triángulo'
else:
    r = '¡No se puede formar un triángulo!'

# output
print("--------------------------------")
print(r)
print("--------------------------------")