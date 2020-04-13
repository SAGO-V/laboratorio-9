print ("inicio ")

for i in range (2,50):
        b=0;
    for j in range (1,(i//2)+1):
        if((i%j)==0):
            b=b+j;
    if(b==i):
        print("El numero" + str(i) + "es perfecto");


print ("fin ")
