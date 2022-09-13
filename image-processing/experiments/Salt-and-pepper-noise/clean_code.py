# import module
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint
import cv2

img_path = "./../lenna.jpeg"
img = plt.imread(img_path)      # rgb (3-channels)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
original = gray.copy()          # to ignore reference error!!! don't worry!!!

row, col = gray.shape
noises = row * col // 50        # total noises you want to add

# add noises
for _ in range(noises):
    x, y = randint(0, row), randint(0, col)
    gray[x, y] = randint(0, 2) * 255

# kernel
g_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
avg_kernel = np.ones((3, 3)) / 9

# filtering
gray_avg_filtered = cv2.filter2D(original, -1, avg_kernel)
g_filtered = cv2.filter2D(gray, -1, g_kernel)
avg_filtered = cv2.filter2D(gray, -1, avg_kernel)
median_filtered = cv2.medianBlur(gray, 3)

# plot
img_set = [original, gray_avg_filtered, gray,
           g_filtered, avg_filtered, median_filtered]

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

# plt.savefig("Salt-Pepper Noise.png")
plt.show()
