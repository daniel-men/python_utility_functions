from typing import List, Tuple
from PIL import Image
import numpy as np
import cv2
import pydicom

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    _image = np.array(scale(image), dtype=np.uint8)
    grayscale = cv2.cvtColor(src=image, code=cv2.COLOR_RGB2GRAY)
    return scale(grayscale, new_min=np.min(_image), new_max=np.max(_image))

def load_grayscale_image(path: str) -> np.ndarray:
    return np.array(Image.open(path).convert('L'))

def resize_image(image: np.ndarray, new_size: Tuple[int, int]) -> np.ndarray:
    _image = image.astype(np.uint8)
    return cv2.resize(_image, new_size).astype(image.dtype)

def load_images_grayscale(image_paths: List[str]) -> np.ndarray:
    return np.array([load_grayscale_image(p) for p in image_paths])

def load_image_data_from_dicom(dicom_path: str) -> np.ndarray:
    return pydicom.dcmread(dicom_path).pixel_array

def load_dicom_images(dicom_paths: List[str]) -> np.ndarray:
    return np.array([load_image_data_from_dicom(path) for path in dicom_paths])

def save_image(image: np.ndarray, path: str):
    Image.fromarray(image).save(path)

def scale(data: np.ndarray, new_min=0, new_max=1) -> np.ndarray:
    maximum = np.max(data)
    minimum = np.min(data)
    return (new_max - new_min) * ((data - minimum) / (maximum - minimum)) + new_min

def create_roi2D(image: np.ndarray, x: int, y: int, roi_size: int) -> np.ndarray:
    size = roi_size // 2
    return image[y-size:y+size, x-size:x+size]