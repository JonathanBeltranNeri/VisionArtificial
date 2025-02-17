# -*- coding: utf-8 -*-
"""
Jonathan Beltran Neri 22310188
"""
import cv2
import numpy as np

imagen = cv2.imread("Actividad2\manos.jpg")  # Cargar la imagen
m, n, c = imagen.shape  # Obtener dimensiones

imagenb = np.zeros((m, n), dtype=np.uint8)  # Imagen en escala de grises

for x in range(m):
    for y in range(n):
        if 111 < imagen[x, y, 0] < 255 and 145 < imagen[x, y, 1] < 208:
            imagenb[x, y] = 255  # Asignar blanco a los píxeles que cumplen la condición

cv2.imshow("manos", imagenb)  # Mostrar la imagen binaria
cv2.waitKey(0)
cv2.destroyAllWindows()
