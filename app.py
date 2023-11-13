import random

print("============================================") 
print("|    Juego de piedra, papel o tijeras      |")
print("============================================\n") 

respuesta = "s"
counter_jugador = 0
counter_computadora = 0
counter_jugados = 0

while True:
    if respuesta == "n":
       break
    
    elif respuesta == "s":
        # Crear un arreglo con las opciones rock, paper y scissors, despues imprimir las opciones que el jugador puede elegir, despues preguntar al jugador que opcion quiere elegir, despues de que el jugador elija una opcion, si eligio una opcion diferente le debe de mostrar un mensaje opcion no valida, la computadora debe de elegir una opcion aleatoria
        opciones = ["rock", "paper", "scissors"]
        print("Opciones: ")
        for opcion in opciones:
            print(opcion)
        opcion_jugador = input("Que opcion quieres elegir?: ")
        if opcion_jugador not in opciones:
            print("\n!!!! Opcion invalida !!!!\n")
            continue
                    
        opcion_computadora = random.choice(opciones)
        # Despues de que el jugador y la computadora eligieron una opcion, se debe de comparar las opciones, si el jugador elige rock y la computadora elige scissors el jugador gana, si el jugador elige rock y la computadora elige paper la computadora gana, si el jugador elige rock y la computadora elige rock es un empate, la cantidad de veces que gana el jugador y la computadora se debe de guardar en una variable 
        if opcion_jugador == "rock":
            if opcion_computadora == "scissors":
                counter_jugador += 1
                print("Ganaste")
            elif opcion_computadora == "paper":
                print("Perdiste")
                counter_computadora += 1
            elif opcion_computadora == "rock":
                print("Empate")
                counter_jugador += 1
                counter_computadora += 1

        # si el jugador elige paper y la computadora elige rock el jugador gana, si el jugador elige paper y la computadora elige scissors la computadora gana, si el jugador elige paper y la computadora elige paper es un empate 
        elif opcion_jugador == "paper":
            if opcion_computadora == "rock":
                counter_jugador += 1
                print("Ganaste")
            elif opcion_computadora == "scissors":
                counter_computadora += 1
                print("Perdiste")
            elif opcion_computadora == "paper":
                print("Empate")
                counter_jugador += 1
                counter_computadora += 1  

        # si el jugador elige scissors y la computadora elige paper el jugador gana, si el jugador elige scissors y la computadora elige rock la computadora gana, si el jugador elige scissors y la computadora elige scissors es un empate
        elif opcion_jugador == "scissors":
            if opcion_computadora == "paper":
                counter_jugador += 1
                print("Ganaste")
            elif opcion_computadora == "rock":
                counter_computadora += 1
                print("Perdiste")
            elif opcion_computadora == "scissors":
                print("Empate")
                counter_jugador += 1
                counter_computadora += 1

        counter_jugados += 1
        
    else:
        print("\n!!!! Opcion invalida !!!!\n")
        respuesta = input("Quieres jugar de nuevo? (s/n): ")
        continue

    respuesta = input("Quieres jugar de nuevo? (s/n): ")

print("======================================================") 
print("| Score del jugador: " + str(counter_jugador) +" VS " +"Score de la computadora: " + str(counter_computadora)+" |") 
print("| Cantidad de veces jugadas: " + str(counter_jugados)+"                       |")
print("======================================================")       
print("**************** Gracias por jugar ******************")