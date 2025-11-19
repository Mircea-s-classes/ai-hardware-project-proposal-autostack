import cv2
import numpy as np

# Load an image (replace 'your_image.jpg' with your image file)
# Or capture from a camera: cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
image = cv2.imread('image01.jpg') 

if image is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur for noise reduction
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 150) # Adjust thresholds as needed

    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # If using camera, release it: cap.release()