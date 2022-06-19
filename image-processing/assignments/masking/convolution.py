import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    path = "lenna.jpeg"
    img = plt.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    laplacian_1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    lap_1 = cv2.filter2D(gray, -1, laplacian_1)

    laplacian_2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    lap_2 = cv2.filter2D(gray, -1, laplacian_2)

    laplacian_3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    lap_3 = cv2.filter2D(gray, -1, laplacian_3)

    laplacian_4 = np.array([[-1, -1, -1], [-1, 16, -1], [-1, -1, -1]])
    lap_4 = cv2.filter2D(gray, -1, laplacian_4)

    shobel_1 = np.array([[-2, -4, -2], [0, 0, 0], [2, 4, 2]])
    sob_1 = cv2.filter2D(gray, -1, shobel_1)

    shobel_2 = np.array([[-2, 0, 2], [-4, 0, 4], [-2, 0, 2]])
    sob_2 = cv2.filter2D(gray, -1, shobel_2)

    img_set = [img, gray, lap_1, lap_2, lap_3, lap_4, sob_1, sob_2]
    img_tittle = [
        "Rgb",
        "Gray",
        "Laplacian_1",
        "Laplacian_2",
        "Laplacian_3",
        "Laplacian_4",
        "Sobel_1",
        "Sobel_2",
    ]

    plot_show(img_set, img_tittle)


def plot_show(img_set, img_tittle):
    n = len(img_set)

    plt.figure(figsize=(20, 20))
    for i in range(n):
        plt.subplot(4, 2, i + 1)
        plt.title(img_tittle[i])
        plt.imshow(img_set[i], "gray")

    plt.savefig("Convolution Filters.png")
    plt.show()


if __name__ == "__main__":
    main()
