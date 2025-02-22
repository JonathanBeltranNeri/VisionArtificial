##Jonathan Beltran Neri 22310188
##Actividad IV: White Patch
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("Actividad2/manos.jpg")  
if image is None:
    raise FileNotFoundError("No se pudo cargar la imagen. Verifica la ruta y el nombre del archivo.")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB

# Generar imágenes con tinte rojo y verde
image_red = image.copy()
image_green = image.copy()

image_red[:, :, 1] = np.clip(image_red[:, :, 1] * 0.5, 0, 255)  # Reducir verde
image_red[:, :, 2] = np.clip(image_red[:, :, 2] * 1.5, 0, 255)  # Aumentar rojo

image_green[:, :, 0] = np.clip(image_green[:, :, 0] * 0.5, 0, 255)  # Reducir azul
image_green[:, :, 1] = np.clip(image_green[:, :, 1] * 1.5, 0, 255)  # Aumentar verde

# Función para aplicar el algoritmo White Patch
def white_patch(img):
    max_values = np.max(img, axis=(0, 1))
    corrected_img = (img / max_values) * 255
    return np.clip(corrected_img, 0, 255).astype(np.uint8)

# Aplicar White Patch a las imágenes
wp_original = white_patch(image)
wp_red = white_patch(image_red)
wp_green = white_patch(image_green)

# Función para clasificar con el método de Otsu
def apply_otsu_threshold(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

# Aplicar el clasificador inicial (antes de White Patch)
binary_original = apply_otsu_threshold(image)
binary_red = apply_otsu_threshold(image_red)
binary_green = apply_otsu_threshold(image_green)

# Aplicar el clasificador después del White Patch
binary_wp_original = apply_otsu_threshold(wp_original)
binary_wp_red = apply_otsu_threshold(wp_red)
binary_wp_green = apply_otsu_threshold(wp_green)

# Mostrar resultados en columnas
fig, axes = plt.subplots(4, 3, figsize=(10, 15))
titles = ["Imagen Original", "Imagen Roja", "Imagen Verde",
          "White Patch - Original", "White Patch - Roja", "White Patch - Verde",
          "Clasificador Inicial - Original", "Clasificador Inicial ", "Clasificador Inicial",
          "Clasificador Adaptado ", "Clasificador Adaptado ", "Clasificador Adaptado "]

images = [image, image_red, image_green,
          wp_original, wp_red, wp_green,
          binary_original, binary_red, binary_green,
          binary_wp_original, binary_wp_red, binary_wp_green]

for i, ax in enumerate(axes.flatten()):
    if i < len(images):
        if len(images[i].shape) == 2:  # Si es una imagen binaria
            ax.imshow(images[i], cmap='gray')
        else:
            ax.imshow(images[i])
        ax.set_title(titles[i])
        ax.axis('off')
    else:
        ax.axis('off')  # Ocultar ejes si no hay imagen para mostrar

plt.tight_layout()
plt.show()