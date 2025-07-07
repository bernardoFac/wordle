import random
import os


palabra = []
# Distintas listas que contienen a las palabras que conforman la categoria
clubes = ("Milan", "River", "Inter", "Colon", "Union", "Velez", "Betis", "Roma", "Porto", "Genoa", "Celta", "Chelsea", "Boca","Lanus", "Arsenal", "Lazio", "Napoli", "Ajax", "Santos", "Tigre")
colores = ("verde", "negro", "beige", "grana", "rojo", "azul", "gris", "cyan", "amarillo","blanco", "morado", "violeta", "celeste", "rosado")
paises = ("Chile", "Japon", "Qatar", "Nepal", "India", "Siria", "Peru", "Brasil", "España","Italia", "Francia", "Grecia", "Mexico", "Canada", "Egipto")
peliculas = ("Bambi", "Rocky", "Joker", "Mulan", "Cars", "Coco", "ToyStory", "Coraline","Avatar", "Titanic", "Batman", "Frozen", "Shrek")
animales = ("Panda", "Cebra", "Tigre", "Burro", "Koala", "Mono", "Gato", "Conejos", "Gallina","Perro", "Cabra", "Pato", "Zorro", "Caballo")
comidas = ("Pizza", "Torta", "Asado", "Sushi", "Tacos", "Pollo", "Pan", "Fideos", "Empanada","Hamburguesa", "Milanesa", "Ñoquis", "Ensalada", "Lentejas")


# Armamos el diccionario
categorias = {
    "clubes": clubes,
    "colores": colores,
    "paises": paises,
    "peliculas": peliculas,
    "animales": animales,
    "comidas": comidas
}

# Lista ordenada auxiliar para mantener orden fijo de las categorías
nombre_categoria = ["Clubes", "Colores", "Países", "Peliculas", "Animales", "Comidas"]
emojis = ["⚽", "🎨", "🌎", "🎬", "🐾", "🍔"]
palabras_ordenadas = [categorias["clubes"], categorias["colores"], categorias["paises"],
                      categorias["peliculas"], categorias["animales"], categorias["comidas"]]

# funcion para generar la palabra a adivinar
def generar_palabra_secreta(lista_palabras):
    return random.choice(lista_palabras).lower()

# funcion para que el usuario seleccione la categoria
def seleccionar_categoria(palabras):
    for i in range(len(palabras)):
        print(f"{i + 1}. {emojis[i]} {nombre_categoria[i]}")
    try:
        seleccion = int(input("Ingresa el número de la categoría que deseas jugar: ")) - 1
    except ValueError:
        seleccion = -1

    if seleccion < 0 or seleccion >= len(palabras):
        seleccion = random.randint(0, len(palabras) - 1)
        print(f"Selección inválida. Se elegirá una categoría aleatoria: {nombre_categoria[seleccion]}")
    else:
        print(f"Has seleccionado la categoría: {nombre_categoria[seleccion]}")
        
    return palabras[seleccion]

# funcion para que se filtre la palabra por dificultad dependiendo del largo
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

# funcion para que se muestre el estado de cada una de las letras ingresadas(adivinada, equivocada, posicion equivocado)
def mostrar_estado_letras(intento, palabra):
    estado = [""] * len(palabra)
    palabra_temp = list(palabra)  # copia para marcar letras usadas

    # 1. Verificar aciertos exactos
    for i in range(len(intento)):
        if intento[i] == palabra[i]:
            estado[i] = f"✅ {intento[i].upper()} está en la palabra y en la posición correcta"
            palabra_temp[i] = None  # marcar como usada

    # 2. Verificar letras correctas en posición incorrecta
    for i in range(len(intento)):
        if estado[i] == "" and intento[i] in palabra_temp:
            estado[i] = f"🟡 {intento[i].upper()} está en la palabra pero en la posición incorrecta"
            palabra_temp[palabra_temp.index(intento[i])] = None  # marcar como usada
        elif estado[i] == "":
            estado[i] = f"❌ {intento[i].upper()} no está en la palabra"

    for mensaje in estado:
        print(mensaje)
    return

