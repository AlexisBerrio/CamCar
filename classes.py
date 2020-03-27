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
        self.velx = 0
        self.vely = 0
        self.posx = 0
        self.posy = 0

        # Hacer aparecer el carro en el centro si es jugador, o en posicion aleatoria si es IA
        if type == 'IA':

            self.seed = randint(0, 3)

            if self.seed == 0:
                self.vely = randint(3, 8)
                self.angle = 0
                self.dir = 'u'
                self.posx = randint(45, 320)
                self.posy = 320
            elif self.seed == 1:
                self.velx = randint(3, 8)
                self.angle = 270
                self.dir = 'r'
                self.posx = 45
                self.posy = randint(45, 320)
            elif self.seed == 2:
                self.vely = -randint(3, 8)
                self.angle = 180
                self.dir = 'd'
                self.posx = randint(45, 320)
                self.posy = 45
            else:
                self.velx = -randint(3, 8)
                self.angle = 90
                self.dir = 'l'
                self.posx = 320
                self.posy = randint(45, 320)
                
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.isPlayer = False
        else:
            self.isPlayer = True
            self.angle = 0
            self.dir = 'c'
            self.width = width
            self.height = height

        print('Type : ', type, 'position : [',self.posx, ', ', self.posy, '] dir :', self.dir)
        # Posiciones iniciales de la esquina superior izquierda
        # self.rect.topleft = (self.posx, self.posy)



    def rot_center(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.angle = angle
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move_IA (self):
        self.posx = self.posx + self.velx
        self.posy = self.posy + self.vely
        #revisar colision con pantalla
        if self.posx > 380 or self.posx < 20:
            self.velx = - self.velx
        if self.posy > 374 or self.posy < 24:
            self.vely = - self.vely
        self.rect = self.image.get_rect()    
        self.rect.center = (self.posx, self.posy)   
    
    def set_dir(self, dir):
        self.dir = dir
# -------- Clase para las monedas --------
class Coin(pygame.sprite.Sprite):
    def __init__(self,width,height):
    #Constructor, tiene como parámetros las posiciones X y Y
        pygame.sprite.Sprite.__init__(self)      
        # Crea un objeto con forma rectangular  
        self.image=pygame.image.load("Coin.png")
        self.rect = self.image.get_rect() 
