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

print("Bienvenido a la página de nike CR")

datos={
    "producto":"Zapatillas",
    "Talla":42,
    "Color": "Negro",
    "Stock": 90
}

Claves=datos.keys() 
print(Claves)
Claves2=datos.values()


datos["Talla"]=input("Ingresa una talla nueva: ")
print(Claves2)