producto = {
    "nombre": "", 
    "marca": "",
    "costo": 0,
    "cantidad": 0,
}

lista_productos = []

flag=True
while flag:
    try: 
        nombreproducto = input("Nombre del producto: ")
        marcaproducto = input("Marca del producto: ")
        costoproducto = int(input("Costo del producto: "))
        cantidadproducto = int(input("Cantidad del producto: "))
    except ValueError:
        print("ALGO SALIO MAL INTENTALO OTRA VEZ")
    else:
        producto["nombre"]= nombreproducto
        producto["marca"]= marcaproducto
        producto["costo"]= costoproducto
        producto["cantidad"]= cantidadproducto
        lista_productos.append(producto)
        producto = {}
        pregunta = input("Desea agrear mas Productos? SI/NO")
        if str(pregunta) != "SI":
            flag = False

        print(lista_productos)

#menu
print("""
      Supermercado 
      elija la opcion
1. listar los productos
2. agregar mas productos
3. hacer la venta.
""")

opcion = input("elija la opcion del menu: ")
