import matplotlib.pyplot as plt
import numpy as np

def show_grayscale_image(image: np.ndarray):
    image.squeeze()
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()

