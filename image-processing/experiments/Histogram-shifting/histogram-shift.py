import matplotlib.pyplot as plt
import numpy as np
import cv2

# lenna-lc is a low contrast grayscale image, so we don't need to convert it to gray
img_path = './../lenna-lc.jpg'
gray = plt.imread(img_path)

row, col = gray.shape
left_shift, right_shift, narrow_band = gray.copy(), gray.copy(), gray.copy()

# left shift and right shift
left_shift = left_shift - 78
right_shift = right_shift + 50

# for narrow band
for x in range(row):
    for y in range(col):
        if narrow_band[x, y] <= 100:
            narrow_band[x, y] = 100
        elif narrow_band[x, y] >= 175:
            narrow_band[x, y] = 175

# calculate histogram for each images
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
left_shift_hist = cv2.calcHist([left_shift], [0], None, [256], [0, 256])
right_shift_hist = cv2.calcHist([right_shift], [0], None, [256], [0, 256])
narrow_band_hist = cv2.calcHist([narrow_band], [0], None, [256], [0, 256])

# plot
img_set = [gray, gray_hist, left_shift, left_shift_hist, right_shift,
           right_shift_hist, narrow_band, narrow_band_hist]
img_title = ["Gray Original", 'Gray Histogram', 'Left Shift', 'Left Shift Histogram',
             'Right Shift', 'Right Shift Histogram', 'Narrow Band', 'Narrow Band Hist']


plt.figure(figsize=(15, 15))
plt.subplots_adjust(hspace=0.5, wspace=.2)

for i in range(len(img_set)):
    plt.subplot(2, 4, i+1)
    plt.title(img_title[i])

    # for histogram 
    if img_set[i].shape[1] == 1:
        plt.plot(img_set[i])
    else:
        plt.imshow(img_set[i], cmap="gray")
    

# plt.savefig("hist-shift.png")
plt.show()

