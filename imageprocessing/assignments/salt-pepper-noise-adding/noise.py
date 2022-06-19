import matplotlib.pyplot as plt
from numpy.random import randint
import numpy as np
import cv2


def main():
    img_path = "./lenna.jpeg"
    img = plt.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    original = gray.copy()

    r, c = gray.shape
    t = (r * c) // 50  # total noise number

    for i in range(t):
        x, y = randint(0, r), randint(0, c)
        gray[x][y] = randint(0, 2) * 255

    g_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    avg_kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9

    avg_gray_filter = cv2.filter2D(original, -1, avg_kernel)
    g_filter = cv2.filter2D(gray, -1, g_kernel)
    avg_filter = cv2.filter2D(gray, -1, avg_kernel)
    median_filter = cv2.medianBlur(gray, 3)

    img_set = [original, avg_gray_filter, gray, g_filter, avg_filter, median_filter]
    img_title = [
        "Grayscale",
        "Filtered Image\n(Average Kernel)",
        "Noisy Image\n(Salt and Pepper Noise)",
        "Filtered Noisy Image\n(Gaussian Kernel)",
        "Filtered Noisy Image\n(Average Kernel)",
        "Filtered Noisy Image\n(Medium Filter)",
    ]

    plt.figure(figsize=(15, 15))
    plt.subplots_adjust(hspace=0.5)

    for i in range(len(img_set)):
        plt.subplot(2, 3, i + 1)
        plt.title(img_title[i])
        plt.imshow(img_set[i], cmap="gray")

    plt.savefig("Salt-Pepper Noise.png")
    plt.show()


if __name__ == "__main__":
    main()
