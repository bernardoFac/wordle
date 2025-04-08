import random

def comparar_palabras(lista1,lista2):
        for i in range(len(lista1)):
                if lista1[i]==lista2[i]:
                        print(lista1[i], "es correcto")
                elif lista1[i] in lista2:
                        print(lista1[i], "está en la palabra pero en la posición incorrecta")
                else:
                        print(lista1[i], "no está en la palabra")
                



def logica():
        palabras=["dedos","manos","torso","silla", "llave", "mundo", "canto", "nieve", "lento", "campo", "plomo", "tigre", "brisa"]
        palabra=[]
        palabra.extend(palabras[random.randint(0,len(palabras)-1)])
        intento=[]
        intentos=str(input("Ingresa tu intento de 5 letras: "))
        while len(intentos)!=5:
                print("El intento debe contener exactamente 5 letras.")
                intentos=str(input("Ingresa tu intento de 5 letras: "))
        
        intento.extend(intentos)
                
        while intento!=palabra: 
                print("Palabra incorrecta.")
                intento=[]
                intentos=str(input("Ingresa tu intento de 5 letras: "))
                intento.extend(intentos)
        
        print("Felicitaciones, adivinaste la palabra")
      
logica()
        
        
        
        
