import cv2
import numpy as np

imagen = cv2.imread("Sin título.jpg") 
kernel=np.array([[1,1,1],[-1,-1,-1],[0,0,0]])
m,n=imagen.shape
imagenf=np.xeros_like(imagen)
for x in range(m-2):
    for y in range(n-2):
        res=np.sum(imagen[x:x+:3,y:y+:3]*kernel)
        if res
        i


cv2.imshow("ladrillos", imagen)  # Mostrar la imagen binaria
cv2.waitKey(0)
cv2.destroyAllWindows()