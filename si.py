#area de funciones
def found_vel (distancia, tiempo):
    result=distancia/tiempo
    print("la velocidad seria de: ", str(result), "m/s")

def found_dist (velocidad, tiempo):
    result=velocidad*tiempo
    print("la distancia seria de: ", str(result), "m")

def found_tiempo (distancia, velocidad):
    result=distancia/velocidad
    print("El tiempo seria de: ", str(result), "s")

def found_vol (lado):
    result=lado*lado*lado
    print("El volumen seria de : ", str(result), "m^3")

def found_area (lado1, lado2):
    result=lado1*lado2
    print("El area seria de : ", str(result), "m^2")

def found_perim (lado1, lado2):
    result=lado1+lado2+lado1+lado2
    print("El perimetro seria de : ", str(result), "m^2")

def found_fuerza (masa, aceleracion):
    result=masa*aceleracion
    print("La fuerza seria de : ", str(result), "N")

def found_trabajo (fuerza, desplazamiento):
    result=fuerza*desplazamiento
    print("El trabajo seria de : ", str(result), "J")

def found_pot (peso, tiempo):
    result=peso/tiempo
    print("La potencia seria de : ", str(result), "J/s")

def found_acel (velocidad_f, velocidad_in, tiempo):
    result=(velocidad_f-velocidad_in)/tiempo 
    print("La velocidad incial seria de : ", str(result), "m/s")

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

    int_velocidad=float(input("Ingrese la velocidad: "))
    int_tiempo=float(input("Ingrease el tiempo: "))
    found_dist(int_velocidad, int_tiempo)

    int_distancia=float(input("Ingrese la distancia: "))
    int_velocidad=float(input("Ingrese la velocidad: "))
    found_tiempo(int_distancia, int_velocidad)

    int_lado=float(input("Ingrease la medida del lado: "))
    found_vol(int_lado)

    int_lado1=float(input("Ingrese la medida del lado: "))
    int_lado2=float(input("Ingrese la medida del otro lado: "))
    found_area(int_lado1, int_lado2)

    int_lado1=float(input("Ingrese la medida de un lado: "))
    int_lado2=float(input("Ingrese la medida del otro lado: "))
    found_perim(int_lado1, int_lado2)

    int_masa=float(input("Ingrese la masa: "))
    int_aceleracion=float(input("Ingrese la aceleración: "))
    found_fuerza(int_masa, int_aceleracion)

    int_fuerza=float(input("Ingrese la fuerza: "))
    int_desplazamiento=float(input("Ingrese el desplazamiento: "))
    found_trabajo(int_fuerza, int_desplazamiento)

    int_peso=float(input("Ingrese la velocidad inicial: "))
    int_tiempo=float(input("Ingrese el tiempo: "))
    found_pot(int_peso, int_tiempo)

    int_velocidadf=float(input("Ingrese la velocidad final: "))
    int_velocidadin=float(input("Ingrese la velocidad inicial: "))
    int_tiempo=float(input("Ingrese el tiempo: "))
    found_acel(int_velocidadf, int_velocidadin, int_tiempo)