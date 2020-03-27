<<<<<<< HEAD
  
=======
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
# --------------------------------------------------------------------------
# ------- CARCAM Juego - Primera entrega  ----------------------------------
# ------- Procesamiento digital de imagenes --------------------------------
# ------- Por: Juan S. Guerrero    jsebastian.guerrero@udea.edu.co  --------
# -------      Johan Alexis Berrío        johan.berrio@udea.edu.co  --------
# -------      Estudiantes  ------------------------------------------------
# ------- Marzo de 2020  ---------------------------------------------------
# --------------------------------------------------------------------------
<<<<<<< HEAD

# --------------------------------------------------------------------------
# --1. Inicializar el sistema, importar dependencias y clases  -------------
# --------------------------------------------------------------------------
import pygame  # librería que contiene la API para el juego
import cv2  # librería OpenCV
import random  # librería para producir numeros aleatorios
from classes import Carro, Coin  # clases para las entidades del juego

# --------------------------------------------------------------------------
# --2. Cargar el modelo pre-entrenado para deteccion de rostros  -----------
# --------------------------------------------------------------------------

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# --------------------------------------------------------------------------
# --3. Inicializar camara web  ---------------------------------------------
# --------------------------------------------------------------------------

cap = cv2.VideoCapture(0)

# --------------------------------------------------------------------------
# --4. Inicializar la API PyGame  ------------------------------------------
# --------------------------------------------------------------------------

=======

# --------------------------------------------------------------------------
# --1. Inicializar el sistema, importar dependencias y clases  -------------
# --------------------------------------------------------------------------
import pygame  # librería que contiene la API para el juego
import cv2  # librería OpenCV
import random  # librería para producir numeros aleatorios
from classes import Carro, Coin  # clases para las entidades del juego

# --------------------------------------------------------------------------
# --2. Cargar el modelo pre-entrenado para deteccion de rostros  -----------
# --------------------------------------------------------------------------

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# --------------------------------------------------------------------------
# --3. Inicializar camara web  ---------------------------------------------
# --------------------------------------------------------------------------

cap = cv2.VideoCapture(-1)

# --------------------------------------------------------------------------
# --4. Inicializar la API PyGame  ------------------------------------------
# --------------------------------------------------------------------------

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
pygame.init()

# --------------------------------------------------------------------------
# --5. Declaracion de variables iniciales y recursos  ----------------------
# --------------------------------------------------------------------------
# -- Definicion de colores para filtrar fondos de imágenes usadas para los elementos del juego --
<<<<<<< HEAD
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
#        R  G  B
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
violeta = (98, 0, 255)

<<<<<<< HEAD
# -- Declaración de variables referentes al sonido del juego --
Coin_sound = pygame.mixer.Sound("CoinGet.ogg")
GameOver = pygame.mixer.Sound("final.wav")
music= pygame.mixer.music.load("music.wav")

# -- Declaración de variables de control para el movimiento en el juego --
dir = 'c' # Direccion inicial del carro
dimensiones = [400, 400] # Establecemos las dimensiones de la pantalla [largo,altura]
hecho1 = True # Variable para habilitar el loop de reinicio del juego
hecho = True # Variable para habilitar el loop principal   
=======
# -- Declaración de variables de control para el movimiento en el juego --

dir = 'c' # Direccion inicial del carro
dimensiones = [400, 400] # Establecemos las dimensiones de la pantalla [largo,altura]
hecho1 = True # Variable para habilitar el loop de reinicio del juego
hecho = True # Variable para habilitar el loop principal
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c

# --------------------------------------------------------------------------
# --6. Inialiacion del programa  -------------------------------------------
# --------------------------------------------------------------------------

# -- Evento principal en la ventana  ---------------------------------------

while hecho1: # mientras la bandera de ejecucion sea True, el juego corre
<<<<<<< HEAD
    
    # Iniciar musica de fondo
    pygame.mixer.music.play(-1)
    
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # -- Evento de pulsacion para salir del juego --

    for evento in pygame.event.get(): # se revisa cada evento que ocurre en el juego
        if evento.type == pygame.QUIT: # se revisa si el evento es de salir
            hecho1 = False # se termina el juego poniendo esta bander en falso
