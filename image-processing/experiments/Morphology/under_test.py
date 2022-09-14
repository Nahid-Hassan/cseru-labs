import matplotlib.pyplot as plt
import cv2
import numpy as np


def erosion(img, kernal):
    r, c = img.shape
    x, y = kernal.shape
    out = np.zeros((r-x+1, c-y+1))
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x, j:j+y], kernal))
            if(sum == 2295):
                out[i][j] = 255
    return out


def dilation(img, kernal):
    r, c = img.shape
    x, y = kernal.shape
    out = np.zeros((r-x+1, c-y+1))
    for i in range(r-x+1):
        for j in range(c-y+1):
            sum = np.sum(np.multiply(img[i:i+x, j:j+y], kernal))
            if(sum >= 255):
                out[i][j] = 255
    return out


def main():
    img_path = "abc.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    _, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernal = np.ones((3, 3), dtype=np.uint8)

    # using builtin morphological function
    img1 = cv2.erode(binary_img, kernal)
    img2 = cv2.dilate(binary_img, kernal)
    op1 = cv2.erode(img2, kernal)
    co1 = cv2.dilate(img1, kernal)

    # using custom morphological function
    img3 = erosion(binary_img, kernal)
    img4 = dilation(binary_img, kernal)
    op2 = erosion(img4, kernal)
    col2 = dilation(img3, kernal)

    img_set = [img1, img2, op1, co1, img3, img4, op2, col2]
    img_title = ["b_erosion","b_dilation","b_opening","b_closing","cus_erosion","cus_dilation","cus_opening","cus_closing"]

    for i in range(len(img_set)):
        plt.subplot(2, 4, i+1)
        plt.title(img_title[i])
        plt.imshow(img_set[i], 'gray')
    plt.savefig("result")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()