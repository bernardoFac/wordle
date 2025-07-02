import random
import os

palabra = []
clubes = ("Milan", "River", "Inter", "Colon", "Union", "Velez", "Betis", "Roma", "Porto", "Genoa", "Celta", "Chelsea")  # 4, 5, 7
colores = ("verde", "negro", "beige", "grana", "rojo", "azul", "gris", "cyan", "amarillo")  # 4, 5, 7
paises = ("Chile", "Japon", "Qatar", "Nepal", "India", "Siria", "Perú", "Brasil", "España")  # 4, 5, 7

peliculas = ("Bambi", "Rocky", "Joker", "Mulan", "Cars", "Coco", "ToyStory", "Coraline")  # 4, 5, 7
animales = ("Panda", "Cebra", "Tigre", "Burro", "Koala", "Mono", "Gato", "Conejos", "Gallina")  # 4, 5, 7
comidas = ("Pizza", "Torta", "Asado", "Sushi", "Tacos", "Pollo", "Pan", "Fideos", "Empanada")  # 3, 5, 7

# Armamos el diccionario
categorias = {
    "clubes": clubes,
    "colores": colores,
    "paises": paises,
    "peliculas": peliculas,
    "animales": animales,
    "comidas": comidas
}


def generar_palabra_secreta(lista_palabras):
    return random.choice(lista_palabras).lower()


def seleccionar_categoria(palabras):
    nombre_categoria = ["Clubes", "Colores", "Países", "Peliculas", "Animales", "Comidas"]
    emojis = ["⚽", "🎨", "🌎", "🎬", "🐾", "🍔"]
    for i in range(len(palabras)):
        print(f"{i + 1}. {emojis[i]} {nombre_categoria[i]}")
    try:
        seleccion = int(input("Ingresa el número de la categoría que deseas jugar: ")) - 1
    except ValueError:
        seleccion = -1

    if seleccion < 0 or seleccion >= len(palabras):
        print("Selección inválida. Se elegirá una categoría aleatoria.")
        seleccion = random.randint(0, len(palabras) - 1)
    else:
        print(f"Has seleccionado la categoría: {nombre_categoria[seleccion]}")
        
    return palabras[seleccion]

def filtrar_palabras_por_dificultad(categorias, dificultad):
    if dificultad == "1":
        longitud = 4
    elif dificultad == "2":
        longitud = 5
    else:
        longitud = 7

    palabras_filtradas = []

    for lista in categorias.values():
        for palabra in lista:
            if len(palabra) == longitud:
                palabras_filtradas.append(palabra.lower())

    return palabras_filtradas


def mostrar_estado_letras(intento, palabra):
    estado = {}

    for i in range(len(intento)):
        letra = intento[i]
        if letra == palabra[i]:
            estado[i] = f"✅ {letra.upper()} está en la palabra y en la posición correcta"
        elif letra in palabra:
            estado[i] = f"🟡 {letra.upper()} está en la palabra pero en la posición incorrecta"
        else:
            estado[i] = f"❌ {letra.upper()} no está en la palabra"

    for i in estado:
        print(estado[i])

def pedir_dificultad():
    print("Seleccioná una dificultad:")
    print("1 - Fácil (4 letras)")
    print("2 - Media (5 letras)")
    print("3 - Difícil (7 letras)")
    dificultad = input("Elegí una opción (1/2/3): ")
    while dificultad not in ("1", "2", "3"):
        dificultad = input("Opción inválida. Elegí 1, 2 o 3: ")
    return dificultad


def intentos_disponibles(n, longitud):
    return input(f"({n + 1}/6) Ingresa tu intento de {longitud} letras o 'vencido' para dejar de jugar: ").lower()

def logica(palabras, intento, aciertos):
    palabraSecreta = generar_palabra_secreta(palabras)
    palabra.clear()
    palabra.extend(palabraSecreta)
    bandera = True
    intentos_realizados = 0
    gano = False

    while bandera and intentos_realizados < 6:
        intento.clear()
        intentos = intentos_disponibles(intentos_realizados, len(palabraSecreta))
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
                print("🎉 ¡Felicidades! Adivinaste la palabra secreta 🎉")
                gano = True
                bandera = False
            else:
                mostrar_estado_letras(intento, palabra)

    if not gano and intentos_realizados == 6:
        print("💀Alcanzaste el máximo de intentos. La palabra secreta era:", palabraSecreta)

    return palabra, intento, aciertos, gano, intentos_realizados

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
    dificultad = pedir_dificultad()

    longitud = 4 if dificultad == "1" else 5 if dificultad == "2" else 7
    palabras_filtradas = []
    for categoria in categorias.values():
        palabras_filtradas.append(tuple(p for p in categoria if len(p) == longitud))


    print("╔══════════════════════════════════════╗")
    print("║         🎉  BIENVENIDO A...          ║")
    print("║             🌟 WORDLE 🌟             ║")
    print("╚══════════════════════════════════════╝\n")
    nombre = input("Ingresa tu nombre: ")
    while True:
        try:
            dni = int(input("Ingresa tu dni: "))
            break
        except ValueError:
            print("El DNI debe ser un número.")
    aciertos = 0
    partidas = 0
    total_intentos_exitosos = 0
    victorias = 0

    while True:
        categoria = seleccionar_categoria(palabras_filtradas)

        if categoria:
            intento = []
            palabra, intento, aciertos, gano, intentos_realizados = logica(categoria, intento, aciertos)
            partidas += 1
            if gano:
                victorias += 1
                total_intentos_exitosos += intentos_realizados

        respuesta = input("¿Querés jugar de nuevo? SI/NO: ")
        if respuesta.lower() != "si":
            actualizarHistorial(dni, nombre, aciertos)
            print("\n🎮 Gracias por jugar a Wordle. ¡Hasta la próxima! 🎮")

            if partidas > 0:
                porcentaje = (victorias / partidas) * 100
                promedio = total_intentos_exitosos / victorias if victorias > 0 else 0
                print("Estadísticas:")
                print(f"Partidas jugadas: {partidas}")
                print(f"Victorias: {victorias}")
                print(f"Porcentaje de victorias: {porcentaje:.2f}%")
                print(f"Promedio de intentos por victoria: {promedio:.2f}")
            else:
                print("No se jugaron partidas.")

            leerHistorial()
            break

if __name__ == "__main__":
    jugar()
