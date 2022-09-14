import matplotlib.pyplot as plt
import numpy as np
import cv2

img_path = "./../lenna.jpeg"

img = plt.imread(img_path)      # rgb (3-channels)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# you can simply using cv2.equalizeHist(gray_image) to equalize the image
# now we are going to create our custom equalizeHist()
# for that we need to,

"""
1. L Value -> 256.
2. Row and Column value or shape of the gray image.
3. Image size.
4. Original gray image histogram.
5. CDF or cumulative sum of the histogram and cdf_min value.
"""

L = 256
row, col = gray.shape
img_size = row * col

cdf = gray_hist.cumsum()
cdf_min = cdf.min()

equalize_img = np.zeros((row, col), np.uint8)
for x in range(row):
    for y in range(col):
        equalize_img[x, y] = ((cdf[gray[x, y]] - cdf_min) / (img_size - cdf_min)) * (L-1)

equalize_img_hist = cv2.calcHist([equalize_img], [0], None, [256], [0, 256])

# plot
img_set = [gray, gray_hist, equalize_img, equalize_img_hist]
img_title = ["Grayscale Image", "Grayscale Image Histogram",
             "Equalize Image", "Equalize Image Histogram"]

plt.subplots_adjust(hspace=.5)

for i in range(len(img_set)):
    plt.subplot(2, 2, i + 1)
    plt.title(img_title[i])

    if img_set[i].shape[1] == 1:
        plt.plot(img_set[i])
    else:
        plt.imshow(img_set[i], cmap='gray')

plt.savefig("histogram-equalization.png")
plt.show()
