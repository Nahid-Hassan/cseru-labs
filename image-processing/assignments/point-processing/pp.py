import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = "lenna.jpeg"
    r = plt.imread(img_path)
    gray = cv2.cvtColor(r, cv2.COLOR_RGB2GRAY)

    T1, T2 = 70, 150
    c, p = .2, .3
    EPSILON = 1e-6

    plt.figure(figsize=(20, 20))
    plt.subplot(2, 3, 1)
    plt.imshow(r)
    plt.title("RGB")
    
    plt.subplot(2, 3, 2)
    plt.imshow(gray, cmap='gray')
    plt.title("Gray")
    
    row, col = gray.shape
    # apply condition 1 and generate new image s
    s = np.full(gray.shape, 10)
    for x in range(row):
        for y in range(col):
            if gray[x, y] >= T1 and gray[x, y] <= T2:
                s[x, y] = 100

    plt.subplot(2, 3, 3)
    plt.title("Condition 1")
    plt.imshow(s, cmap='gray')

    # apply condition 2 and generate new image s
    s = gray
    for x in range(row):
        for y in range(col):
            if gray[x, y] >= T1 and gray[x, y] <= T2:
                s[x, y] = 100
    
    plt.subplot(2, 3, 4)
    plt.title("Condition 2")
    plt.imshow(s, cmap='gray')

    # apply condition 3 and generate new image s
    s = c * np.log(1 + gray)

    plt.subplot(2, 3, 5)
    plt.title("Condition 3")
    plt.imshow(s, cmap='gray')

    # apply condition 4 and generate new image s
    s = c * ((EPSILON + gray) ** p)
    
    plt.subplot(2, 3, 6)
    plt.title("Condition 4")
    plt.imshow(s, cmap='gray')

    plt.savefig("lenna_after_point_processing.png")

    plt.show()

if __name__ == '__main__':
    main()