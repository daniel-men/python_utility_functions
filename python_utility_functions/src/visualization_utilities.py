import matplotlib.pyplot as plt
import numpy as np

def show_grayscale_image(image: np.ndarray):
    image.squeeze()
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()

def show_multiple_images(images: np.ndarray, cmap: str = 'gray'):
    for image in images:
        plt.figure()
        plt.imshow(image, cmap=cmap)
    plt.show()