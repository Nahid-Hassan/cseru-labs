import cv2
import matplotlib.pyplot as plt
import os

def main():
    window = 30
    path = "lenna.jpg"

    if os.path.exists(path) and os.path.isfile(path):
        gray = plt.imread(path)
    else:
        print("Path not exits!!!")
        exit(0)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    r, c = gray.shape

    left, right, narrow_band = gray.copy(), gray.copy(), gray.copy()

    # shifting
    left = left - 79
    right = right + 50

    for i in range(r):
        for j in range(c):
            if narrow_band[i][j] <= 100:
                narrow_band[i][j] = 100
            elif narrow_band[i][j] >= 175:
                narrow_band[i][j] = 175

    # calcHist
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    left_hist = cv2.calcHist([left], [0], None, [256], [0,256])
    right_hist = cv2.calcHist([right], [0], None, [256], [0,256])
    narrow_band_hist = cv2.calcHist([narrow_band], [0], None, [256], [0, 256])

    img_set  = [gray, gray_hist, left, left_hist, right, right_hist, narrow_band, narrow_band_hist]
    img_title = ["Gray Original", 'Gray Histogram', 'Left Shift', 'Left Shift Histogram', 'Right Shift', 'Right Shift Histogram', 'Narrow Band', 'Narrow Band Hist']

    # img_set_title = dict(zip(img_set, img_title))

    plt.figure(figsize=(20,20))
    k = 0
    for i in range(len(img_set)):
        temp_img = img_set[i]
        if temp_img.shape[1] != 1:
            plt.subplot(2, 4, k + 1)
            plt.title(img_title[i])
            plt.imshow(temp_img, cmap='gray')   
            k += 1
        else:
            plt.subplot(2, 4, k + 4)
            plt.title(img_title[i])
            plt.plot(temp_img)

    plt.savefig("Shift - Histogram.jpg")
    plt.show()

    
if __name__ == '__main__':
    main()
