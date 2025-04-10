"""
Desarrolla un programa que cumpla con los siguientes criterios:
1. Mostrar un Menú Interactivo:
o Al iniciar, el programa debe mostrar un menú en pantalla con al menos tres
opciones:
1. Mostrar un mensaje.
2. Mostrar una lista de nombres.
3. Salir del programa.
2. Captura y Procesamiento de la Opción:
o El usuario debe poder seleccionar una opción ingresando un número o palabra clave.
o El programa debe responder a la opción elegida ejecutando la acción
correspondiente:
 Si elige la opción "Mostrar mensaje", debe imprimirse en consola un
mensaje amigable o motivacional.
 Si elige "Mostrar nombres", se debe mostrar una lista predefinida de
nombres.
 Si elige "Salir", el programa debe finalizar mostrando un mensaje de
despedida.
3. Estructura de Control:
o Usa un bucle while para mantener el programa en ejecución mientras el usuario no
elija la opción de salir.
o Asegúrate de validar la entrada del usuario y mostrar un mensaje de error si la
opción no es válida.
"""

print( "Bienvenido a mi programa, espero que la pases bien, a continuación, el menú con las opciones que puedes realizar")
def cls():
    import os
    os.system('cls' if os.name=='nt' else 'clear')
def pausa(segundos):
    import time 
    time.sleep(segundos)
    
def Menu():
    print("Opción 1= Mostrar mensaje ") 
    print("Opción 2= Ver lista de nombres")
    print("Opción 3= Salir")    
    
def lista():
    Nombres=["Elvis", "Dylan", "Mynor","Alejandro"]
    print(Nombres)

def M_Mensaje():
    print("Fallar es la verdadera victoria, tu puedes :)")

def Salir():
    print("Hasta luego querido amigo")





while True:
    Menu()
    User=int(input("¿Cúal opción eliges? "))
    if User== 1:
        M_Mensaje()
        pausa(3)
        cls()
        
    elif User==2:
        lista()
        pausa(3)
        cls()
    
    elif User==3:
        Salir()
        pausa(3)
        cls()
        break
    
    else: 
        print("Esa opción no existe, por favor prueba de nuevo")
        pausa(3)
        cls()

