import random

palabra = []
intento = []
clubes=("Milan", "River", "Inter", "Colon", "Union", "Vélez", "Betis","Porto","Genoa","Celta")
colores=("verde", "negro","beige","grana")
paises=("Chile", "Japon", "Qatar", "Nepal", "India", "Siria")	
palabras = (clubes, colores, paises)

def generar_palabra_secreta(palabras):
    """Selecciona una palabra secreta aleatoria en minúscula."""
    palabras_5_letras = [p for p in palabras if len(p) == 5]
    return random.choice(palabras_5_letras).lower()

def seleccionar_categoria(palabras):
    """Permite al jugador elegir una categoría o selecciona una aleatoria si la elección es inválida."""
    for i in range(len(palabras)):
        nombre_categoria = ["Clubes", "Colores", "Países"]
        print(f"{i + 1}. {nombre_categoria[i]}")    
    seleccion = int(input("Ingresa el número de la categoría que deseas jugar: ")) - 1
    if seleccion < 0 or seleccion >2:
        print("Selección inválida. Se elegirá una categoría aleatoria.")
        seleccion = random.randint(0, len(palabras) - 1)
    else:
        print(f"Has seleccionado la categoría: {nombre_categoria[seleccion]}")
        
    return palabras[seleccion]

def mostrar_estado_letras(intento, palabra):
    """Compara las letras del intento con la palabra y muestra su estado."""
    for i in range(5):
        if intento[i] == palabra[i]:
            print(intento[i], "está en la palabra y en la posición correcta")
        elif intento[i] in palabra:
            print(intento[i], "está en la palabra pero en la posición incorrecta")
        else:
            print(intento[i], "no está en la palabra")

intentos_disponibles = lambda n: input("(" + str(n + 1) + "/6) Ingresa tu intento de 5 letras o vencido para dejar de jugar: ").lower()


def logica(palabras, intento):
    """Ejecuta el núcleo del juego: elige una palabra secreta, gestiona los intentos del jugador y determina el resultado."""
    palabraSecreta = generar_palabra_secreta(palabras)
    palabra.clear()
    palabra.extend(palabraSecreta)
    bandera = True
    intentos_realizados = 0
    while bandera and intentos_realizados < 6:
        intento.clear()
        intentos = intentos_disponibles(intentos_realizados)

        if intentos == "vencido":
            print("La palabra secreta era:", palabraSecreta)
            bandera = False
        elif len(intentos) != 5:
            print("El intento debe contener exactamente 5 letras.")
        else:
            intentos_realizados += 1
            intento.extend(intentos)

            if intento == palabra:
                print("Felicidades, has adivinado la palabra!")
                bandera = False
            else:
                mostrar_estado_letras(intento, palabra)

    if intentos_realizados == 6:
        print("Alcanzaste el máximo de intentos. La palabra secreta era:", palabraSecreta)
    
    return palabra, intento


def jugar():
    """Inicia y administra el ciclo completo del juego, permitiendo múltiples partidas si el jugador lo desea."""
    while True:
        categoria = seleccionar_categoria(palabras)
        if categoria:
            logica(categoria, intento)
        respuesta = input("¿Querés jugar de nuevo? SI/NO: ")
        if respuesta.lower() != "si":
            print("¡Gracias por jugar!")
            break

jugar()
