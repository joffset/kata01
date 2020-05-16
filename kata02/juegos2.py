

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad < 4:
    print("El precio de la entrada es 0")
elif edad <= 4 <= 18:
    print("El precio de la entrada es 5 euros")
else:
    print("El precio de la entrada es 10 euros.")