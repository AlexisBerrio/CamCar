
import pygame
import cv2
import random
#from pygame.locals import *

#Clasificador de rostros en vista fontal
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

pygame.init()


# Definicion de colores 
#        R  G  B
negro = (0, 0 ,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)
negro = (0, 0 ,0)

# ---- Declaración de variables ----
# Variables de control para el movimiento
dir = 'c'
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400,400]

hecho = True
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
#Posicion inicial obstaculos
rect_x = 100
rect_y = 50
#Posicion inicial carro
x_coord = 150
y_coord = 290
# Velocidad y direccion
rect_cambio = 2
pos_cambio = 0
pos_cambioy = 0
velocidad = 2
angle = 0
rot = 0
#Tolerancia para el centro
tol = 0.25 
#Contabilizador de puntaje
marcador = 0
#--- Crear ventana para el juego ---
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("CAMCAR")
# --- Ocultar el puntero --- 
pygame.mouse.set_visible(0)


 #-------- Clase que representa a los carros --------
class carro(pygame.sprite.Sprite):
    def __init__(self,width,height,ima):
    #Constructor, tiene como parámetros las posiciones X y Y y la imagen del carro
        pygame.sprite.Sprite.__init__(self)
        
        # Cargar imagen y eliminar el fondo negro
        self.image = ima
        self.image.set_colorkey(negro)
        # Obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        # Posiciones iniciales de la esquina superior izquierda
        self.rect.topleft=(width,height)
        
    def rot_center(self, angle,x,y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
 #-------- Clase para las monedas --------
class coin(pygame.sprite.Sprite):
    def __init__(self,width,height,color):
    #Constructor, tiene como parámetros las posiciones X y Y
        pygame.sprite.Sprite.__init__(self)
        
        # Crea un objeto con forma rectangular
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()    

#Mediante la clase Group se añaden a una lista todas las monedas generadas
moneda_lista = pygame.sprite.Group()
#Se tiene tambien en cuenta el carro del jugador
lista_sprites = pygame.sprite.Group()
 
 # ---- Generación de monedas en posiciones aleatorias ----   
for i in range(4):
    # Esto representa una moneda
    moneda = coin(20, 20, negro)
    # Establecemos una ubicación aleatoria para cada moneda
    moneda.rect.x = random.randrange(400)
    moneda.rect.y = random.randrange(400) 
    # Añadimos cada moneda a la lista de objetos
    moneda_lista.add(moneda)    
    lista_sprites.add(moneda)

# --- Score ---
fuente = pygame.font.Font(None, 25)
texto = fuente.render("Score:", True,negro)

# --- Bucle que espera que se presione una tecla para empezar el juego ---
while hecho:    
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: 
            hecho = False

# -------- Bucle principal del Programa -----------
while not hecho:
    # Captura frame-by-frame
    ret, image = cap.read()
    # Reflejar la imagen con respecto al eje y
    image = cv2.flip( image, 1 )
    # Pasar cada frame a escala de grises
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar clasificador de rostros frontales
    face = face_classifier.detectMultiScale(gris, 1.3, 5)
    # Seguimiento del rostro mediante un rectangulo
    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
        #Obtener dirección en base a la posición del rostro, 20% de tolerancia para el centro
        if (x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol) and (y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
            dir = 'c'
        elif x + w/2 < image.shape[1]/2 and (y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
            dir = 'l'
        elif x + w/2 > image.shape[1]/2 and (y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
            dir = 'r'
        elif y + h/2 < image.shape[0]/2 and (x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol):
            dir = 'u'
        elif y + h/2 > image.shape[0]/2 and (x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol):
            dir = 'd'
    # Mostrar el resultado
    cv2.imshow('image', image)
# --- Bucle principal de eventos ---
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True  
#        Al obtener la posición del rostro, se cambia la velocidad en X y Y
    if dir == 'l' and (x_coord>0):
        pos_cambio =- 3
        pos_cambioy = 0
        rot = 1
#        print('-')
    elif dir == 'r' and (x_coord<400-60):
        pos_cambio = 3
        pos_cambioy = 0
        rot = 2
#        print('+')
    elif dir == 'c':
#        print('0')
        pos_cambio = 0
        pos_cambioy = 0
    elif dir == 'u' and (y_coord>0):
        pos_cambioy =- 3
        pos_cambio = 0
        rot = 0
#        print('++')
    elif dir == 'd' and (y_coord<400-60):
        pos_cambioy = 3
        pos_cambio = 0
        rot = 3 
    else:
        pos_cambio = 0
        pos_cambioy = 0
#        print('--')
#    print(pos_cambio)
        
    x_coord = x_coord + pos_cambio
    y_coord = y_coord + pos_cambioy
    rect_y += velocidad
#   Limpiar pantalla
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    pantalla.fill(blanco)
 
#Obstaculo 1  
    obsta1=carro(rect_x,rect_y,pygame.image.load("Obstaculo1.png"))
    pantalla.blit(obsta1.image,obsta1.rect)  
#Obstaculo 2    
    obsta2=carro(rect_x+200,rect_y+6,pygame.image.load("Obstaculo2.png"))
    pantalla.blit(obsta2.image,obsta2.rect)  
#Carro
    car=carro(x_coord,y_coord,pygame.image.load("Carro.png"))
    #Con rot podemos rotar la imagen del carro dependiendo de la dirección de movimiento
    if rot == 0:
        car.rot_center(0,x_coord,y_coord)
    elif rot == 1:
        car.rot_center(90,x_coord,y_coord)
    elif rot == 2:
        car.rot_center(270,x_coord,y_coord)
    elif rot == 3:
        car.rot_center(180,x_coord,y_coord)
    pantalla.blit(car.image,car.rect)
   
    
    
# --- Se buscan colisiones del entre el carro del jugadror y las monedas    
    lista_impactos = pygame.sprite.spritecollide(car, moneda_lista, True) 
    for moneda in lista_impactos:
        marcador += 1
#        print( marcador )
# Dibujar monedas
    lista_sprites.draw(pantalla)
    
# ---- Comprobar colisiones entre carros ----   
    if pygame.sprite.collide_rect(car, obsta1) or pygame.sprite.collide_rect(car, obsta2) :
        velocidad=0
#Score en pantalla 
    pantalla.blit(texto, [5, 5])
    font = pygame.font.Font(None, 25)
    text = font.render(str(marcador), 1, negro)
    pantalla.blit(text, (70,5))      
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
cap.release()
cv2.destroyAllWindows()
pygame.quit()