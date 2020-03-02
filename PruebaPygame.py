# -*- coding: utf-8 -*-
"""


@author: ALEXIS
"""

import pygame
# import random
 
 
# Definicion de colores 
negro = (0, 0 ,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)
PI = 3.141592653
  
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400,400]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Prueba")
   
#Imagen del carro
carro = pygame.image.load("Carro.jpg").convert()

hecho = False 
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
#Posicion inicial obstaculos
rect_x = 50
rect_y = 50
#Posicion inicial carro
x_coord = 100
# Velocidad y direccion
rect_cambio = 2
pos_cambio = 0
#Ocultar el puntero 
pygame.mouse.set_visible(0)
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True  
#        Al presionar las teclas de direccion, se cambia la velocidad    
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pos_cambio =- 3
            elif evento.key == pygame.K_RIGHT:
                pos_cambio = 3
#       Vuelve a 0 si se suelta la tecla
        elif evento.type == pygame.KEYUP:
            # Si es una de las flechas, resetea el vector a cero.
            if evento.key == pygame.K_LEFT:
                pos_cambio = 0
            elif evento.key == pygame.K_RIGHT:
                pos_cambio = 0
    x_coord = x_coord + pos_cambio
    rect_y += 1
#   Limpiar pantalla
    pantalla.fill(blanco)
    
#Obstaculo 1  
    pygame.draw.rect(pantalla, negro, [rect_x, rect_y, 70, 50])
    pygame.draw.rect(pantalla, rojo, [rect_x + 10, rect_y + 10, 50, 30])
    
#Obstaculo 2  
    pygame.draw.rect(pantalla, negro, [rect_x+200, rect_y, 70, 50])
    pygame.draw.rect(pantalla, rojo, [rect_x + 210, rect_y + 10, 50, 30])

#Carro
    pantalla.blit(pygame.transform.scale(carro,(70,70)), [x_coord, 330])
#    pygame.draw.rect(pantalla, negro, [x_coord, 330, 50, 20])
# 
            
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
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