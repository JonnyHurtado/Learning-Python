#Creamos variable zoo que contiene lista de animales
zoo = ["lion", "tiger", "mamut", "elephant", "hypopotamus"] 

#Mientras los valores sean verdaderos
while True:

    #En cada iteración del bucle, se toma el último elemento de la lista zoo utilizando el método pop(). 
    # El elemento retirado se asigna a la variable animal.
    animal = zoo.pop() 

    #Imprime el elemento retirado de la lista.
    print (animal)

    #Este IF finalizara el ciclo si es encontrado el elemento "tiger".
    #Si animal es igual a tiger, rompe con break el cliclo while.
    if animal == "tiger":
        break

    #imprime el resultado de como va quedando la lista
    print(zoo)