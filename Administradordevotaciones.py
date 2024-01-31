dpi=""
dpi=input("Por favor ingrese dpi")
cantidad=len(dpi)
if cantidad==13:
    print("Opciones para presidente: a)Partido Rojo b)Partido Azul")
    presidente=input("¿Por quién desearía votar?; Ingrese la letra")
    print("Opciones para alcalde: a)Partido Azul b)Partido Verde c)Partido Morado d)Partido Rojo")
    alcalde=input("¿Por quién desea votar? Ingrese la letra")
    if presidente=="a":
            print("Usted voto por el Partido Rojo")
    elif presidente=="b":
            print("Usted voto por el Partido Azul") 
    if alcalde=="a":
            print("Usted voto por el Partido Azul")
    elif alcalde=="b":
            print("Usted voto por el Partido Verde")
    elif alcalde=="c":
            print("Usted voto por el Partido Morado")
    elif alcalde=="d":
            print("usted voto por el Partido Rojo")
    print("Su número de DPI es", dpi)              
if cantidad!=13:
       print("DPI no válido")            