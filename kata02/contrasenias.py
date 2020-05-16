
password = "contrasenia"

password_del_usuario = input("Introduzca la contrasenia: ")
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("el password es correcto")
else:
    print("el password no coincide")
