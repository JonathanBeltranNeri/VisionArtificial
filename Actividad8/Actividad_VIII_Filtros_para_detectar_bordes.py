import cv2
import numpy as np
import matplotlib.pyplot as plt  # Importar Matplotlib

# Paso 1: Leer la imagen en escala de grises
image_path = r'Actividad5\ladrillos.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Error: No se pudo cargar la imagen en la ruta: {image_path}")
    exit()

# Paso 2: Definir los kernels de Sobel
kernel_vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Paso 3: Aplicar filtros de detección de bordes
edges_vertical = cv2.filter2D(image, cv2.CV_64F, kernel_vertical)
edges_horizontal = cv2.filter2D(image, cv2.CV_64F, kernel_horizontal)
magnitude = np.sqrt(edges_vertical**2 + edges_horizontal**2)

# Convertir a uint8 para visualización
edges_vertical = cv2.convertScaleAbs(edges_vertical)
edges_horizontal = cv2.convertScaleAbs(edges_horizontal)
magnitude = cv2.convertScaleAbs(magnitude)

# Mostrar imágenes con Matplotlib
plt.figure(figsize=(10, 4))

plt.subplot(1, 4, 1)
plt.title("Imagen Original")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Bordes Verticales")
plt.imshow(edges_vertical, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.title("Bordes Horizontales")
plt.imshow(edges_horizontal, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Magnitud del Gradiente")
plt.imshow(magnitude, cmap="gray")
plt.axis("off")

plt.show()
