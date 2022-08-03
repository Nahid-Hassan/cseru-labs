import matplotlib.pyplot as plt
import cv2
import numpy


def main():
    # image path
    path = 'sunset.jpg'
    # read image
    img = plt.imread(path)
    # print shape, max and min value
    print(img.shape, img.max(), img.min())

    red, green, blue = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # convert image into grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # convert image into binary
    _, binary = cv2.threshold(grayscale, 150, 255, cv2.THRESH_BINARY)

    # plot histogram
    plt.figure(figsize = (20, 20))

    plt.subplot(2, 3, 1)
    plt.title('RGB')
    plt.imshow(img)


    plt.subplot(2, 3, 2)
    plt.title('Red')
    plt.imshow(red)

    plt.subplot(2, 3, 3)
    plt.title('Green')
    plt.imshow(green)
    
    plt.subplot(2, 3, 4)
    plt.title('Blue')
    plt.imshow(blue)
    
    plt.subplot(2, 3, 5)
    plt.title('Grayscale')
    plt.imshow(grayscale, cmap='gray')

    plt.subplot(2, 3, 6)
    plt.title('Binary')
    plt.imshow(binary, cmap='gray')

    plt.savefig('rgb-images.jpg')

    plt.show()

if __name__ == '__main__':
    main()
