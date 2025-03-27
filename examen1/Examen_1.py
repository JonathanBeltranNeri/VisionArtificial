## Jonathan Beltran Neri 22310188
## 6E vision artificial 
# Examen primer parcial 

import numpy as np
import cv2
from scipy.ndimage import convolve

# Cargar la imagen en escala de grises
image = cv2.imread("examen1\\ajolote.jpg", cv2.IMREAD_GRAYSCALE)

# Duplicar el borde de la imagen
image_padded = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_REFLECT)

# Filtro I - Laplaciano discreto en 2D
laplacian_kernel = np.array([[0, 1, 0],
                              [1, -4, 1],
                              [0, 1, 0]])

filtered_image_1 = convolve(image_padded.astype(float), laplacian_kernel)
filtered_image_1 = np.clip(filtered_image_1[1:-1, 1:-1], 0, 255).astype(np.uint8)

# Guardar la imagen original y la filtrada en formato .npy
np.save("22310188filtro1.npy", {"original": image, "filtrada": filtered_image_1})

# Filtro II - Matriz dada
custom_kernel = np.array([[1, 1, 1],
                          [1, -8, 1],
                          [1, 1, 1]])

filtered_image_2 = convolve(image_padded.astype(float), custom_kernel)
filtered_image_2 = np.clip(filtered_image_2[1:-1, 1:-1], 0, 255).astype(np.uint8)

# Guardar la imagen original y la filtrada en formato .npy
np.save("22310188filtro2.npy", {"original": image, "filtrada": filtered_image_2})

# Configurar las ventanas para que se abran en tamaño pequeño
cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Filtro Laplaciano", cv2.WINDOW_NORMAL)
cv2.namedWindow("Filtro Personalizado", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Imagen Original", 400, 400)
cv2.resizeWindow("Filtro Laplaciano", 400, 400)
cv2.resizeWindow("Filtro Personalizado", 400, 400)

# Mostrar las imágenes en ventanas separadas
cv2.imshow("Imagen Original", image)
cv2.imshow("Filtro Laplaciano", filtered_image_1)
cv2.imshow("Filtro Personalizado", filtered_image_2)

cv2.waitKey(0)  # Esperar hasta que se presione una tecla
cv2.destroyAllWindows()  # Cerrar las ventanas


