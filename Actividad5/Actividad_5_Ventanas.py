import matplotlib.pyplot as plt
import numpy as np
from skimage import color, measure, filters, morphology
from skimage.io import imread
from skimage.measure import regionprops_table
import pandas as pd

# Cargar la imagen personalizada en escala de grises
image = imread("Actividad5\pared2.jpg")
gray_image = color.rgb2gray(image) if len(image.shape) == 3 else image

# Convertir a binario usando un umbral automático
thresh = filters.threshold_otsu(gray_image)
binary_image = gray_image > thresh

# Remover ruido con morfología matemática
cleaned_image = morphology.remove_small_objects(binary_image, 50)

# Etiquetar objetos
labeled_image = measure.label(cleaned_image)

# Obtener propiedades de los objetos
regions = measure.regionprops(labeled_image)

# Crear un DataFrame con las propiedades de las regiones
props = regionprops_table(labeled_image, properties=['label', 'area', 'perimeter', 'bbox'])
df = pd.DataFrame(props)
print(df)

# Mostrar imagen original con los bounding boxes
fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(gray_image, cmap='gray')
ax.set_title('Objetos detectados con Bounding Boxes')
ax.axis('off')

# Dibujar los bounding boxes
for region in regions:
    minr, minc, maxr, maxc = region.bbox
    rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr,
                         edgecolor='red', linewidth=2, fill=False)
    ax.add_patch(rect)

plt.show()
