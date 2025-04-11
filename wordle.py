import random

palabra=[]
intento=[]

def logica(palabra, intento):
        palabras=["dedos","manos","torso","silla", "llave", "mundo", "canto", "nieve", "lento", "campo", "plomo", "tigre", "brisa"]
        palabraSecreta=palabras[random.randint(0,len(palabras)-1)]
        palabra.extend(palabraSecreta)
        

        bandera=True        
        while bandera: 
                intento.clear()
                intentos=str(input("Ingresa tu intento de 5 letras: "))
                
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
                


palabra, intento=logica(palabra, intento)
        
        
        

        