import numpy as np
import matplotlib.pyplot as plt
import cv2 

def main():
    path = 'lenna.jpeg'
    img = plt.imread(path)
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    
    # print(gray.shape)

    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]

    red_u, red_c = np.unique(red, return_counts=True)
    green_u, green_c = np.unique(green, return_counts=True)
    blue_u, blue_c = np.unique(blue, return_counts=True)
    
    red = cv2.calcHist([img], [0], None, [256], [0, 256])
    green = cv2.calcHist([img], [1], None, [256], [0, 256])
    blue = cv2.calcHist([img], [2], None, [256], [0,256])

    plt.figure(figsize=(20,20))
    
    plt.subplot(1,2,1)
    plt.title("Custom")
    plt.plot(red_u, red_c, 'r')
    plt.plot(green_u, green_c, 'g')
    plt.plot(blue_u, blue_c, 'b')

    plt.subplot(1,2,2)
    plt.title("Using calcHist Function")
    plt.plot(green, 'g')
    plt.plot(red, 'r')
    plt.plot(blue, 'b')

    plt.show()

if __name__ == '__main__':
    main()