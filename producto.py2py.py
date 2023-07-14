def crearprotductos(lista_productos):
    flag=True
    while flag:
        try:
            nombreproducto = input("nombre del producto")
            marcaproducto = input("marca del producto")
            costoproducto = int(input("costo del producto"))
            cantidadproducto = int(input("cantida del producto"))
        except ValueError:
            print("algo salio mal intentalo de nuevo")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]=costoproducto
            producto["cantida"]=cantidadproducto
            lista_productos(producto)
            producto ={}
            pregunta = input("desea agregar mas productos? si/no")
            if str (pregunta) != "si":
                  flag =False

                  print(lista_productos)


 #productos 

print("""
      supermercado
      elija una opcion
      1. listar los productos
      2. agregar mas productos
      3. hacer una ventana
      """)     
            
def listarproductos(lista_productos):
    for producto in lista_productos:
        print(f"{producto.get('nombre') | {producto.get ('cantidad)} | {productos.get('costo)}}" )