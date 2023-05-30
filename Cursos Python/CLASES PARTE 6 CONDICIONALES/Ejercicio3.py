'''Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''

palabra1 = input("Ingresa la primer palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("NO riman, por que tienen menos de 3 carácteres")
elif palabra1[-3 : ]==palabra2[-3 : ]:
    print("Las palabras riman")
elif palabra1[-2 : ]==palabra2[-2 : ]:
    print("Las palabras riman")
else:
    print("Las palabras no riman")