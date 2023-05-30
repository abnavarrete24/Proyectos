#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
#El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocalMinuscula = input("Ingrese una vocal en minúscula: ")
consonante = input("Ingrese una consonante en mayuscula: ")

vocalMinuscula = vocalMinuscula.upper()
consonante = consonante.lower()

print("La consonante fue: {} \nLa vocal fue {}". format(consonante, vocalMinuscula))

#print(format((letraMayuscula.lower(),vocalMinuscula.upper())))

