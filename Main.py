import random
import os

palabra = []
clubes = ("Milan", "River", "Inter", "Colon", "Union", "Velez", "Betis", "Porto", "Genoa", "Celta")
colores = ("verde", "negro", "beige", "grana")
paises = ("Chile", "Japon", "Qatar", "Nepal", "India", "Siria")	
palabras = [clubes, colores, paises]

nombre = input("Ingresa tu nombre: ")
dni = int(input("Ingresa tu dni: "))

def generar_palabra_secreta(palabras):
    palabras_5_letras = [p for p in palabras if len(p) == 5]
    return random.choice(palabras_5_letras).lower()

def seleccionar_categoria(palabras):
    nombre_categoria = ["Clubes", "Colores", "Países"]
    for i in range(len(palabras)):
        print(f"{i + 1}. {nombre_categoria[i]}")
    try:
        seleccion = int(input("Ingresa el número de la categoría que deseas jugar: ")) - 1
    except ValueError:
        seleccion = -1

    if seleccion < 0 or seleccion > 2:
        print("Selección inválida. Se elegirá una categoría aleatoria.")
        seleccion = random.randint(0, len(palabras) - 1)
    else:
        print(f"Has seleccionado la categoría: {nombre_categoria[seleccion]}")
        
    return palabras[seleccion]

def mostrar_estado_letras(intento, palabra):
    estado = {}

    for i in range(len(intento)):
        letra = intento[i]
        if letra == palabra[i]:
            estado[i] = f"{letra} está en la palabra y en la posición correcta"
        elif letra in palabra:
            estado[i] = f"{letra} está en la palabra pero en la posición incorrecta"
        else:
            estado[i] = f"{letra} no está en la palabra"

    for i in estado:
        print(estado[i])

intentos_disponibles = lambda n: input(f"({n + 1}/6) Ingresa tu intento de 5 letras o 'vencido' para dejar de jugar: ").lower()

def logica(palabras, intento, aciertos):
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
                aciertos += 1
                print("Felicidades, has adivinado la palabra!")
                bandera = False
            else:
                mostrar_estado_letras(intento, palabra)

    if intentos_realizados == 6:
        print("Alcanzaste el máximo de intentos. La palabra secreta era:", palabraSecreta)

    return palabra, intento, aciertos

def leerHistorial():
    ruta_actual = os.path.dirname(__file__)
    ruta_archivo = os.path.join(ruta_actual, "historial.csv")
    try:
        with open(ruta_archivo,"r") as file:
            for linea in file:
                linea=linea.strip()
                campos=linea.split(";")
                dni,nombre,aciertos=campos
                print(f"Nombre:{nombre}     DNI:{dni}      Aciertos:{aciertos}")
    except Exception as e:
        print(f"Ocurrio un error {e}")
    
def actualizarHistorial(dni,nombre,aciertos):
    ruta_actual = os.path.dirname(__file__)
    ruta_archivo = os.path.join(ruta_actual, "historial.csv")
    nuevas_lineas=[]
    jugadorEncontrado=False  
         
    try:
        with open(ruta_archivo,"r") as file:
            for linea in file:
                linea=linea.strip()
                campos=linea.split(";")
                dniV,nombreV,aciertosV=campos
                if dniV==str(dni):
                    jugadorEncontrado=True
                    if int(aciertosV)<aciertos:
                            nuevas_lineas.append(f"{dni};{nombre};{aciertos}\n")
                            print("Aciertos actualizados.")
                    else:
                        nuevas_lineas.append(linea+"\n")
                    continue
                nuevas_lineas.append(linea+"\n")
    except Exception as e:
        print(f"Ocurrio un error {e}")
    if not jugadorEncontrado:
        nuevas_lineas.append(f"{dni};{nombre};{aciertos}\n")
    try:
        with open(ruta_archivo,"w")as file:
            file.writelines(nuevas_lineas)
    except Exception as e:
        print(f"Ocurrio un error {e}")
            
                                            
            
def jugar():
    aciertos = 0
    while True:
        categoria = seleccionar_categoria(palabras)
        if categoria:
            intento = []  # Inicialización necesaria
            palabra, intento, aciertos = logica(categoria, intento, aciertos)
        respuesta = input("¿Querés jugar de nuevo? SI/NO: ")
        if respuesta.lower() != "si":
            actualizarHistorial(dni,nombre,aciertos)
            print("¡Gracias por jugar!")
            leerHistorial()
            break

jugar()
