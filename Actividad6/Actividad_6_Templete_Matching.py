import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen principal y plantilla en escala de grises
imagen = cv2.imread("Actividad6\pug.jpg", cv2.IMREAD_GRAYSCALE)
plantilla = cv2.imread("Actividad6\pug2.png", cv2.IMREAD_GRAYSCALE)

# Obtener dimensiones de la plantilla
w, h = plantilla.shape[::-1]  

# Aplicar Template Matching con correlación normalizada
resultado = cv2.matchTemplate(imagen, plantilla, cv2.TM_CCOEFF_NORMED)

# Encontrar el mejor punto de coincidencia
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

# Coordenadas de la mejor coincidencia
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# Dibujar el rectángulo en la imagen original (convertida a color para visualizar)
imagen_color = cv2.imread("Actividad6\pug.jpg")  
cv2.rectangle(imagen_color, top_left, bottom_right, (0, 255, 0), 2)

# Mostrar el resultado
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(resultado, cmap="gray")
plt.title("Mapa de Coincidencia")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB))
plt.title("Detección en la Imagen Original")

plt.show()
