#Creamos variable zoo que contiene lista de animales
zoo = ["lion", "tiger", "mamut", "elephant", "hypopotamus"] 

#Mientras los valores sean verdaderos
while True:

    #En cada iteración del bucle, se toma el último elemento de la lista zoo utilizando el método pop(). 
    # El elemento retirado se asigna a la variable animal.
    animal = zoo.pop() 
    print (animal) #Imprime el elemento retirado de la lista.
    if animal == "mamut": #Este IF finalizara el ciclo si es encontrado el elemento "mamut".
        break #Si animal es igual a mamut, rompe con break el cliclo while.
    print(zoo) #imprime el resultado de como va quedando la lista

#Salida de datos:
#hypopotamus
#['lion', 'tiger', 'mamut', 'elephant']
#elephant
#['lion', 'tiger', 'mamut']
#mamut








#=============================================================
#=============================================================
suma = 0
numero = 1
while suma <= 10:
    suma += numero
    numero += 1
print("La suma es:", suma)
# Salida: La suma es: 15

#=============================================================
#=============================================================
numero = 1
while numero <= 10:
    if numero % 2 == 0:
        print(numero)
    numero += 1
# Salida: 2, 4, 6, 8, 10


#=============================================================
#=============================================================
edad = int(input("Ingrese su edad: "))
while edad < 0 or edad > 120:
    print("Edad inválida. Inténtelo de nuevo.")
    edad = int(input("Ingrese su edad: "))
print("Edad válida. Gracias.")