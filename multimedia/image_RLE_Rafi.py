import matplotlib.pyplot as plt
import numpy as np
import cv2
 
 
def encoding(img, bits):
    encoded = []
    count = 0
    prev = None
    fimg = img.flatten()
    for pixel in fimg:
        if prev == None:
            prev = pixel
            count += 1
        else:
            if prev != pixel:
                encoded.append((count, prev))
                prev = pixel
                count = 1
            else:
                if count < (2**bits)-1:
                    count += 1
                else:
                    encoded.append((count, prev))
                    prev = pixel
                    count = 1
    encoded.append((count, prev))
    return np.array(encoded)
 
 
def decode(encoded, shape):
    decoded = []
    for rl in encoded:
        r, p = rl[0], rl[1]
        decoded.extend([p]*r)
    dimg = np.array(decoded).reshape(shape)
    return dimg
 
 
def main():
    img = cv2.imread("952142.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    plt.subplot(2, 1, 1)
    plt.imshow(gray)
    plt.savefig('pic1')
    plt.show()
    encoded = encoding(gray, 8)
    print('encoded pic: ')
    print(encoded.shape)
    out = decode(encoded, gray.shape)
    print('decoded pic: ')
    print(out.shape)
    plt.subplot(2, 1, 2)
    plt.imshow(out)
    plt.savefig('pic2')
    plt.show()
 
 
main()