# funcion para que el usuario seleccione la dificultad
def pedir_dificultad():
    print("Seleccioná una dificultad:")
    print("1 - Fácil (4 letras)")
    print("2 - Media (5 letras)")
    print("3 - Difícil (7 letras)")
    dificultad = input("Elegí una opción (1/2/3): ")
    while dificultad not in ("1", "2", "3"):
        dificultad = input("Opción inválida. Elegí 1, 2 o 3: ")
    return dificultad

# funcion para mostrar cantidad de ingresos restantes
def intentos_disponibles(n, longitud):
    return input(f"({n + 1}/6) Ingresa tu intento de {longitud} letras o 'vencido' para dejar de jugar: ").lower()

# funcion que se encarga de generar la palabra secreta y validar que no se llegue a la cantidad maxima de intentos
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
        elif len(intentos) != len(palabraSecreta):
            print(f"El intento debe contener exactamente {len(palabraSecreta)} letras.")
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

# lee y muestra el historial
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
  
# actualiza el historial agregando la ultima sesion  
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

# actualiza el ranking de los mejores 5 jugadores del juejo
def crearRanking():
    ruta_actual = os.path.dirname(__file__)
    ruta_historial = os.path.join(ruta_actual, "historial.csv")
    ruta_ranking = os.path.join(ruta_actual, "ranking.txt")

    jugadores = []

    try:
        with open(ruta_historial, "r") as file:
            for linea in file:
                dni, nombre, aciertos = linea.strip().split(";")
                jugadores.append({"dni": dni, "nombre": nombre, "aciertos": int(aciertos)})
    except Exception as e:
        print(f"No se pudo leer el historial: {e}")
        return

    jugadores.sort(key=lambda x: x["aciertos"], reverse=True)
    top_5 = jugadores[:5]

    print("🏆 TOP 5:")
    i = 1
    for jugador in top_5:
        print(f"{i}. {jugador['nombre']} (DNI: {jugador['dni']}) - Aciertos: {jugador['aciertos']}")
        i += 1

    try:
        with open(ruta_ranking, "w") as file:
            i = 1
            for jugador in top_5:
                file.write(f"{i}. {jugador['nombre']} (DNI: {jugador['dni']}) - Aciertos: {jugador['aciertos']}\n")
                i += 1
    except Exception as e:
        print(f"No se pudo escribir el ranking: {e}")

 
# funcion principal que registra al usuario y va llamando a las otras funciones       
def jugar():
    triunfos = 0
    dificultad = pedir_dificultad()

    longitud = 4 if dificultad == "1" else 5 if dificultad == "2" else 7
    palabras_filtradas = []
    for categoria in palabras_ordenadas:
        palabras_filtradas.append(tuple(p for p in categoria if len(p) == longitud))


    print("╔══════════════════════════════════════╗")
    print("║         🎉  BIENVENIDO A...          ║")
    print("║             🌟 WORDLE 🌟             ║")
    print("╚══════════════════════════════════════╝\n")
    
    while True:
        nombre = input("Ingresa tu nombre: ")
        if nombre.isalpha():
            break
        else:
            print("El nombre solo debe contener letras. Intentá de nuevo.")
            
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
                triunfos += 1
                if triunfos == 2:
                    print("🔥¡Dos triunfos seguidos!")
                elif triunfos == 3:
                    print("💥¡Tres triunfos consecutivos! No te para nadie!")
                elif triunfos >= 5:
                    print("🏆¡Crack total!")
            else:
                triunfos = 0

        respuesta = input("¿Querés jugar de nuevo? SI/NO: ")
        if respuesta.lower() != "si":
            actualizarHistorial(dni, nombre, aciertos)
            print("📂 Resultados guardados")
            print("\n🎮 Gracias por jugar a Wordle. ¡Hasta la próxima! 🎮")

            intentos_estadisticas = 0
            ver_estadisticas = ""

            while intentos_estadisticas < 2:
                ver_estadisticas = input("¿Querés ver tus estadísticas de juego? SI/NO: ").lower()
                if ver_estadisticas in ("si", "no"):
                    break
                else:
                    intentos_estadisticas += 1
                    print("Respuesta inválida. Por favor escribí 'SI' o 'NO'.")

            
            if intentos_estadisticas == 2 and ver_estadisticas not in ("si", "no"):
                print("Respuesta automática: NO")
                ver_estadisticas = "no"

            if ver_estadisticas == "si":
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
            intentos_ranking = 0
            ver_ranking = ""

            while intentos_ranking < 2:
                ver_ranking = input("¿Querés ver el ranking TOP 5? SI/NO: ").lower()
                if ver_ranking in ("si", "no"):
                    break
                else:
                    intentos_ranking += 1
                    print("Respuesta inválida. Por favor escribí 'SI' o 'NO'.")

            if intentos_ranking == 2 and ver_ranking not in ("si", "no"):
                print("Respuesta automática: NO")
                ver_ranking = "no"

            if ver_ranking == "si":
                crearRanking()
            break

