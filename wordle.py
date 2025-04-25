import random

palabra = []
intento = []
clubes=["Milan", "River", "Inter", "Colon", "Union", "Vélez", "Betis","Porto","Genoa","Celta"]
colores=[ "verde", "negro","beige","grana"]
paises=["Chile", "Japon", "Qatar", "Nepal", "India", "Siria"]	
palabras = [clubes, colores, paises]

def seleccionar_categoria(palabras):
    for i in range(len(palabras)):
        nombre_categoria = ["Clubes", "Colores", "Países"]
        print(f"{i + 1}. {nombre_categoria[i]}")    
    seleccion = int(input("Ingresa el número de la categoría que deseas jugar: ")) - 1
    if seleccion < 0 or seleccion >2:
        print("Selección inválida. Se elegirá una categoría aleatoria.")
        seleccion = random.randint(0, len(palabras) - 1)
    else:
        print(f"Has seleccionado la categoría: {palabras[seleccion]}")
        
    return palabras[seleccion]

def logica(palabras, intento):
    palabraSecreta = palabras[random.randint(0, len(palabras) - 1)].lower()
    palabra.clear()
    palabra.extend(palabraSecreta)
    bandera=True        
    while bandera: 
                intento.clear()
                intentos=str(input("Ingresa tu intento de 5 letras o vencido para dejar de jugar: ")).lower()
                
                if intentos == "vencido":
                        print("La palabra secreta era: ", palabraSecreta)
                        bandera=False
                if len(intentos)!=5:
                        print("El intento debe contener exactamente 5 letras.")
                else:
                        intento.clear()
                        intento.extend(intentos) 
                
                        if intento==palabra:
                                print("Felicidades, has adivinado la palabra!")
                                bandera=False
                        else:
                                for i in range(5):
                                        if intento[i] == palabra[i]:
                                                print(intento[i], "está en la palabra y en la posición correcta")
                                        elif intento[i] in palabra:
                                                print(intento[i], "está en la palabra pero en la posición incorrecta")
                                        else:
                                                print(intento[i], "no está en la palabra")
    return palabra, intento 


def jugar():
    while True:
        categoria = seleccionar_categoria(palabras)
        if categoria:
            logica(categoria, intento)
        respuesta = input("¿Querés jugar de nuevo? SI/NO: ")
        if respuesta.lower() != "si":
            print("¡Gracias por jugar!")
            break

jugar()
