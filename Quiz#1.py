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

print("Bienvenido a la página de nike CR, aquí puedes modificar las estadisticas de las Zapatillas")
print("Las claves que puedes modificar son: producto, Talla, Color y Stock")
print("Recuerda que debes ingresar la clave tal y como se muestra en el diccionario")



datos={
    "producto":"Zapatillas",
    "Talla":42,
    "Color": "Negro",
    "Stock": 90
}


def Funcion():
        Usuario_O=input("¿Quieres modificar o eliminar algún dato? (Escribe editar o borrar) ")

        while Usuario_O=="editar":
            User=input("¡Que datos deseas modificar?: ")

            datos["Talla"]= int(input("Cúal será la nueva talla? ")) if User=="Talla" else "Dato no existente"
            datos["Color"]=input("Cúal será el color nuevo? ") if User=="Color" else "Dato no existente"
            datos["Stock"]=int (input("Stock? ")) if User=="Stock" else ""

            Usuario_O=input("Quieres modificar otro dato? ")

        print(datos)
        
        while Usuario_O=="borrar":
            User=input("¡Que datos deseas borrar?: ")
            datos.pop('Talla') if User=="Talla" else "Dato no existente"
            datos.pop('Color') if User=="Color" else "Dato no existente"
            datos.pop('Stock') if User=="Stock" else "Dato no existente"

            Usuario_O=input("Quieres borrar otro dato? ")
        
        print(datos)


Funcion()


