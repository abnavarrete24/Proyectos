#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
#Sino, decirle al usuario que no es vocal

letra = input("Ingrese una letra: ")

'''if letra.lower() == "a":
    print("Es vocal")
else:
    if letra.lower() == "e":
        print("Es vocal")
    else:
        if letra.lower() == "i":
            print("Es vocal")
        else: 
            if letra.lower() == "o":
                print("Es vocal")
            else:
                if letra.lower() == "u":
                    print("Es vocal")
                else:
                    print("No es vocal")'''

if letra.lower() in "aeiou":
    print("Es vocal")
else:
    print("NO es vocal")
