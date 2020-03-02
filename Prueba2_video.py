
import numpy as np
import cv2
import matplotlib.pyplot as plt


face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   
cap = cv2.VideoCapture(0)

while(True):
    # Captura frame-by-frame
    ret, image = cap.read()
    #Pasar cada frame a escala de grises 
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Aplicar clasificador de rostros frontales
    face= face_classifier.detectMultiScale(gris,1.3,5)
    #Seguimiento del rostro mediante un rectangulo
    for(x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)  
    # Mostrar el resultado
    cv2.imshow('image',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
cap.release()
cv2.destroyAllWindows()

    