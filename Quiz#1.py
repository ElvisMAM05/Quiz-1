"""
Requerimientos del Programa
Tu programa debe cumplir con las siguientes funcionalidades:
1. Interacción con el Usuario:
o Solicita al usuario que ingrese la clave (key) del diccionario cuyo valor desea
modificar.
o Si la clave existe, permite al usuario ingresar un nuevo valor y actualiza dicha
entrada en el diccionario.
2. Visualización del Estado Actual:
o Una vez realizada la modificación, muestra en consola el diccionario actualizado,
reflejando los cambios realizados.

3. Eliminación de Elementos:
o Solicita al usuario que indique una clave a eliminar del diccionario.
o Si la clave existe, elimínala y muestra el diccionario final luego de la eliminación.
o En caso de que la clave no exista, informa al usuario que no se encontró la clave y
muestra el diccionario sin cambios.

4. Robustez:
o Asegúrate de manejar correctamente posibles errores, como claves inexistentes o
entradas vacías.
o El programa debe ser claro, intuitivo y fácil de usar, mostrando mensajes
informativos en cada paso del proceso.

"""

def cls():
    import os
    os.system('cls' if os.name=='nt' else 'clear')
def pausa(segundos):
    import time 
    time.sleep(segundos)
    
Clave=""
def Frases():
    print("Bienvenido a la página de nike CR, aquí puedes modificar las estadisticas de las Zapatillas")
    print("Las claves que puedes modificar son: producto, Talla, Color y Stock")
    print("Recuerda que debes ingresar la clave tal y como se muestra en el diccionario")
    print("Las claves son las siguientes: ")

datos={
    "producto":"Zapatillas",
    "Talla":42,
    "Color": "Negro",
    "Stock": 90
    }
    
while True:
    Frases()
    print("Talla")
    print("Color")
    print("Slock")
    
    User1=input("¿Que quieres hacer? borrar o editar? ")
    
    if User1=="editar":
        
            while True: 
                User=input("¡Que datos deseas editar?: ")
                if User in datos:
                    if User=="Talla":
                        datos["Talla"]=int (input("Cúal será la talla nueva? "))
                        print(datos)
                        pausa(3)
                        cls()
                    elif User=="Color":
                        datos["Color"]=input("Cúal será el color nuevo? ")
                        print(datos)
                        pausa(3)
                        cls()
                    elif User=="Slock":
                        datos["Stock"]=int (input("Stock? "))
                        print(datos)
                        pausa(3)
                        cls()
                    
                else: 
                    print(f"La clave {User} no existe, prueba de nuevo") 
                    pausa(3)
                    cls()
                    
    elif User1=="borrar":
        User=input("¡Que datos deseas borrar?: ")
        if User in datos:
            if User=="Talla":
                datos.pop('Talla')
                print(datos)
                pausa(3)
                cls()
            elif User=="Color":
                datos.pop('Color')
                print(datos)
                pausa(3)
                cls()
            elif User=="Stock":                
                datos.pop('Stock')
                print(datos)
                pausa(3)
                cls()
                
        else:
            print(f"La clave {User} no existe, prueba de nuevo") 
            pausa(3)
            cls()