import pygame
import sys
pygame.init()


screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

estado="Pantalla inicial"

def cargar(nombre):
    img=pygame.transform.scale(pygame.image.load(nombre), (screen_width, screen_height))
    screen.blit(img, (0, 0))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print(estado)
                if estado == "Pantalla inicial":
                    estado = "Pantalla 1"
                elif estado == "Pantalla 1":
                    estado = "Pantalla 2"
                elif estado == "Pantalla 3":
                    estado="Pantalla 5"
                elif estado=="Pantalla 6":
                    estado="Pantalla 8" 
                elif estado=="Pantalla 7":
                    estado="Pantalla 9" 
                elif estado=="Pantalla 8":
                    estado="Pantalla 10"
                elif estado=="Pantalla 11":  
                    estado="Pantalla 12"
                elif estado=="Pantalla 12":  
                    estado="Pantalla 13"
                elif estado=="Pantalla 13":
                    estado="Pantalla 14"
                elif estado=="Pantalla 14":
                    estado="Pantalla 15"
                elif estado=="Pantalla 15":
                    estado="Pantalla 16"
                elif estado=="Pantalla 16":
                    estado="Pantalla 17"
                elif estado=="Pantalla 18":
                    estado="Pantalla 19"
                elif estado=="Pantalla 19":
                    estado="Pantalla 20"
                elif estado=="Pantalla 20":
                    estado="Pantalla 21" 
                elif estado=="Pantalla 21":
                    estado="Pantalla 22" 
                elif estado=="Pantalla 22":
                    estado="Pantalla 23" 
                elif estado=="Pantalla 24":
                    estado="Pantalla 25"
                elif estado=="Pantalla 25":
                    estado="Pantalla 26"
                elif estado=="Pantalla 27":
                    estado="Pantalla 19"
                elif estado=="Pantalla 4":
                    estado="Pantalla 28"
                elif estado=="Pantalla 29":
                    estado="Pantalla 31"
                elif estado=="Pantalla 30":
                    estado="Pantalla 31"
                elif estado=="Pantalla 31":
                    estado="Pantalla 32"
                elif estado=="Pantalla 33":
                    estado="Pantalla 34"
                elif estado=="Pantalla 34":
                    estado="Pantalla 35"
                elif estado=="Pantalla 36":
                    estado="Pantalla 37"
                elif estado=="Pantalla 37":
                    estado="Pantalla 38"
                elif estado=="Pantalla 38":
                    estado="Pantalla 39"
                elif estado=="Pantalla 40":
                    estado="Pantalla 19"
                elif estado=="Pantalla 41":
                    estado="Pantalla 42"
                elif estado=="Pantalla 43":
                    estado="Pantalla 19"
                elif estado=="Pantalla 44":
                    estado="Pantalla 45"
            if event.key == pygame.K_LEFT:
                if estado == "Pantalla 2":
                    estado = "Pantalla 3"
                elif estado=="Pantalla 5":
                    estado="Pantalla 6"
                elif estado=="Pantalla 10":
                    estado="Pantalla 11"
                elif estado=="Pantalla 9":
                    estado="Pantalla 24"
                elif estado=="Pantalla 28":
                    estado="Pantalla 29"   
                elif estado=="Pantalla 32":
                    estado="Pantalla 33"  
                elif estado=="Pantalla 35":
                    estado="Pantalla 36" 
                elif estado=="Pantalla 42":
                    estado="Pantalla 43"
            if event.key==pygame.K_RIGHT:
                if estado=="Pantalla 5":
                    estado="Pantalla 7"
                elif estado=="Pantalla 5":
                    estado="Pantalla 26"  
                elif estado=="Pantalla 10":
                    estado="Pantalla 18"
                elif estado=="Pantalla 9":
                    estado="Pantalla 27" 
                elif estado=="Pantalla 28":
                    estado="Pantalla 30" 
                elif estado=="Pantalla 32":
                    estado="Pantalla 41" 
                elif estado=="Pantalla 35":
                    estado="Pantalla 40" 
                elif estado=="Pantalla 42":
                    estado="Pantalla 44"  
                elif estado == "Pantalla 2":
                    estado = "Pantalla 4"                

    if estado=="Pantalla inicial":
        cargar("inicio.jpg")

    elif estado=="Pantalla 1":
        cargar("instrucciones.png")

    elif estado=="Pantalla 2":
        cargar("opciones.png")

    elif estado=="Pantalla 3":
        cargar ("imagen1.png")

    elif estado=="Pantalla 4":
        cargar("imagen2.png")

    elif estado=="Pantalla 5":
        cargar("texto1.png")

    elif estado=="Pantalla 6":
        cargar ("imagen 3.png")    

    elif estado=="Pantalla 7":
        cargar ("imagen 4.png")

    elif estado=="Pantalla 8":
        cargar ("texto 2.png")    

    elif estado=="Pantalla 9":
        cargar ("texto 3.png")
    
    elif estado=="Pantalla 10":
        cargar ("texto 4.png") 

    elif estado=="Pantalla 11":
        cargar ("pueblo 1.png")
    
    elif estado=="Pantalla 12":
        cargar ("pueblo 2.png")
    
    elif estado=="Pantalla 13":
        cargar ("texto 5.png")
    
    elif estado=="Pantalla 14":
        cargar ("texto 6.png")

    elif estado=="Pantalla 15":
        cargar ("prometida.png")
    
    elif estado=="Pantalla 16":
        cargar ("texto7.png")

    elif estado=="Pantalla 17":
        cargar ("pueblo 3.png")
    
    elif estado=="Pantalla 18":
        cargar ("pergaminono.png")
    
    elif estado=="Pantalla 19":
        cargar ("caminar.png")

    elif estado=="Pantalla 20":
        cargar ("texto8.png")

    elif estado=="Pantalla 21":
        cargar ("piedras.png")

    elif estado=="Pantalla 22":
        cargar ("texto9.png")

    elif estado=="Pantalla 23":
        cargar ("inicio3.png")

    elif estado=="Pantalla 24":
        cargar ("demonio.png") 

    elif estado=="Pantalla 25":
        cargar ("muerte1.png")

    elif estado=="Pantalla 26":
        cargar ("restos.png")  

    elif estado=="Pantalla 27":
        cargar ("dialogo.png")

    elif estado=="Pantalla 28":
        cargar ("manus.png")
    
    elif estado=="Pantalla 29":
        cargar ("origen.png")
    
    elif estado=="Pantalla 30":
        cargar ("llegar.png")
    
    elif estado=="Pantalla 31":
        cargar ("camino.png")
    
    elif estado=="Pantalla 32":
        cargar ("destino.png")
       
    elif estado=="Pantalla 33":
        cargar ("boss.png")
    
    elif estado=="Pantalla 34":
        cargar ("boss2.png") 
    
    elif estado=="Pantalla 35":
        cargar ("boss3.png") 
    
    elif estado=="Pantalla 36":
        cargar ("convertir.png")

    elif estado=="Pantalla 37":
        cargar ("convertir2.png")

    elif estado=="Pantalla 38":
        cargar ("convertir3.png")

    elif estado=="Pantalla 39":
        cargar ("convertir4.png")

    elif estado=="Pantalla 40":
        cargar ("poderno.png")

    elif estado=="Pantalla 41":
        cargar ("heroe.png")
    
    elif estado=="Pantalla 42":
        cargar ("heroe2.png")
    
    elif estado=="Pantalla 43":
        cargar ("heroe3.png")

    elif estado=="Pantalla 44":
        cargar ("heroe4.png")

    elif estado=="Pantalla 45":
        cargar ("heroe5.png")
    pygame.display.flip()

pygame.quit()
sys.exit()
