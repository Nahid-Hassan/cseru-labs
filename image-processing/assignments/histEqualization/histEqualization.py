import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

# this line of code is for my environment issue...
os.environ["QT_QPA_PLATFORM"] = "wayland"


def main():
    # img_path = "lenna.jpeg"
    # img_path = "tree.jpg"
    img_path = "einstein.jpg"
    # img_path = "nature.jpeg"
    img = plt.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    gray_eq = cv2.equalizeHist(gray)
    # equHist2(gray)
    gray_eq_hist = cv2.calcHist([gray_eq], [0], None, [256], [0, 256])

    img_set = [gray, gray_hist, gray_eq, gray_eq_hist]
    img_title = ["gray", "gray_hist", "gray_eq", "gray_eq_hist"]

    plot_images(img_set, img_title)


######################################################################
## Below equHist(gray) and equHist2(gray) is under development
######################################################################
def equHist(gray):
    values, counts = np.unique(gray, return_counts=True)
    # print(len(values), values)
    # print(len(counts), counts)
    # print(gray.shape, sum(counts))

    prob_values = counts / sum(counts)
    # print(prob_values)
    cm = np.cumsum(prob_values)
    # print(cm)
    l = gray.max() * cm
    l = np.round(l)
    print(list(zip(values, counts, l)))


def equHist2(gray):
    values, counts = np.unique(gray, return_counts=True)
    cum_counts = np.cumsum(counts)

    cum_counts_norm = cum_counts / cum_counts[-1]  # normalize
    cum_counts_norm_mul_by_max = cum_counts_norm * gray.max()

    cum_counts_round = np.round(cum_counts_norm_mul_by_max)

    print(list(zip(values, counts, cum_counts_round)))
####################################################################

def plot_images(img_set, img_title):
    for i in range(len(img_set)):
        plt.subplot(2, 2, i + 1)
        plt.title(img_title[i])

        if img_set[i].shape[1] == 1:
            plt.plot(img_set[i])
        else:
            plt.imshow(img_set[i], cmap="gray")

    plt.savefig('HistogramEqualization.png')
    plt.show()


if __name__ == "__main__":
    main()




img_path = "einstein.jpg"
img = plt.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

gray_eq = cv2.equalizeHist(gray)
gray_eq_hist = cv2.calcHist([gray_eq], [0], None, [256], [0, 256])

img_set = [gray, gray_hist, gray_eq, gray_eq_hist]
img_title = ["gray", "gray_hist", "gray_eq", "gray_eq_hist"]


plot_images(img_set, img_title)
