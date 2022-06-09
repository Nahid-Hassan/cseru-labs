import matplotlib.pyplot as plt
import cv2
import numpy

def main():
    # image path
    path = 'trees_in_water.jpg'
    path = 'sunset.jpg'
    # read image
    img = plt.imread(path)
    # print shape, max and min value
    print(img.shape, img.max(), img.min())

    # split image into red, green and blue channels
    # red = img[:, :, 0]
    # green = img[:, :, 1]
    # blue = img[:, :, 2]

    # convert image into grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # convert image into binary
    _, binary = cv2.threshold(grayscale, 150, 255, cv2.THRESH_BINARY)

    # plot histogram
    red = cv2.calcHist([img], [0], None, [256], [0, 256])
    green = cv2.calcHist([img], [1], None, [256], [0, 256])
    blue = cv2.calcHist([img], [2], None, [256], [0,256])
    grayscale = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    binary = cv2.calcHist([binary], [0], None, [256], [0, 256])

    plt.figure(figsize = (20, 20))

    plt.subplot(2, 3, 1)
    plt.title('RGB')

    plt.plot(red, 'r')
    plt.plot(green, 'g')
    plt.plot(blue, 'b')

    plt.subplot(2, 3, 2)
    plt.title('Red')
    plt.plot(red, 'r')

    plt.subplot(2, 3, 3)
    plt.title('Green')
    plt.plot(green, 'g')
    
    plt.subplot(2, 3, 4)
    plt.title('Blue')
    plt.plot(blue, 'b')
    
    plt.subplot(2, 3, 5)
    plt.title('Grayscale')
    plt.plot(grayscale, 'k')

    plt.subplot(2, 3, 6)
    plt.title('Binary')
    plt.plot(binary, 'k')

    plt.savefig('histogram.jpg')

    plt.show()

if __name__ == '__main__':
    main()