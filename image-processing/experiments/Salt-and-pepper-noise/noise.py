# import module
import matplotlib.pyplot as plt
import numpy as np
import cv2

# image path
img_path = "./../lenna.jpeg"
img = plt.imread(img_path)      # rgb (3-channels)

# convert rgb to gray
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
original = gray.copy()          # to ignore reference error!!! don't worry!!!

# noises
row, col = gray.shape
noises = row * col // 50        # total noises you want to add

# randomly added black and white pixels
for i in range(noises):
    # provide random points
    x, y = np.random.randint(0, row), np.random.randint(0, col)
    # randint(0,2) -> returns 0 or 1 at a time
    # 0 * 255 => 0, and 1 * 255 => 255
    gray[x, y] = np.random.randint(0, 2) * 255

# gaussian kernel
# divide by 16 because of total sum of each weights is equal 16
g_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
# here total some of each weights is equal 9
avg_kernel = np.ones((3, 3)) / 9

# filter2d
gray_avg_filtered = cv2.filter2D(original, -1, avg_kernel)
# apply gaussian filter
g_filtered = cv2.filter2D(gray, -1, g_kernel)
# apply average filter
avg_filtered = cv2.filter2D(gray, -1, avg_kernel)
# median filter produce best output for salt and pepper noise
# median blur smooth the image
median_filtered = cv2.medianBlur(gray, 3)

# plot the image
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
