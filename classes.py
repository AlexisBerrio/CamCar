# --------------------------------------------------------------------------
# ------- CARCAM Juego ( Clases ) - Primera entrega  -----------------------
# ------- Procesamiento digital de imagenes --------------------------------
# ------- Por: Juan S. Guerrero    jsebastian.guerrero@udea.edu.co  --------
# -------      Johan Alexis Berrío        johan.berrio@udea.edu.co  --------
# -------      Estudiantes  ------------------------------------------------
# ------- Marzo de 2020  ---------------------------------------------------
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# --1. Importar dependencias  ---------------------------------------------
# --------------------------------------------------------------------------
import pygame # las clases heredan de pygame sprite debido a que seran instanciados en imagenes
from random import randint # randint permite generar posiciones y velocidades aleatorias

# --------------------------------------------------------------------------
# --2. Clase que representa los carros  ------------------------------------
# --------------------------------------------------------------------------
class Carro(pygame.sprite.Sprite):
    #Constructor, tiene como parámetros las posiciones X y Y y la imagen del carro
    def __init__(self, width, height, ima, color,type):
        # Esta propiedad recibe a la clase misma para instanciar despues la imagen
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen y eliminar el fondo negro
        self.image = ima
        self.image.set_colorkey(color)
        # Obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        # Definir variables de velocidad y posicion del carro en x,y
        self.velx = 0
        self.vely = 0
        self.posx = 0
        self.posy = 0

        # Hacer aparecer el carro en el centro si es jugador, o en posicion aleatoria si es IA
        if type == 'IA':
            #la variable seed dice la direccion que tendra la IA por defecto siendo aleatoria entre 0 y 3:
            # 0 - > arriba con angulo de 0 grados, velocidad aleatoria entre 3 y 8 hacia abajo
            #       aparece aleatoriamente en la parte inferior de la pantalla
            # 1 - > derecha con angulo de 270 grados, velocidad aleatoria entre 3 y 8
            #       aparece aleatoriamente en la parte izquierda de la pantalla
            # 2 - > abajo con angulo de 180 grados, velocidad aleatoria entre 3 y 8
            #       aparece aleatoriamente en la parte superior de la pantalla
            # 3 - > izquierda con angulo de 90 grados, velocidad aleatoria entre 3 y 8
            self.seed = randint(0, 3)

            if self.seed == 0:
                self.vely = randint(3, 8) # velocidad y aleatoria entre 3 y 8
                self.angle = 0 # angulo con respecto a la vertical
                self.dir = 'u' # direccion
                self.posx = randint(45, 320) # posicion x
                self.posy = 320 # posicion y
            elif self.seed == 1:
                self.velx = randint(3, 8) # velocidad x aleatoria entre 3 y 8
                self.angle = 270 # angulo con respecto a la vertical
                self.dir = 'r' # direccion
                self.posx = 45 # posicion x
                self.posy = randint(45, 320) # posicion y
            elif self.seed == 2:
                self.vely = -randint(3, 8) # velocidad y aleatoria entre 3 y 8
                self.angle = 180 # angulo con respecto a la vertical
                self.dir = 'd' # direccion
                self.posx = randint(45, 320) # posicion x
                self.posy = 45 # posicion y
            else:
                self.velx = -randint(3, 8) # velocidad x aleatoria entre 3 y 8
                self.angle = 90 # angulo con respecto a la vertical
                self.dir = 'l' # direccion
                self.posx = 320 # posicion x
                self.posy = randint(45, 320) # posicion y
            #transform rota la imagen de acuerdo al angulo
            self.image = pygame.transform.rotate(self.image, self.angle)
            # la bandera de identificacion es falsa ya que es IA y no jugador
            self.isPlayer = False
        else:
            # de otro modo la bandera de jugador es True
            self.isPlayer = True
            # el angulo es 0
            self.angle = 0
            # direccion central
            self.dir = 'c'
            # la posicion x es la que se configura en el archivo pricipal
            self.width = width
            # la posicion y es la que se configura en el archivo pricipal
            self.height = height

# --2. Metodos de clase Carro  ------------------------------------
    # rot center permite rotar la imagen y moverla para despues PyGame actualizar la pantalla
    def rot_center(self, angle, x, y):
        # se rota la imagen
        self.image = pygame.transform.rotate(self.image, angle)
        #se guarda el angulo de rotacion para rotaciones consecutivas
        self.angle = angle
        # se guarda la informacion de ancho y largo para usarla en la deteccion de colision
        self.rect = self.image.get_rect()
        # se cambia las coordenadas por las actuales
        self.rect.center = (x, y)
    # move_IA sirve para mover
    def move_IA (self):
        # mover automaticamente el carro con la velocidad inicial ya sea x o y
        self.posx = self.posx + self.velx # movimiento en x
        self.posy = self.posy + self.vely # movimiento en y
        #revisar colision con pantalla
        # si se choca invierte su velocidad ya sea x o y
        if self.posx > 380 or self.posx < 20:
            self.velx = - self.velx
        if self.posy > 374 or self.posy < 24:
            self.vely = - self.vely
        #se actualiza la informacion de posicion
        self.rect = self.image.get_rect()
        # se cambia finalmente por la nueva para refrescar pantalla despues
        self.rect.center = (self.posx, self.posy)   
    # set_dir permite cambiar la direccion del objeto por la que se ingresa
    def set_dir(self, dir):
        self.dir = dir
# --------------------------------------------------------------------------
# --3. Clase que representa las monedas  -----------------------------------
# --------------------------------------------------------------------------
class Coin(pygame.sprite.Sprite):
    #Constructor, tiene como parámetros las posiciones X y Y
    def __init__(self,width,height):
        # Esta propiedad recibe a la clase misma para instanciar despues la imagen
        pygame.sprite.Sprite.__init__(self)      
        # Crea un objeto con forma rectangular con la imagen coin
        self.image=pygame.image.load("Coin.png")
        # se guarda la informacion de ancho y largo para usarla en la deteccion de colision
        self.rect = self.image.get_rect()

#--------------------------------------------------------------------------
#---------------------------  FIN DEL ARCHIVO -----------------------------
#--------------------------------------------------------------------------