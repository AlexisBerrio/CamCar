import pygame
from random import randint

# -------- Clase que representa a los carros --------
class Carro(pygame.sprite.Sprite):
    def __init__(self, width, height, ima, color,type):
        # Constructor, tiene como parámetros las posiciones X y Y y la imagen del carro
        pygame.sprite.Sprite.__init__(self)

        # Cargar imagen y eliminar el fondo negro
        self.image = ima
        self.image.set_colorkey(color)
        # Obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()

        # Hacer aparecer el carro en el centro si es jugador, o en posicion aleatoria si es IA
        if type == 'IA':

            self.seed = randint(0, 3)

            self.velx = 0
            self.vely = 0

            if self.seed == 0:
                self.vely = randint(10, 45)
                self.angle = 0
                self.dir = 'u'
                self.width = randint(45, 320)
                self.height = 320
            elif self.seed == 1:
                self.velx = randint(10, 45)
                self.angle = 270
                self.dir = 'r'
                self.width = 45
                self.height = randint(45, 320)
            elif self.seed == 2:
                self.vely = -randint(3, 45)
                self.angle = 145
                self.dir = 'd'
                self.width = randint(45, 320)
                self.height = 45
            else:
                self.velx = -randint(3, 45)
                self.angle = 90
                self.dir = 'l'
                self.width = 320
                self.height = randint(45, 320)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.isPlayer = False
        else:
            self.isPlayer = True
            self.angle = 0
            self.dir = 'c'
            self.width = width
            self.height = height

        print('Type : ', type, 'position : [',self.width, ', ', self.height, '] dir :', self.dir)
        # Posiciones iniciales de la esquina superior izquierda
        self.rect.topleft = (self.width, self.height)



    def rot_center(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.angle = angle
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def set_dir(self, dir):
        self.dir = dir
# -------- Clase para las monedas --------
class Coin(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        # Constructor, tiene como parámetros las posiciones X y Y
        pygame.sprite.Sprite.__init__(self)

        # Crea un objeto con forma rectangular y lo instancia como superficie colisionable
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
