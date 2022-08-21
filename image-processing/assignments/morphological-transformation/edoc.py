# Erosion, Dilation, Opening, Closing
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

os.environ["QT_QPA_PLATFORM"] = "wayland"
"""
Concept:

In Python OpenCV,

    1) when you perform erosion operation it actually remove the white pixels and vice versa.
    2) when you perform dilation operation it actually adding the white pixels and vice versa.  

    # Opening -> Erosion >> Dilation
    # Closing -> Dilation >> Erosion 
"""

def main():
    # image_path = "hw.jpeg"
    image_path = "abc.jpeg"
    img = plt.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # print(gray.shape) # 416, 416
    kernel = np.ones((3,3))

    erosion = cv2.erode(gray, kernel=kernel, iterations=1)
    dilation = cv2.dilate(gray, kernel=kernel, iterations=1)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel=kernel)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel=kernel)

    image_set = [img, gray, erosion, dilation, opening, closing]
    image_title = ['Original','Gray Image', 'After Erosion', 'After Dilation', 'Opening', 'Closing']

    plt.figure(figsize=(15,15))
    plt.subplots_adjust(hspace=.5)

    for i in range(len(image_set)):
        plt.subplot(2,3,i + 1)
        plt.title(image_title[i])
        if image_set[i].ndim == 3:
            plt.imshow(image_set[i])
        else:
            plt.imshow(image_set[i], cmap='gray')

    plt.savefig('edoc.png')
    plt.show()

if __name__ == '__main__':
    main()
