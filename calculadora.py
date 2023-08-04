def suma (a, b):
    return a+b 
def resta(a, b):
    return a-b 
def multiplicacion(a, b):
    return a*b 
def division (a, b):
    return a/b 

def input_int(mensaje, mensaje_error):
        while True:
            try:
                v=int(input(mensaje))
            except ValueError:
                pass
            else:
                return v
        #break


menu = """
    calculadora:
opciones:
1. sumar 
2. restar
3. multiplicacion
4. division
5.
"""

while True:
    print(menu)
    opcion = input_int("elije la opcion : ","es la opcion incorrecta:")

    if opcion in [1,2,3,4,]:
        if opcion == 1:
            a=int(input("ingrese el primer valor:", " mensaje_error:"))
            b=int(input("ingrese el segundo valor:"," mensaje_error:"))
            if opcion ==1:
                    print(f"el resultado es {suma(a,b)}")
            elif opcion ==2:
                      print(f"el resultado es {resta(a,b)}")
            elif opcion ==3:
                        print(f"el resultado es {multiplicacion(a,b)}")
            elif opcion ==4:
                        print(f"el resultado es {division(a,b)}")
        elif opcion == 5:
              print("saliendo")
              