<<<<<<< HEAD
            
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # -- Se establece el tiempo de refresco de los eventos en el juego --

    reloj = pygame.time.Clock() # Inicializar tiempo

    # -- Iniciar posicion de obstaculos --

    rect_x = 25 # Posicion x inicial de obstaculos
    rect_y = 35 # Posicion y inicial de obstaculos

    # -- Posicion inicial del Carro jugador --

    x_coord = 150 # Coordenada x
    y_coord = 290 # Coordenada y

    # -- Variables iniciales del jugador --

    pos_cambio = 0 # posicion en x
    pos_cambioy = 0 # posicion en y
    angle = 0 # angulo inicial al que el jugador esta viendo
    tol = 0.22 # Tolerancia en el centro para cuando cambia a la posición del rostro
    marcador = 0 # Contabilizador de puntaje
    tope = 1 # Tope se activa cuando se llega a ciertos puntajes, sube de nivel
<<<<<<< HEAD
    
    
        # --- Instanciar ventana para el juego ---
=======

    # --- Instanciar ventana para el juego ---
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # La instancia de display permite crear la ventana
    pantalla = pygame.display.set_mode(dimensiones)
    # Nombre de la ventana
    pygame.display.set_caption("CAMCAR")
    # Cargar en el fondo la imagen de fondo del juego
    background_image = pygame.image.load("Back.jpg")
    # Carga en una variable la imagen de fondo del menú de inicio
    Inic = pygame.image.load("Inicio.png")
    pygame.mouse.set_visible(0) # Ocultar el puntero
<<<<<<< HEAD
    
    
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # --- Contenedores para entidades: monedas y enemigos ---

    # Mediante la clase Group se puede agregar objetos para deteccion de colision y para la mecanica del juego
    # Instanciar grupo de monedas
    moneda_lista = pygame.sprite.Group()
    # Instanciar grupo de enemigos
    enemigos_lista = pygame.sprite.Group()
    # Instancia para almacenar las imagenes que corresponden a las entidades
    lista_sprites = pygame.sprite.Group()
<<<<<<< HEAD
    
    # Carro, recibe coordenadas en X y Y, su imagen, su color de fondo
    # y una etiqueda para diferenciarlo de la IA
    car = Carro(x_coord, y_coord, pygame.image.load("Carro.png"), negro, 'Player')      
    
    
    # --- Variables para texto en pantalla. ---
    
    
        # Puntaje
=======

    # --- Instanciar jugador ---

    # Carro, recibe coordenadas en X y Y, su imagen, su color de fondo
    # y una etiqueda para diferenciarlo de la IA
    car = Carro(x_coord, y_coord, pygame.image.load("Carro.png"), negro, 'Player')

    # --- Variables para texto en pantalla. ---

    # Puntaje
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # Función que recibe el tipo de letra y el tamano, None por defecto
    fuente = pygame.font.Font(None, 25)
    # Crea una superficie para poner el texto 
    texto = fuente.render("Score:", True, blanco)
    # Fin de juego
    fuente2 = pygame.font.Font(None, 70)
    final = fuente2.render("Game Over", True, blanco)
    # Inicio
    fuente3 = pygame.font.Font(None, 40)
    inicio = fuente3.render("Pulse una tecla para iniciar", True, rojo)
    # Ubica una imagen en la pantalla, recibe la imagen y la posición incial
    pantalla.blit(Inic, [0, 0])
    # En este caso, ubica en pantalla la superficie con el texto inicial.
    pantalla.blit(inicio, [10, 200])
    # flip se encarga de actualizar la pantalla con lo anterior
    pygame.display.flip()
<<<<<<< HEAD
    
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    # --------------------------------------------------------------------------
    # --7. Ciclo principal del juego -------------------------------------------
    # --------------------------------------------------------------------------

    # -------- Bucle de espera del Programa -----------
<<<<<<< HEAD
    
    
    # --- Bucle que espera que se presione una tecla para empezar el juego ---
    while hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                hecho = False
    
    # -------- Bucle principal del Programa -----------
