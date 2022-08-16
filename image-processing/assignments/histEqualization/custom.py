import numpy as np
import os
import matplotlib.pyplot as plt
import cv2

os.environ["QT_QPA_PLATFORM"] = "wayland"


def main():
    img_path = "nature.jpeg"
    img = plt.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    gray_np_array = np.asarray(gray)
    # print(gray_np_array)

    flat = gray.flatten()
    plt.hist(flat, bins=50)
    plt.show()


if __name__ == '__main__':
    main()