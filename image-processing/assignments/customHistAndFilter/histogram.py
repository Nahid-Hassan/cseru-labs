import numpy as np
import matplotlib.pyplot as plt
import cv2 

def pixel_freq(mat):
    d = dict()

    for x in range(256):
        d[x] = 0
    
    for row in mat:
        for pixel in row:
            d[pixel] += 1
    
    return d

def main():
    path = 'lenna.jpeg'
    img = plt.imread(path)
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    
    # print(gray.shape)

    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]

    red_dict = pixel_freq(red)
    green_dict = pixel_freq(green)
    blue_dict = pixel_freq(blue)
    # gray_dict = pixel_freq(gray)
    
    red = cv2.calcHist([img], [0], None, [256], [0, 256])
    green = cv2.calcHist([img], [1], None, [256], [0, 256])
    blue = cv2.calcHist([img], [2], None, [256], [0,256])

    plt.figure(figsize=(20,20))
    
    plt.subplot(1,2,1)
    plt.title("Custom")
    plt.plot(red_dict.keys(), red_dict.values(), 'r')
    plt.plot(green_dict.keys(), green_dict.values(), 'g')
    plt.plot(blue_dict.keys(), blue_dict.values(), 'b')

    plt.subplot(1,2,2)
    plt.title("Using calcHist Function")
    plt.plot(green, 'g')
    plt.plot(red, 'r')
    plt.plot(blue, 'b')
    
    plt.savefig('Histogram.png')
    plt.show()

if __name__ == '__main__':
    main()