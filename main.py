
print("para empezar el programa siga las siguientes instrucciones")
base=int(input("para iniciar escribe 1 para finalizar escribe 0 \n ")) 

cantidad_opera= 0 
while base !=0 :
    base=int(input("escriba el numero de la base de la pontencia \n ")) 
    
    cantida_opera = cantidad_opera + 1
    
    if base !=0 :
        exponente=int(input("escriba el numero del exponente de la potencia \n ")) 
        resultado= 1
        i=0
    
        for i in  range(exponente):
            resultado *= base
            
    print("la potencia es")
    print(resultado)


print ("la cantidad de operaciones fue de ")
print(cantida_opera)







