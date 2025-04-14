import random

palabra = []
intento = []

def logica(palabra, intento):
    palabras = ["dedos", "manos", "torso", "silla", "llave", "mundo", "canto", "nieve", "lento", "campo", "plomo", "tigre", "brisa"]
    seguir_jugando = True

    while seguir_jugando:
        palabra.clear()
        intento.clear()
        palabraSecreta = palabras[random.randint(0, len(palabras) - 1)]
        palabra.extend(palabraSecreta)

        print("Si no encuentra la palabra, escriba la palabra VENCIDO")
        print("Tenés hasta 6 intentos para adivinar la palabra.")

        bandera = True        
        cantidad_intentos = 0

        while bandera and cantidad_intentos < 6: 
            intento.clear()
            numero_intento = cantidad_intentos + 1
            mensaje = f"Intento {numero_intento}/6 - Ingresa tu intento de 5 letras: "
            intentos = input(mensaje)

            if (intentos == "VENCIDO") or (intentos == "Vencido") or (intentos == "vencido"):
                        print("Te rendiste. La palabra era:", "".join(palabra))
                        break

            if len(intentos) != 5:
                print("El intento debe contener exactamente 5 letras.")
            else:
                intento.extend(intentos)
                cantidad_intentos += 1

                if intento == palabra:
                    print("Felicidades, has adivinado la palabra!")
                    bandera = False
                else:
                    for i in range(5):
                        if intento[i] == palabra[i]:
                            print(intento[i], "está en la palabra y en la posición correcta")
                        elif intento[i] in palabra:
                            print(intento[i], "está en la palabra pero en la posición incorrecta")
                        else:
                            print(intento[i], "no está en la palabra")

        if cantidad_intentos == 6 and intento != palabra:
            print("Se acabaron los intentos. La palabra era:", "".join(palabra))

        respuesta = input("Querés jugar de nuevo? SI/NO: ")
        if respuesta not in ("SI", "Si", "si"):
            seguir_jugando = False
            print("Gracias por jugar!")
        else:
            print("Comencemos de nuevo!")

# Ejecutar el juego
logica(palabra, intento)