texto="hola mundo aaaaaaa"

con_a=0 

for i in texto:
    if (i=="a" or i=="e"):
        if(i=="a"):
            cont_a += 1
        print("es una vocal")
    elif(i==" "):
        print(es un espacio)
    else:
        print("es un consonante")

        print(f" la cantidad de la vocal a es { con_a}")


