import random




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
        
        
        
        
