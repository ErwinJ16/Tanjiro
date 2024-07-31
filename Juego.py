import pygame
import sys

states = {
    "Pantalla inicial": "inicio.jpg",
    "Pantalla 1": "instrucciones.png",
    "Pantalla 2": "opciones.png",
    "Pantalla 3": "imagen1.png",
    "Pantalla 4": "imagen2.png",
    "Pantalla 5": "texto1.png",
    "Pantalla 6": "imagen 3.png",
    "Pantalla 7": "imagen 4.png",
    "Pantalla 8": "texto 2.png",
    "Pantalla 9": "texto 3.png",
    "Pantalla 10": "texto 4.png",
    "Pantalla 11": "pueblo 1.png",
    "Pantalla 12": "pueblo 2.png",
    "Pantalla 13": "texto 5.png",
    "Pantalla 14": "texto 6.png",
    "Pantalla 15": "prometida.png",
    "Pantalla 16": "texto7.png",
    "Pantalla 17": "pueblo 3.png",
    "Pantalla 18": "pergaminono.png",
    "Pantalla 19": "caminar.png",
    "Pantalla 20": "texto8.png",
    "Pantalla 21": "piedras.png",
    "Pantalla 22": "texto9.png",
    "Pantalla 23": "inicio3.png",
    "Pantalla 24": "demonio.png",
    "Pantalla 25": "muerte1.png",
    "Pantalla 26": "restos.png",
    "Pantalla 27": "dialogo.png",
    "Pantalla 28": "manus.png",
    "Pantalla 29": "origen.png",
    "Pantalla 30": "llegar.png",
    "Pantalla 31": "camino.png",
    "Pantalla 32": "destino.png",
    "Pantalla 33": "boss.png",
    "Pantalla 34": "boss2.png",
    "Pantalla 35": "boss3.png",
    "Pantalla 36": "convertir.png",
    "Pantalla 37": "convertir2.png",
    "Pantalla 38": "convertir3.png",
    "Pantalla 39": "convertir4.png",
    "Pantalla 40": "poderno.png",
    "Pantalla 41": "heroe.png",
    "Pantalla 42": "heroe2.png",
    "Pantalla 43": "heroe3.png",
    "Pantalla 44": "heroe4.png",
    "Pantalla 45": "heroe5.png"
}

transitions = {
    "Pantalla inicial": {"space": "Pantalla 1"},
    "Pantalla 1": {"space": "Pantalla 2"},
    "Pantalla 2": {"left": "Pantalla 3", "right": "Pantalla 4", "space": "Pantalla 5"},
    "Pantalla 3": {},
    "Pantalla 4": {"space": "Pantalla 28"},
    "Pantalla 5": {"left": "Pantalla 6", "right": "Pantalla 7"},
    "Pantalla 6": {},
    "Pantalla 7": {},
    "Pantalla 8": {"space": "Pantalla 9"},
    "Pantalla 9": {"left": "Pantalla 24", "right": "Pantalla 27"},
    "Pantalla 10": {"left": "Pantalla 11", "right": "Pantalla 18"},
    "Pantalla 11": {"space": "Pantalla 12"},
    "Pantalla 12": {"space": "Pantalla 13"},
    "Pantalla 13": {"space": "Pantalla 14"},
    "Pantalla 14": {"space": "Pantalla 15"},
    "Pantalla 15": {"space": "Pantalla 16"},
    "Pantalla 16": {"space": "Pantalla 17"},
    "Pantalla 17": {},
    "Pantalla 18": {},
    "Pantalla 19": {"space": "Pantalla 20"},
    "Pantalla 20": {"space": "Pantalla 21"},
    "Pantalla 21": {"space": "Pantalla 22"},
    "Pantalla 22": {"space": "Pantalla 23"},
    "Pantalla 23": {},
    "Pantalla 24": {"space": "Pantalla 25"},
    "Pantalla 25": {"space": "Pantalla 26"},
    "Pantalla 26": {"space": "Pantalla 27"},
    "Pantalla 27": {"space": "Pantalla 19"},
    "Pantalla 28": {"left": "Pantalla 29", "right": "Pantalla 30", "space": "Pantalla 4"},
    "Pantalla 29": {"space": "Pantalla 31"},
    "Pantalla 30": {"space": "Pantalla 31"},
    "Pantalla 31": {"space": "Pantalla 32"},
    "Pantalla 32": {"left": "Pantalla 33", "right": "Pantalla 41", "space": "Pantalla 35"},
    "Pantalla 33": {"space": "Pantalla 34"},
    "Pantalla 34": {"space": "Pantalla 35"},
    "Pantalla 35": {"left": "Pantalla 36", "right": "Pantalla 40", "space": "Pantalla 37"},
    "Pantalla 36": {"space": "Pantalla 37"},
    "Pantalla 37": {"space": "Pantalla 38"},
    "Pantalla 38": {"space": "Pantalla 39"},
    "Pantalla 39": {"space": "Pantalla 40"},
    "Pantalla 40": {"space": "Pantalla 19"},
    "Pantalla 41": {"space": "Pantalla 42"},
    "Pantalla 42": {"left": "Pantalla 43", "right": "Pantalla 44", "space": "Pantalla 45"},
    "Pantalla 43": {"space": "Pantalla 19"},
    "Pantalla 44": {"space": "Pantalla 45"},
    "Pantalla 45": {}
}

pygame.init()
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
estado = "Pantalla inicial"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                estado = transitions[estado].get("space", estado)
            elif event.key == pygame.K_LEFT:
                estado = transitions[estado].get("left", estado)
            elif event.key == pygame.K_RIGHT:
                estado = transitions[estado].get("right", estado)

    image = pygame.image.load(states[estado])
    image = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
