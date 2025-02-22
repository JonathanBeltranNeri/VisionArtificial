import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image_path = "Actividad2\manos.jpg"  # Asegúrate de que la imagen esté en la misma carpeta o proporciona la ruta completa
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir a RGB

# Generar imágenes con diferente intensidad (atenuando la luminosidad)
image_light = np.clip(image * 0.7, 0, 255).astype(np.uint8)  # Reducir brillo ligeramente
image_dark = np.clip(image * 0.4, 0, 255).astype(np.uint8)   # Reducir brillo más

# Convertir a coordenadas cromáticas
def to_chromatic(img):
    img = img.astype(np.float32)
    sum_channels = np.sum(img, axis=2, keepdims=True) + 1e-6  # Evitar división por cero
    chromatic = img / sum_channels * 255  # Normalizar a 255
    return chromatic.astype(np.uint8)

image_chromatic = to_chromatic(image)
image_light_chromatic = to_chromatic(image_light)
image_dark_chromatic = to_chromatic(image_dark)

# Función mejorada para aplicar un clasificador basado en segmentación de color
def apply_classifier(img, threshold=100):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)  # Invertir para mejorar visibilidad
    return binary

# Aplicar clasificador a las tres imágenes
binary_original = apply_classifier(image)
binary_light = apply_classifier(image_light)
binary_dark = apply_classifier(image_dark)

# Aplicar clasificador a las imágenes en coordenadas cromáticas
binary_chromatic = apply_classifier(image_chromatic)
binary_light_chromatic = apply_classifier(image_light_chromatic)
binary_dark_chromatic = apply_classifier(image_dark_chromatic)

# Mostrar resultados
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
titles = ["Imagen Original", "Atenuada 1", "Atenuada 2"]
images = [
    (image, image_light, image_dark),
    (image_chromatic, image_light_chromatic, image_dark_chromatic),
    (binary_chromatic, binary_light_chromatic, binary_dark_chromatic)
]
labels = ["Imagen RGB", "Coordenadas Cromáticas", "Clasificación"]

for row in range(3):
    for col in range(3):
        axes[row, col].imshow(images[row][col], cmap="gray" if row == 2 else None)
        axes[row, col].axis("off")
        if col == 0:
            axes[row, col].set_ylabel(labels[row], fontsize=12, fontweight='bold')
        if row == 0:
            axes[row, col].set_title(titles[col])

plt.tight_layout()
plt.show()