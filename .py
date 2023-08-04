from Productos import Productos



lista_productos=[]
p=productos("laptop","asus",20000,5)
lista_productos.append(p)
print(lista_productos)
producto=lista_productos
print(producto.info())

nombre_p=input("nombre del producto")
marca_p=input("marca del producto")
precio_p=int(input("precio del producto:","no ingresaste bien el precio"))
cantidad_p=int(input("cantidad del producto:"))
t=producto(nombre_p,marca_p,precio_p,cantidad_p)
print (t.info())