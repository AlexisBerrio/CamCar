import pygame
import cv2
import random
from classes import Carro,Coin


#from pygame.locals import *

# Clasificador de rostros en vista fontal, usa la técnica HAAR y entrega el rectangulo de la cara
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Se habilita la camara integrada
cap = cv2.VideoCapture(0)

# Inicialización de los componentes de Pygame
pygame.init()

# Definicion de colores 
#        R  G  B
negro = (0, 0 ,0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)

# ---- Declaración de variables ----
# Variables de control para el movimiento
dir = 'c'
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400,400]

# Variable para habilitar el loop principal
hecho = True
hecho1 = True
while hecho1:
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho1 = False  
    # Se usa para establecer cuan rápido se actualiza la pantalla
    reloj = pygame.time.Clock()
    #Posicion inicial obstaculos
    rect_x = 25
    rect_y = 35
    #Posicion inicial Carro
    x_coord = 150
    y_coord = 290
    # Dirección y ángulo
    pos_cambio = 0
    pos_cambioy = 0
    angle = 0
    #Tolerancia para el centro
    tol = 0.22
    #Contabilizador de puntaje
    marcador = 0
    tope = 1
    #--- Crear ventana para el juego ---
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("CAMCAR")
    background_image = pygame.image.load("Back.jpg")
    Inic = pygame.image.load("Inicio.png")
    # --- Ocultar el puntero --- 
    pygame.mouse.set_visible(0)
    #Mediante la clase Group se añaden a una lista todas las monedas generadas
    moneda_lista = pygame.sprite.Group()
    enemigos_lista = pygame.sprite.Group()
    #Se tiene tambien en cuenta el Carro del jugador
    lista_sprites = pygame.sprite.Group()
    
    
    #Obstaculo 2
    #Carro
    car=Carro(x_coord,y_coord,pygame.image.load("Carro.png"),negro,'Player')
    
    # --- Score ---
    fuente = pygame.font.Font(None, 25)
    texto = fuente.render("Score:", True,blanco)
    # --- Game Over ---
    fuente2 = pygame.font.Font(None, 70)
    final = fuente2.render("Game Over", True,blanco)
    # --- Inicio ---
    fuente3 = pygame.font.Font(None, 40)
    inicio = fuente3.render("Pulse una tecla para iniciar", True,rojo)
    
    pantalla.blit(Inic, [0, 0])
    pantalla.blit(inicio, [10, 200])
    pygame.display.flip()
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
                hecho1 = False  
                hecho = True
    #        Al obtener la posición del rostro, se cambia la velocidad en X y Y
        if dir == 'l' and (x_coord>0):
            pos_cambio =- 4
            pos_cambioy = 0
    #        print('-')
        elif dir == 'r' and (x_coord<400):
            pos_cambio = 4
            pos_cambioy = 0
    #        print('+')
        elif dir == 'c':
    #        print('0')
            pos_cambio = 0
            pos_cambioy = 0
        elif dir == 'u' and (y_coord>0):
            pos_cambioy =- 4
            pos_cambio = 0
    #        print('++')
        elif dir == 'd' and (y_coord<400):
            pos_cambioy = 4
            pos_cambio = 0
        else:
            pos_cambio = 0
            pos_cambioy = 0
    #        print('--')
    #    print(pos_cambio)
        pantalla.blit(background_image, [0, 0])
        x_coord = x_coord + pos_cambio
        y_coord = y_coord + pos_cambioy
    #   Limpiar pantalla
        if cv2.waitKey(1) & 0xFF == ord('q'):
            hecho1 = False
            break
        # pantalla.fill(blanco)
        #Con rot podemos rotar la imagen del Carro dependiendo de la dirección de movimiento
        
         # ---- Generación de monedas en posiciones aleatorias ----   
        if tope == 1:
            tope = 0
            moneda_lista.empty()
            lista_sprites.empty()
            for i in range(marcador + 5):
                # Esto representa una moneda
                moneda = Coin(20, 20)
                # Establecemos una ubicación aleatoria para cada moneda
                moneda.rect.x = random.randrange(30,400-30)
                moneda.rect.y = random.randrange(50,400-30) 
                # Añadimos cada moneda a la lista de objetos
                moneda_lista.add(moneda)    
                lista_sprites.add(moneda)
                
                # Ahora para los obstaculos
            if marcador == 0 or marcador == 5 or marcador == 10 or marcador == 15:
            #Obstaculo
                enemigo=Carro(rect_x,rect_y,pygame.image.load("Obstaculo1.png"),blanco,'IA')   
            # if marcador == 5:
            #Obstaculo 1
                # obsta2=Carro(rect_x+200,rect_y+6,pygame.image.load("Obstaculo2.png"),negro,'IA')
                # o2 = 1
            enemigos_lista.add(enemigo)
            lista_sprites.add(enemigo)
    
        if pos_cambioy or pos_cambio != 0:
            # print('in')
            #rotamos a la posicion original antes de rotar de nuevo
            car.rot_center(-car.angle, x_coord, y_coord)
            if dir == 'u':
                car.rot_center(0, x_coord, y_coord)
            elif dir == 'l':
                car.rot_center(90, x_coord, y_coord)
            elif dir == 'r':
                car.rot_center(270, x_coord, y_coord)
            elif dir == 'd':
                car.rot_center(180, x_coord, y_coord)
            else:
                pass
        car.dir = dir
        
        for i in enemigos_lista:
    # pantalla.blit(i.image, i.rect)
            i.move_IA()
            pantalla.blit(i.image,i.rect)
    
        pantalla.blit(car.image,car.rect)
        
    # --- Se buscan colisiones del entre el Carro del jugadror y las monedas
        lista_impactos = pygame.sprite.spritecollide(car, moneda_lista, True) 
        for moneda in lista_impactos:
            marcador += 1   
            if marcador % 5 == 0:
                tope = 1
    #        print( marcador )
    # Dibujar monedas
        lista_sprites.draw(pantalla)
        # Dibujar enemigos
        enemigos_lista.draw(pantalla)
        
    # ---- Comprobar colisiones entre Carros ----
        for i in enemigos_lista:
            if pygame.sprite.collide_rect(car, i) == True:
                i.velx = 0
                i.vely = 0
                pantalla.blit(final, (90,190))
                pygame.display.flip()
                pygame.time.wait(2000)
                hecho = True
    #Score en pantalla 
        pantalla.blit(texto, [5, 5])
        font = pygame.font.Font(None, 25)
        text = font.render(str(marcador), 1, blanco)
        pantalla.blit(text, (70,5))      
        # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
     
        # --- Limitamos a 60 fotogramas por segundo (frames per second)
        reloj.tick(30)
        
    # Cerramos la ventana y salimos.
    # Si te olvidas de esta última línea, el programa se 'colgará'
    # al salir si lo hemos estado ejecutando desde el IDLE.
            
cap.release()
cv2.destroyAllWindows()
pygame.quit()