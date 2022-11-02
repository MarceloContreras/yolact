from pickletools import uint8
import numpy as np
import cv2 
from matplotlib import pyplot as plt

"""
Prueba de todas las clases en una misma instancia
"""

mask = np.load('mask_data.npy')
image = np.asarray(mask, dtype=np.uint8)
output_mask = np.zeros((mask.shape[1], mask.shape[2]), dtype = np.uint8)

for i in range(mask.shape[0]):
    output_mask = output_mask | image[i,:,:]

plt.figure(1)
plt.imshow(output_mask); plt.axis('off')
plt.show()


"""
Prueba seleccionando una única clase 
"""

#cv2.imshow('Colorimage', output_mask)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
