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
    print("El volumen seria de : ", str(result), "m^3")


int_distancia=float(input("Ingrese la distancia: "))
int_tiempo=float(input("Ingrease el tiempo: "))
found_vel(int_distancia, int_tiempo)

int_velocidad=float(input("Ingrese la velocidad: "))
int_tiempo=float(input("Ingrease el tiempo: "))
found_dist(int_velocidad, int_tiempo)

int_distancia=float(input("Ingrease la distancia: "))
int_velocidad=float(input("Ingrese la velocidad: "))
found_tiempo(int_distancia, int_velocidad)

int_lado=float(input("Ingrease la medida del lado: "))
found_vol(int_lado)