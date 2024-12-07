op = False
User = "Jaero"
Password = "OneTwoThree"
Failures = 0

while op != True :

    user1 = input("Ingresa tu usuario: ")
    password1 = input("Ingresa tu contraseña: ")
    if user1 == User and password1 == Password:
        print("Acceso concedido")
        op = True
    else:
        print("Usuario o contraseña incorrectos") 
        if Failures == 3:
            break
    Failures += 1