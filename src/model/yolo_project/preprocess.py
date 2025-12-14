import cv2 as cv
import numpy as np

def preprocess_for_yolo(img):
    """
    - Grayscale
    - CLAHE contrast enhancement
    - Canny edge detection
    - Morphological cleanup
    """
    # 1. Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 2. CLAHE
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray_clahe = clahe.apply(gray)

    # 3. Edge detection
    edges = cv.Canny(gray_clahe, threshold1=30, threshold2=80)

    # 4. Morphological cleanup
    kernel = np.ones((3,3), np.uint8)
    edges_clean = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel, iterations=1)

    # Optional: convert single channel to 3-channel image for YOLO
    edges_3ch = cv.cvtColor(edges_clean, cv.COLOR_GRAY2BGR)

    return edges_3ch
