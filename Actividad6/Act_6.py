
import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_matching(image_path, template_path, method=cv2.TM_CCOEFF_NORMED):
    # Cargar la imagen y la plantilla en escala de grises
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    
    # Aplicar la correlación normalizada
    result = cv2.matchTemplate(image, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Seleccionar la mejor coincidencia
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Dibujar el rectángulo de coincidencia
    image_rgb = cv2.imread(image_path)
    cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
    
    # Mostrar los resultados
    plt.subplot(121), plt.imshow(result, cmap='gray')
    plt.title('Mapa de coincidencias'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Resultado final'), plt.xticks([]), plt.yticks([])
    plt.show()

# Uso del código
image_path = 'Actividad6\dino.jpg'  # Reemplaza con la ruta de tu imagen
template_path = 'Actividad6\dino2.png'     # Reemplaza con la ruta de tu plantilla
template_matching(image_path, template_path)
