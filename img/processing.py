import cv2

def process(image):
    height, width, _ = image.shape
    
    white_square(image, (0, height - 150), (490, height)) # Vamos a salir adelante
    white_square(image, (width - 350, 0),  (width, 350)) # Logo Min. de Salud
    # white_square(image, (378, 500), (1010, 1200)) # Map Lines
    # white_square(image, (1705, 700), (1835, 780)) # Alert Sign (suspicious)
    return threshold(grayscale(image))

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def white_square(image, top_left, bottom_right):
    return cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), -1)