=======

    while hecho: # bandera para mantener en espera hasta presionar tecla abajo
        for evento in pygame.event.get(): # escuchador de eventos
            if evento.type == pygame.KEYDOWN: # revisar si fue una tecla abajo
                hecho = False # cambiar bandera para iniciar juego

    # -------- Bucle de ejecucion del Programa -----------

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
    while not hecho: # bandera para mantener el juego hasta que se cierre
        # Captura frame-by-frame
        ret, image = cap.read()
        # Reflejar la imagen con respecto al eje y
        image = cv2.flip(image, 1)
        # Pasar cada frame a escala de grises
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        """Aplicar clasificador de rostros frontales
        Recibe la imagen, el factor de reducción de la imagen en cada escala
        y la cantidad de vecinos minima que debe tener un rectángulo para tenerlo
        en cuenta. Entrega la posición del rectángulo del rostro
        """
        face = face_classifier.detectMultiScale(gris, 1.3, 5)
               # Seguimiento del rostro mediante un rectangulo
        for (x, y, w, h) in face:
            # Dibuja un rectángulo azul alrededor del rostro
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
            """Obtener dirección en base a la posición del rostro, 22% de tolerancia para el centro
            Se busca ubicar la posicion del rostro en uno de los 5 posibles puntos:
                Centro, arriba, abajo, derecha o izquierda"""
            if (x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (
                    x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol) and (
                    y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (
                    y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
                dir = 'c' # direccion al centro
            elif x + w / 2 < image.shape[1] / 2 and (
                    y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (
                    y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
                dir = 'l' # direccion a la izquierda
            elif x + w / 2 > image.shape[1] / 2 and (
                    y + h / 2 > image.shape[0] / 2 - image.shape[0] / 2 * tol) and (
                    y + h / 2 < image.shape[0] / 2 + image.shape[0] / 2 * tol):
                dir = 'r' # direccion a la derecha
            elif y + h / 2 < image.shape[0] / 2 and (
                    x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (
                    x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol):
                dir = 'u' # direccion a arriba
            elif y + h / 2 > image.shape[0] / 2 and (
                    x + w / 2 > image.shape[1] / 2 - image.shape[1] / 2 * tol) and (
                    x + w / 2 < image.shape[1] / 2 + image.shape[1] / 2 * tol):
                dir = 'd' # direccion a abajo
<<<<<<< HEAD
    
        # Mostrar el resultado de la captura de vídeo
        cv2.imshow('image', image)
        
        
        
=======

        # Mostrar el resultado de la captura de vídeo
        cv2.imshow('image', image)


>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # --- Bucle principal de eventos de Pygame ---

        # Se sale del juego al presionar "salir"
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho1 = False
                hecho = True
<<<<<<< HEAD
                
                
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        #  Al presionar 'q'en la ventana de opencv, termina el ciclo actual
        #  cambiando la banera hecho1 a Falso y rompiendo el ciclo principal
        if cv2.waitKey(1) & 0xFF == ord('q'):
            hecho1 = False
            break
<<<<<<< HEAD
        
        
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # Al obtener la posición del rostro, se cambia la velocidad en X y Y
        # Se limitan los movimientos al tamaño de la pantalla y se asigna
        # velocidad en una direccion dada por el rastreo de rostro
        if dir == 'l' and (x_coord > 0):
            pos_cambio = - 4
            pos_cambioy = 0
        elif dir == 'r' and (x_coord < 400):
            pos_cambio = 4
            pos_cambioy = 0
        elif dir == 'c':
            pos_cambio = 0
            pos_cambioy = 0
        elif dir == 'u' and (y_coord > 0):
            pos_cambioy = - 4
            pos_cambio = 0
        elif dir == 'd' and (y_coord < 400):
            pos_cambioy = 4
            pos_cambio = 0
        # Cuando el rostro está el el centro, no puede haber movimiento
        else:
            pos_cambio = 0
            pos_cambioy = 0
            
            
        #  Muestra en pantalla la imagen de fondo
        pantalla.blit(background_image, [0, 0])
        # Actualiza las coordenadas del carro para hacer que se mueva 
        x_coord = x_coord + pos_cambio # actualizar coordenada x
        y_coord = y_coord + pos_cambioy # actualizar coordenada y
<<<<<<< HEAD
            
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # ---- Generación de monedas en posiciones aleatorias ----

        # Cuando se "suba de nivel, genera mas monedas" y se añade un enemigo
        if tope == 1: # tope representa subir de nivel
            tope = 0 # se desactiva la subida para no seguir subiendo
            moneda_lista.empty() # se vacian las monedas
            lista_sprites.empty() # se vacian las imagenes de los objetos
            for i in range(marcador + 5): #segun el marcador apareceran mas monedas
                # Esto representa una moneda
                moneda = Coin(20, 20)
                # Establecemos una ubicación aleatoria para cada moneda
                moneda.rect.x = random.randrange(30, 400 - 30)
                moneda.rect.y = random.randrange(50, 400 - 30)
                # Añadimos cada moneda a la lista de objetos
                moneda_lista.add(moneda)
                lista_sprites.add(moneda)
<<<<<<< HEAD
                
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
            # ---- Generación de enemigos en posiciones aleatorias ----

            # Ahora para los obstaculos, enemigo cada 5 monedas
            # en base al marcador
            if marcador == 0 or marcador == 5 or marcador == 10 or marcador == 15:
                # Obstaculo, la misma clase del carro, solo que la etiqueda indica que no es controlado por el jugador
                enemigo = Carro(rect_x, rect_y, pygame.image.load("Obstaculo1.png"), blanco, 'IA')
            # Se añade el nuevo objeto a la lista de sprites y a la lista de enemigos
            enemigos_lista.add(enemigo)
            lista_sprites.add(enemigo)
<<<<<<< HEAD
            
            
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # ---- Rotación y movimiento del jugador ----
        if pos_cambioy or pos_cambio != 0:
            # Con rot podemos rotar la imagen del Carro dependiendo de la dirección de movimiento
            # Rotamos a la posicion original antes de rotar de nuevo
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
<<<<<<< HEAD
            
            
        # -- Se le asigna la direccion del rostro al carro del jugador
        car.dir = dir
        
        
        # -- Genera el movimiento de los carros de la IA  y los muestra en pantalla
=======

        # -- Se le asigna la direccion del rostro al carro del jugador
        car.dir = dir

        # -- Genera el moviiento de los carros de la IA  y los muestra en pantalla
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        for i in enemigos_lista:
            # Realiza la interacción por cada carro de la IA en pantalla
            # cada enemigo se mueve de forma aleatoria mediante el metodo move_IA (clases)
            i.move_IA()
            pantalla.blit(i.image, i.rect)

        # -- Muestra y actualiza el carro del jugador, recibe la imagen y su rectángulo
        pantalla.blit(car.image, car.rect)
<<<<<<< HEAD
        
        
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # --- Se buscan colisiones del entre el Carro del jugadror y las monedas
        """La función revisa si los rectángulos de los objetos se superponen, de
        ser así, aumenta en 1 su contador por cada colisión,recibe el carro del jugador,
        la lista de monedas y el tipo de verificación 
        """
        lista_impactos = pygame.sprite.spritecollide(car, moneda_lista, True)
        for moneda in lista_impactos:
<<<<<<< HEAD
            Coin_sound.play() #Se emite un sonido al detectar una colisión con monedas
            marcador += 1   
            # Cada 5 monedas obtenidas, se sube de nivel 
            if marcador % 5 == 0:
                tope = 1
                
=======
            marcador += 1
            # Cada 5 monedas obtenidas, se sube de nivel 
            if marcador % 5 == 0:
                tope = 1
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # Dibujar monedas
        lista_sprites.draw(pantalla)
        # Dibujar enemigos
        enemigos_lista.draw(pantalla)
<<<<<<< HEAD
        
=======

>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        # ---- Comprobar colisiones entre Carros ----
        for i in enemigos_lista:
            # Detecta la colisión entre los rectángulos de los enemigos y jugador
            if pygame.sprite.collide_rect(car, i) == True:
                # Cuando hay colisión, para el movimiento de la IA y reinicia el juego
                i.velx = 0
                i.vely = 0
                # Se imprime un aviso de game over
                pantalla.blit(final, (90, 190))
                pygame.display.flip()
                GameOver.play()
                # Se esperan 2000 ms antes de reiniciar
                pygame.time.wait(2000)
                hecho = True
<<<<<<< HEAD
# Score en pantalla
=======
        # Score en pantalla
>>>>>>> 7c7495a862eab90d8332e4b15318095d3041739c
        pantalla.blit(texto, [5, 5])
        font = pygame.font.Font(None, 25)
        text = font.render(str(marcador), 1, blanco)
        pantalla.blit(text, (70, 5))
        # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
        # --- Limitamos a 60 fotogramas por segundo (frames per second)
        reloj.tick(30)
cap.release() # Cierra la ventana de la camara web
cv2.destroyAllWindows() # destruye las ventanas de OpenCV
pygame.quit() # Termina el programa
#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA -----------------------------
#--------------------------------------------------------------------------