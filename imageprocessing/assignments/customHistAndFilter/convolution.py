import matplotlib.pyplot as plt
import cv2
import numpy as np

def conv(mat, kernel):
    row, col = mat.shape
    r, c = kernel.shape[0] // 2, kernel.shape[1] // 2
    r, c = r * 2, c * 2

    new_image = np.zeros((row - r, col - c), dtype=np.uint8)
    for i in range(row - r):
        for j in range(col - c):
            new_image[i][j] = np.sum(np.multiply(mat[i:3+i, j:3+j], kernel))

    return new_image 

def main():
    path = 'lenna.jpeg'
    img  = plt.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    box_blur_kernel = np.ones((3,3)) / 9
    sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) 
 
    box_blur = cv2.filter2D(gray, -1, box_blur_kernel)
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    
    box_blur_custom = conv(gray, box_blur_kernel)
    sharpen_custom = conv(gray, sharpen_kernel)

    plt.figure(figsize=(20,20))

    plt.subplot(2,2,1)
    plt.title("Using Builtin Function")
    plt.imshow(box_blur, cmap='gray')

    plt.subplot(2,2,2)
    plt.title("Using custom Function")
    plt.imshow(box_blur_custom, cmap='gray')

    plt.subplot(2,2,3)
    plt.title("Using Builtin Function")
    plt.imshow(sharpen, cmap='gray')

    plt.subplot(2,2,4)
    plt.title("Using custom Function")
    plt.imshow(sharpen_custom, cmap='gray')

    plt.savefig("NeighborHood.png")
    plt.show()

if __name__ == '__main__':
    main()