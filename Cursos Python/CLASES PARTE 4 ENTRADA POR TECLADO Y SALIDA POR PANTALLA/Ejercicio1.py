from math import sqrt
#SQRT: llama a una libreria math

a = int(input('Ingrese el valor de a:'))
b = int(input('Ingrese el valor de b:'))
c = int(input('Ingrese el valor de c:'))
#d = int(input('Ingrese el valor de d:'))

x1 = 0
x2 = 0

if ((b**2)-(4*a*c))<0:
    print("No se puede realizar porque no se puede sacar la raíz de ese número")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
print("La solución es: \nx1=",x1, "\nx2", x2)

#x = ((-b+(^b**2-4*a*c)))



