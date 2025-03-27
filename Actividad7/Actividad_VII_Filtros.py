import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, sigma=15):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.int16)
    noisy_image = np.clip(image.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_image

def add_salt_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = image.copy()
    num_salt = np.ceil(salt_prob * image.size).astype(int)
    num_pepper = np.ceil(pepper_prob * image.size).astype(int)
    
    coords_salt = [np.random.randint(0, i, num_salt) for i in image.shape]
    coords_pepper = [np.random.randint(0, i, num_pepper) for i in image.shape]
    
    noisy_image[tuple(coords_salt)] = 255
    noisy_image[tuple(coords_pepper)] = 0
    
    return noisy_image

def apply_filters(image):
    return {
        "Gaussian": cv2.GaussianBlur(image, (5, 5), 0),
        "Mean": cv2.blur(image, (5, 5)),
        "Median": cv2.medianBlur(image, 7),
        "Min": cv2.erode(image, np.ones((3,3), np.uint8)),
        "Max": cv2.dilate(image, np.ones((3,3), np.uint8))
    }

def show_images(images_dict, title):
    plt.figure(figsize=(12, 8))
    num_images = len(images_dict)
    rows = 3
    cols = 4 if num_images > 8 else (num_images // 3 + 1)
    
    for i, (name, img) in enumerate(images_dict.items(), 1):
        plt.subplot(rows, cols, i)
        plt.imshow(img, cmap='gray')
        plt.title(name, fontsize=8)
        plt.axis("off")
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

# Cargar imagen en escala de grises
image = cv2.imread('Actividad2\manos.jpg', cv2.IMREAD_GRAYSCALE)

# Contaminar imágenes con ruido
noisy_gaussian = add_gaussian_noise(image)
noisy_salt_pepper = add_salt_pepper_noise(image)

# Aplicar filtros
filtered_gaussian = apply_filters(noisy_gaussian)
filtered_salt_pepper = apply_filters(noisy_salt_pepper)

# Organizar todas las imágenes en un solo diccionario (máximo 12 imágenes)
all_images = {
    "Original": image,
    "Gaussian Noise": noisy_gaussian,
    "Salt & Pepper Noise": noisy_salt_pepper,
}

filtered_images = {
    **{f"Gaussian Noise - {k}": v for k, v in filtered_gaussian.items()},
    **{f"Salt & Pepper Noise - {k}": v for k, v in filtered_salt_pepper.items()}
}

# Limitar el número total de imágenes a 12
filtered_images = dict(list(filtered_images.items())[:9])
all_images.update(filtered_images)

# Mostrar todas las imágenes
show_images(all_images, "All Processed Images")
