import matplotlib.pyplot as plt
import numpy as np
import cv2

img_path = "./abc.jpeg"
img = plt.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# binary = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# erosion -> remove white pixels
# dilation -> adding white pixels


def erosion(img, kernel):
    row, col = img.shape
    r, c = kernel.shape

    cutoff = np.sum(kernel) * 255
    new_img = np.zeros((row - r + 1, col - r + 1), dtype=np.uint8)
    for x in range(row - r + 1):
        for y in range(col - r + 1):
            temp = np.sum(np.multiply(img[x:x+r, y:y+c], kernel))
            if temp == cutoff:
                new_img[x, y] = 255

    return new_img

def dilation(img, kernel):
    row, col = img.shape
    r, c = kernel.shape

    cutoff = 255
    new_img = np.zeros((row - r + 1, col - r + 1), dtype=np.uint8)
    for x in range(row - r + 1):
        for y in range(col - r + 1):
            temp = np.sum(np.multiply(img[x:x+r, y:y+c], kernel))
            if temp >= cutoff:
                new_img[x, y] = 255

    return new_img

kernel = np.ones((3, 3), dtype=np.uint8)

# using builtin function
erosion_builtin = cv2.erode(binary, kernel, iterations=1)
dilation_builtin = cv2.dilate(binary, kernel, iterations=1)
# erosion -> dilation = opening
opening_builtin = cv2.dilate(erosion_builtin, kernel)
closing_builtin = cv2.erode(dilation_builtin, kernel)

# using custom function
erosion_custom = erosion(binary, kernel)
dilation_custom = dilation(binary, kernel)
# erosion -> dilation = opening
opening_custom = dilation(erosion_custom, kernel)
closing_custom = erosion(dilation_custom, kernel)

img_set = [binary, erosion_builtin, dilation_builtin, opening_builtin, closing_builtin,
           erosion_custom, dilation_custom, opening_custom, closing_custom]
img_title = [
    "Binary Image",
    "Erosion Builtin",
    "Dilation Builtin",
    "Opening Builtin",
    "Closing Builtin",
    "Erosion Custom",
    "Dilation Custom",
    "Opening Custom",
    "Closing Custom"
]

plt.figure(figsize=(20,20))
plt.subplots_adjust(wspace=.1, hspace=.3)
plt.tight_layout()

for i in range(len(img_set)):
    plt.subplot(3,3,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])

plt.savefig("edoc.png")
plt.show()