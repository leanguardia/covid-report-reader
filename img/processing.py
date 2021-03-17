import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def show_img(img):
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rectangle_to_relative(img, topleft, bottomright):
  height, width = img.shape
  cv.rectangle(img, topleft, bottomright, (0,255,0), 1)
  print(f"({(round(topleft[0]/width, 4))}, {round(topleft[1]/height,4)}), ({round(bottomright[0]/width, 4)}, {round(bottomright[1]/height,4)})")
  show_img(img)

def process(image):
    height, width, _ = image.shape
    return threshold(grayscale(image))

def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def threshold(image):
    return cv.threshold(image, 96, 255, cv.THRESH_BINARY)[1]

def threshold_otsu(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

def white_square(image, top_left, bottom_right):
    ''' This used to be in process'''    
    # white_square(image, (0, height - 150), (490, height)) # Vamos a salir adelante
    # white_square(image, (width - 350, 0),  (width, 350)) # Logo Min. de Salud
    # white_square(image, (378, 500), (1010, 1200)) # Map Lines
    # white_square(image, (1705, 700), (1835, 780)) # Alert Sign (suspicious)
  
    return cv.rectangle(image, top_left, bottom_right, (255, 255, 255), -1)


if __name__ == "__main__":
    img = cv.imread('img/reportes_salud/299_.png',0)
    # img = cv.medianBlur(img,1)
    th = threshold(img)
    ret,th0 = cv.threshold(img,50,255,cv.THRESH_BINARY)
    ret,th1 = cv.threshold(img,130,255,cv.THRESH_BINARY)
    
    # kernel = np.ones((3,3), np.uint8)
    # erosion = cv2.erode(th0, kernel, iterations = 1)

    # th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
    #             cv.THRESH_BINARY,11,2)
    # th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #             cv.THRESH_BINARY,11,2)
    # titles = ['Original Image', 'Global Thresholding (v = 127)',
    #             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th, th0, th1]
    for i in range(len(images)):
      # show_img(images[i])
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        # plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
