import mymathlib

while True:
    print("Seleccione la opción que desea realizar: ")
    print("1. Velocidad")
    print("2. Distancia")
    print("3. Tiempo")
    print("4. Volumen")
    print("5. Area")
    print("6. Perimetro")
    print("7. Fuerza")
    print("8. Trabajo")
    print("9. Potencia")
    print("10. Aceleración")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion=="1":
        int_distancia=float(input("Ingrese la distancia: "))
        int_tiempo=float(input("Ingrease el tiempo: "))
        found_vel(int_distancia, int_tiempo)

    if opcion=="2":
        int_velocidad=float(input("Ingrese la velocidad: "))
        int_tiempo=float(input("Ingrease el tiempo: "))
        found_dist(int_velocidad, int_tiempo)

    if opcion=="3":
        int_distancia=float(input("Ingrese la distancia: "))
        int_velocidad=float(input("Ingrese la velocidad: "))
        found_tiempo(int_distancia, int_velocidad)

    if opcion=="4":
        int_lado=float(input("Ingrease la medida del lado: "))
        found_vol(int_lado)

    if opcion=="5":
        int_lado1=float(input("Ingrese la medida del lado: "))
        int_lado2=float(input("Ingrese la medida del otro lado: "))
        found_area(int_lado1, int_lado2)

    if opcion=="6":
        int_lado1=float(input("Ingrese la medida de un lado: "))
        int_lado2=float(input("Ingrese la medida del otro lado: "))
        found_perim(int_lado1, int_lado2)

    if opcion=="7":
        int_masa=float(input("Ingrese la masa: "))
        int_aceleracion=float(input("Ingrese la aceleración: "))
        found_fuerza(int_masa, int_aceleracion)

    if opcion=="8":
        int_fuerza=float(input("Ingrese la fuerza: "))
        int_desplazamiento=float(input("Ingrese el desplazamiento: "))
        found_trabajo(int_fuerza, int_desplazamiento)

    if opcion=="9":
        int_peso=float(input("Ingrese la velocidad inicial: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        found_pot(int_peso, int_tiempo)

    if opcion=="10":
        int_velocidadf=float(input("Ingrese la velocidad final: "))
        int_velocidadin=float(input("Ingrese la velocidad inicial: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        found_acel(int_velocidadf, int_velocidadin, int_tiempo)
    
    elif opcion=="11":
        print("Se cierra el programa")
        break
    
    else:
        print("Opción no válida")