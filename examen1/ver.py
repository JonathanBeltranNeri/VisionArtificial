import numpy as np

archivo = "22310188filtro1.npy"
data = np.load(archivo, allow_pickle=True).item()  # Convertir a diccionario

original = data["original"]
filtrada = data["filtrada"]

print("Dimensiones de la imagen original:", original.shape)
print("Dimensiones de la imagen filtrada:", filtrada.shape)

# Mostrar las imágenes
import cv2
cv2.imshow("Imagen Original", original)
cv2.imshow("Imagen Filtrada", filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()
