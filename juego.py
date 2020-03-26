
import pygame
import cv2
import random
from classes import Carro,Coin
#from pygame.locals import *

#Clasificador de rostros en vista fontal
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(-1)

pygame.init()


# Definicion de colores 
#        R  G  B
negro = (0, 0 ,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)
amarillo = (255, 255, 0)
negro = (0, 0 ,0)

# ---- Declaración de variables ----
# Variables de control para el movimiento
dir = 'c'
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400,400]

hecho = True
# flagScore se usa para detectar colision y agregar enemigos una sola vez
flagScore = False
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
#Posicion inicial obstaculos
rect_x = 25
rect_y = 35
#Posicion inicial Carro
x_coord = 150
y_coord = 290
# Velocidad y direccion
rect_cambio = 2
velocidad = 2
angle = 0
#Tolerancia para el centro
tol = 0.22
#Contabilizador de puntaje
marcador = 0
#--- Crear ventana para el juego ---
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("CAMCAR")
# --- Ocultar el puntero --- 
pygame.mouse.set_visible(0)
#Mediante la clase Group se añaden a una lista todas las monedas generadas
moneda_lista = pygame.sprite.Group()
enemigos_lista = pygame.sprite.Group()
#Se tiene tambien en cuenta el Carro del jugador
lista_sprites = pygame.sprite.Group()
#Enemigos
enemigos = 0
#Carro
car=Carro(x_coord,y_coord,pygame.image.load("Carro.png"),negro,'Player')
#Bandera para actualizar lista de enemigos
 # ---- Generación de monedas en posiciones aleatorias ----   
for i in range(4):
    # Esto representa una moneda
    moneda = Coin(20, 20, amarillo)
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
    # --- Comprobar el marcador y decidir la aparicion de los enemigos
    if flagScore:
        if marcador > 5:
            enemigos = 1
        elif marcador > 10:
            enemigos = 2
        elif marcador > 20:
            enemigos = 1
        elif marcador > 30:
            enemigos = 2
        elif marcador > 40:
            enemigos = 1
        elif marcador > 50:
            enemigos = 1
        elif marcador > 60:
            enemigos = 1
        else:
            enemigos = 0
        for i in range(enemigos):
            # Esto representa una moneda
            enemigo = Carro(rect_x, rect_y, pygame.image.load("Obstaculo1.png"), blanco, 'IA')
            # Añadimos cada moneda a la lista de objetos
            enemigos_lista.add(enemigo)
            lista_sprites.add(enemigo)
        flagScore = False
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
    #cv2.imshow('image', image)
# --- Bucle principal de eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True  
#        Al obtener la posición del rostro, se cambia la velocidad en X y Y
    if dir == 'l' and (x_coord>0):
        car.velx =- 5
        car.vely = 0
#        print('-')
    elif dir == 'r' and (x_coord<400):
        car.velx = 5
        car.vely = 0
#        print('+')
    elif dir == 'c':
#        print('0')
        car.velx = 0
        car.vely = 0
    elif dir == 'u' and (y_coord>0):
        car.vely =- 5
        car.velx = 0
#        print('++')
    elif dir == 'd' and (y_coord<400):
        car.vely = 5
        car.velx = 0
    else:
        car.velx = 0
        car.vely = 0

#   Limpiar pantalla
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    pantalla.fill(blanco)
    #Con rot podemos rotar la imagen del Carro dependiendo de la dirección de movimiento
    if car.vely or car.velx != 0:
        print('in')
        #rotamos a la posicion original antes de rotar de nuevo
        car.rot_center(-car.angle, car.velx, car.vely)
        if dir == 'u':
            car.rot_center(0, car.velx, car.vely)
        elif dir == 'l':
            car.rot_center(90, car.velx, car.vely)
        elif dir == 'r':
            car.rot_center(270, car.velx, car.vely)
        elif dir == 'd':
            car.rot_center(180, car.velx, car.vely)
        else:
            pass
    car.dir = dir

    for i in enemigos_lista:
        pantalla.blit(i.image, i.rect)

    pantalla.blit(car.image,car.rect)
    
# --- Se buscan colisiones del entre el Carro del jugadror y las monedas
    lista_impactos = pygame.sprite.spritecollide(car, moneda_lista, True)

    for moneda in lista_impactos:
        marcador += 1
        flagScore = True


# Dibujar monedas
    lista_sprites.draw(pantalla)
    
# ---- Comprobar colisiones entre Carros ----
    for i in enemigos_lista:
        if pygame.sprite.collide_rect(car, i):
            car.velx = 0
            car.vely = 0
            car.posx = 150
            car.posy = 290

#Score en pantalla 
    pantalla.blit(texto, [5, 5])
    font = pygame.font.Font(None, 25)
    text = font.render(str(marcador), 1, negro)
    pantalla.blit(text, (70,5))      
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 30 fotogramas por segundo (frames per second)
    reloj.tick(30)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
cap.release()
cv2.destroyAllWindows()
pygame.quit()