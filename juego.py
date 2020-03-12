# -*- coding: utf-8 -*-
"""
@author: ALEXIS
"""

import pygame
import cv2
#import random

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


 
 
# Definicion de colores 
negro = (0, 0 ,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)
PI = 3.141592653

# Variables de control para el movimiento
dir = 'c'
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400,400]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("CAMCAR")

hecho = False 
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
#Posicion inicial obstaculos
rect_x = 100
rect_y = 50
#Posicion inicial carro
x_coord = 100
# Velocidad y direccion
rect_cambio = 2
pos_cambio = 0
velocidad = 3
#Ocultar el puntero 
pygame.mouse.set_visible(0)

#Imagen del carro
carro = pygame.image.load("llama.png").convert()
carro=pygame.transform.scale(carro,(70,70))
rectanguloCarro = carro.get_rect()
carro.set_colorkey(negro)
rectanguloCarro.top = 330

#Imagen del obstaculo1
obsta1 = pygame.image.load("Obstaculo1.png")#.convert()
obsta1.set_colorkey(negro)
rectobsta1 = obsta1.get_rect()

# --- Imagen del obstaculo2 ---
obsta2 = pygame.image.load("Obstaculo2.png")#.convert()
obsta2.set_colorkey(negro)
rectobsta2 = obsta2.get_rect()

# --- Score ---
fuente = pygame.font.Font(None, 25)
texto = fuente.render("Score:", True,negro)
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
        #Obtener dirección en base a la posición del rostro, 10% de tolerancia para el centro
        if (x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * 0.1) and (x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * 0.1):
            dir = 'c'
        elif x + w/2 < image.shape[1]/2:
            dir = 'l'
        elif x + w/2 > image.shape[1]/2:
            dir = 'r'
    # Mostrar el resultado
    cv2.imshow('image', image)
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True  
#        Al presionar las teclas de direccion, se cambia la velocidad
    if dir == 'l':
        pos_cambio =- 3
        print('-')
    elif dir == 'r':
        pos_cambio = 3
        print('+')
    elif dir == 'c':
        print('0')
        pos_cambio = 0
    print(pos_cambio)
    x_coord = x_coord + pos_cambio
    rect_y += velocidad
#   Limpiar pantalla
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    pantalla.fill(blanco)
# ---- Actualizar posiciones ----
    rectobsta1 = obsta1.get_rect()
    rectobsta1.left = rect_x
    rectobsta1.top = rect_y
    
    rectobsta2 = obsta1.get_rect()
    rectobsta2.left = rect_x+200
    rectobsta2.top = rect_y+6
    
    rectanguloCarro.left = x_coord
    
    
# ---- Comprobar colisiones ----
    if rectanguloCarro.colliderect( rectobsta1 ):
        velocidad=0
    if rectanguloCarro.colliderect( rectobsta2 ):
        velocidad=0
 
 # ---- Dibujamos objetos ----   
#Obstaculo 1  
    pantalla.blit(obsta1,rectobsta1)  
#Obstaculo 2  
    pantalla.blit(obsta2,rectobsta2)  
#Carro
    pantalla.blit(carro,rectanguloCarro)
#Score
    pantalla.blit(texto, [5, 5])
            
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

#pygame.draw.line(pantalla, verde, [0, 0], [100, 100], 5)
#    for desplazar_y in range(0, 100, 10):
#        pygame.draw.line(pantalla, rojo, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)
#        
#    pygame.draw.rect(pantalla, negro, [20, 20, 250, 100], 2)
#    pygame.draw.ellipse(pantalla, negro, [20, 20, 250, 100], 2) 
#    pygame.draw.arc(pantalla, negro, [20, 220, 250, 200], 0, PI / 2, 2)
#    pygame.draw.arc(pantalla, verde, [20, 220, 250, 200], PI / 2, PI, 2)
#    pygame.draw.arc(pantalla, azul, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
#    pygame.draw.arc(pantalla, rojo, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)
#    pygame.draw.polygon(pantalla, negro, [[100, 100], [0, 200], [200, 200]], 5)
#    
#    #Texto
#    fuente = pygame.font.Font(None, 25)
#    texto = fuente.render("Mi texto", True,negro)
#    pantalla.blit(texto, [250, 250])