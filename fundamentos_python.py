""" Hola mundo con python """
print("Hola Mundo!! Wiand1515")


""" Comentarios en Python """
# para realizar comentarios en una linea en python utilizamos("#")
""" y en caso de querer comentar,
mas de una linea,
utilizamos las triple comillas """

""" Variables en Python """
#Para asignar una variable en python simplemente la nombramos e igualamos al valor que queramos asignar

perro = "perro"
gato = "gato"
numero = 15

print(perro,gato,numero)

""" Concatenacion en Python """
#Utilizamos la concatenacion para unir dos variables en python se realiza de la siguiente manera

nombre = "Matias"
apellido = "Fuentes"

print(nombre + " " + apellido)

#con la siguiente sintaxis podemos utilizar la concatenacion como si fueran template strings de JS

print(f"{nombre} {apellido}")

#podemos de igual manera concatenar variables de la siguiente manera (utilizando metodo format)

print("{} {}".format(nombre,apellido))

""" Tipos de datos en Python """

nada = None
print(type(nada), nada)

string = "Soy un string y en python me llamo str"
print(type(string), string)

entero = 11
print(type(entero), entero)

decimal = 4.2 #llamado en python flotante
print(type(decimal), decimal)

booleano = True #este tipo de dato debe comenzar con mayuscula a diferencia de JS
print(type(booleano), booleano)

lista = [1,2.28,True,"perro"] #conocido como arrays en JS
print(type(lista), lista)

tupla = ("probando", "tipos de datos", "en Python") #Array que no varia
print(type(tupla), tupla)

diccionario = {
    "nombre": "Matias",
    "apellido": "Fuentes",
    "edad": 30,
    "vive": True,
} #es el equivalente a objetos en JS

print(type(diccionario), diccionario["nombre"])


