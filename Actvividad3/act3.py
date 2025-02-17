# -*- coding: utf-8 -*-
"""
Jonathan Beltran Neri 22310188
"""
import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread("Actividad2\\manos.jpg")  # Cambia la ruta si es necesario
m, n, c = imagen.shape  # Obtener dimensiones

# 1. Modificar la intensidad de la imagen (aumento del brillo)
factor = 1.5  # Aumentamos el brillo en un 50%
imagen_modificada = cv2.convertScaleAbs(imagen, alpha=factor, beta=0)

# 2. Reducir la intensidad de la imagen (disminución del brillo)
factor_reduccion = 0.5  # Reducimos el brillo en un 50%
imagen_reducida = cv2.convertScaleAbs(imagen, alpha=factor_reduccion, beta=0)

# 3. Convertir a escala de grises (original, modificada y reducida)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_modificada_gris = cv2.cvtColor(imagen_modificada, cv2.COLOR_BGR2GRAY)
imagen_reducida_gris = cv2.cvtColor(imagen_reducida, cv2.COLOR_BGR2GRAY)

# 4. Crear imágenes binarias
imagenb_original = np.zeros((m, n), dtype=np.uint8)
imagenb_modificada = np.zeros((m, n), dtype=np.uint8)
imagenb_reducida = np.zeros((m, n), dtype=np.uint8)

# Umbral para la binarización según los valores de los canales de la imagen original, modificada y reducida
for x in range(m):
    for y in range(n):
        # Para la imagen original
        if 111 < imagen[x, y, 0] < 255 and 145 < imagen[x, y, 1] < 208:
            imagenb_original[x, y] = 255
        # Para la imagen modificada
        if 111 < imagen_modificada[x, y, 0] < 255 and 145 < imagen_modificada[x, y, 1] < 208:
            imagenb_modificada[x, y] = 255
        # Para la imagen reducida
        if 111 < imagen_reducida[x, y, 0] < 255 and 145 < imagen_reducida[x, y, 1] < 208:
            imagenb_reducida[x, y] = 255

# Mostrar las imágenes
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Modificada", imagen_modificada)
cv2.imshow("Imagen Reducida", imagen_reducida)

cv2.imshow("Escala de Grises Original", imagen_gris)
cv2.imshow("Escala de Grises Modificada", imagen_modificada_gris)
cv2.imshow("Escala de Grises Reducida", imagen_reducida_gris)

cv2.imshow("Imagen Binaria Original", imagenb_original)
cv2.imshow("Imagen Binaria Modificada", imagenb_modificada)
cv2.imshow("Imagen Binaria Reducida", imagenb_reducida)

cv2.waitKey(0)
cv2.destroyAllWindows()
