#El siguiente algoritmo resuelve el problema oara realizar la suma o multiplicacion de dos numeros

a = 0 
b = 0
c = 0
a = float(input("Ingresde el primer numero:"))
b = float(input("Ingresde el segundo numero:"))
if a > 0 or b > 0 :
  print("Suma de numeros")
  c = a +b 
else : 
  print("Multiplicacion de numeros")
  c = a * b 

print("El resultado de la operacion es: " , c) 