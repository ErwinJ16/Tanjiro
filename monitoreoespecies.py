conteo_especies={}
print("Bienvenido al programa de monitoreo de especies")
print("Debera ingresar el nombre de una especie avistada en el ecosistema o fin para cerrar la lista")
while True:
    especies=input("Ingrese las especies avistadas")
    if especies=="fin":
        break
    if especies in conteo_especies:
        conteo_especies[especies] += 1
    else:
        conteo_especies[especies] =1
especie_comun=max(conteo_especies, key=conteo_especies.get)
num_especie=conteo_especies[especie_comun]
print("Las especies avistadas son:", conteo_especies)
print("La especie más común en el ecosistema es", especie_comun, "con", num_especie, "avistamientos")
print("Se cierra el programa")