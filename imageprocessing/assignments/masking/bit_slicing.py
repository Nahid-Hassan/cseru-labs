import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    path = "lenna.jpeg"
    rgb = plt.imread(path)

    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    r, c = grayscale.shape

    bit_1 = np.zeros((r, c), dtype=np.uint8)
    bit_2 = np.zeros((r, c), dtype=np.uint8)
    bit_3 = np.zeros((r, c), dtype=np.uint8)
    bit_4 = np.zeros((r, c), dtype=np.uint8)
    bit_5 = np.zeros((r, c), dtype=np.uint8)
    bit_6 = np.zeros((r, c), dtype=np.uint8)
    bit_7 = np.zeros((r, c), dtype=np.uint8)
    bit_8 = np.zeros((r, c), dtype=np.uint8)

    k = 1
    for i in range(r):
        for j in range(c):
            bit_1[i][j] = grayscale[i][j] & k

    bit_2 = grayscale & (k << 1)
    bit_3 = grayscale & (k << 2)
    bit_4 = grayscale & (k << 3)
    bit_5 = grayscale & (k << 4)
    bit_6 = grayscale & (k << 5)
    bit_7 = grayscale & (k << 6)
    bit_8 = grayscale & (k << 7)

    img_set = [bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8]
    plot_img(img_set)


def plot_img(img_set):
    n = len(img_set)

    plt.figure(figsize=(20, 20))
    for i in range(n):
        plt.subplot(4, 2, i + 1)
        plt.title("Bit " + str(i + 1))
        plt.imshow(img_set[i], cmap="gray")
    plt.savefig("Bit_Slicing.png")
    plt.show()


if __name__ == "__main__":
    main()
