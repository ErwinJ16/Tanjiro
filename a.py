import pygame
import sys
import random

# Iniciar
pygame.init()

# Configuracion de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triángulo asesino")

# Color del fondo
background_color = (0, 0, 0)

# tamaño y posicion del triangulo
triangle_size = 50
x = width // 2 - triangle_size // 2
y = height // 2 - triangle_size // 2

# velocidad del triangulo
speed = 6

# laser
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 20
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

# objetivos
class Target:
    def __init__(self):
        self.x = random.randint(0, width - 20)
        self.y = -20
        self.width = 20
        self.height = 20
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.y > height - self.height:
            self.y = -20

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Iniciar contador
score = 0

# Iniciar laser
laser = None

# Iniciar objetivos
targets = [Target() for _ in range(5)]

# loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed # Move the triangle up
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    
    # disparar con la barra
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + triangle_size // 2, y + triangle_size)

    # Mover el laser
    if laser is not None:
        laser.move()

    # Mover los objetivos
    for target in targets:
        target.move()

    # verificar si el laser golpea a un objetivo
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    # verificar si el laser esta fuera de la pantalla
    if laser is not None and laser.y < 0:
        laser = None

    
    for target in targets:
        if (x <= target.x + target.width and
            x + triangle_size >= target.x and
            y <= target.y + target.height and
            y + triangle_size >= target.y):
            running = False
            font = pygame.font.Font(None, 36)
            text = font.render("Fin del juego", True, (255, 0, 0))
            screen.blit(text, (width // 2 - 100, height // 2 - 30))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before quitting
            break

    # mantener al tirangulo en la ventana
    if x < 0:
        x = 0
    elif x + triangle_size > width:
        x = width - triangle_size
    if y < 0:
        y = 0
    elif y + triangle_size > height:
        y = height - triangle_size

    # fondo, triangulo y laser
    screen.fill(background_color)
    points = [(x, y + triangle_size), (x + triangle_size, y + triangle_size), (x + triangle_size // 2, y)]
    pygame.draw.polygon(screen, (255, 0, 0), points)
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    # puntaje
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # actualizar la pantalla
    pygame.display.flip()

    # velocidad del loop
    pygame.time.Clock().tick(60)

# salir de pygame
pygame.quit()
sys.exit()