def jugar_duelo():
    """Modo Duelo donde se pueden enfrentar 2 usuarios localmente y ver quien es el mejor"""
    print("🔥Modo de Duelo🔥")
    nombre1 = input("Jugador 1 - Ingresá tu nombre: ")
    dni1 = input("Jugador 1 - Ingresá tu DNI: ")
    nombre2 = input("Jugador 2 - Ingresá tu nombre: ")
    dni2 = input("Jugador 2 - Ingresá tu DNI: ")

    dificultad = pedir_dificultad()
    longitud = 4 if dificultad == "1" else 5 if dificultad == "2" else 7

    palabras_filtradas = []
    for categoria in palabras_ordenadas:
        palabras_filtradas.append(tuple(p for p in categoria if len(p) == longitud))

    print(f"\n Turno de {nombre1}")
    categoria1 = seleccionar_categoria(palabras_filtradas)
    palabra_secreta1 = generar_palabra_secreta(categoria1)
    intento1 = []
    aciertos1 = 0
    _, _, aciertos1, gano1, intentos1 = logica([palabra_secreta1], intento1, aciertos1)

    print(f"\n Turno de {nombre2}")
    categoria2 = seleccionar_categoria(palabras_filtradas)
    palabra_secreta2 = generar_palabra_secreta(categoria2)
    intento2 = []
    aciertos2 = 0
    _, _, aciertos2, gano2, intentos2 = logica([palabra_secreta2], intento2, aciertos2)

    print("\n Resultado Del Duelo:")
    if gano1 and not gano2:
        print(f"🏆 ¡Gana {nombre1}!")
    elif gano2 and not gano1:
        print(f"🏆 ¡Gana {nombre2}!")
    elif gano1 and gano2:
        if intentos1 < intentos2:
            print(f"🏆 Ambos adivinaron, pero {nombre1} lo hizo en menos intentos.")
        elif intentos2 < intentos1:
            print(f"🏆 Ambos adivinaron, pero {nombre2} lo hizo en menos intentos.")
        else:
            print("🤝 ¡Empate! Ambos adivinaron en la misma cantidad de intentos.")
    else:
        print("💀 Ninguno adivinó, son malisimos")

    if gano1:
        actualizarHistorial(dni1, nombre1, aciertos1)
    if gano2:
        actualizarHistorial(dni2, nombre2, aciertos2)
        
    print(f"\nPalabra de {nombre1} era: {palabra_secreta1}")
    print(f"Palabra de {nombre2} era: {palabra_secreta2}")
    print("📂 Resultados guardados")
    print("\n🎮 Gracias por jugar a Wordle. ¡Hasta la próxima! 🎮")
    

# main que ejecuta la funcion principal        
if __name__ == "__main__":
    print("╔══════════════════════════════════════╗")
    print("║         🎉  BIENVENIDO A...          ║")
    print("║             🌟 WORDLE 🌟             ║")
    print("╚══════════════════════════════════════╝\n")
    modo = input("🎮 ¿Querés jugar solo o en duelo? (solo/duelo): ").lower()
    if modo == "duelo":
        jugar_duelo()
    else:
        jugar()


