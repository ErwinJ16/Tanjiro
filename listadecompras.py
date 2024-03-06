lista=[]
for _ in range(50):
    item=input("ingrese un item")
    if item=="fin":
        print("Se cierra la lista de compras")
        break
    else:
        lista.append(item)
print("La lista es:", lista)
eliminar=input("¿Desea eliminar un item?")
if eliminar=="si":
        while True:
            item=input("¿Qué item quiere borrar?:")
            if item=="fin":
                 print("Se cierra la lista")
                 print("Los items son:", lista)
                 break
            else:
                 lista.remove(item)
elif eliminar=="no":
    print("Los items son:", lista)


