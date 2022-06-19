import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    path = 'lenna.jpeg'
    # path = 'chair.jpg'
    # path = 'art.jpg'
    img  = plt.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print(gray.shape)

    horz_kernel = np.array([[-3,-10,-3], [0,0,0], [3,10,3]])
    vert_kernel = np.array([[-3,0,3],[-10,0,10], [-3,0,3]])
    box_blur_kernel = np.ones((3,3)) / 9
    # identity_kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
    sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    edge_d_kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])


    # new_image = np.zeros((gray.shape[0] - 2, gray.shape[1] - 2), dtype=np.uint8)
    # row, col = gray.shape
    # for i in range(row-2):
        # for j in range(col-2):
            # new_image[i][j] = np.sum(np.multiply(gray[i:3+i, j:3+j], vert_kernel)) 


    horizontal = cv2.filter2D(gray, -1, horz_kernel)
    vertical = cv2.filter2D(gray, -1, vert_kernel)
    box_blur = cv2.filter2D(gray, -1, box_blur_kernel)
    # identity = cv2.filter2D(gray, -1, identity_kernel)
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    edge = cv2.filter2D(gray, -1, edge_d_kernel)


    img_set = [img, gray, horizontal, vertical, box_blur, sharpen, edge]
    title_set = ['RGB', 'Grayscale', 'Horizontal', 'Vertical', 'Box Blur', 'Sharpen', 'Edge']

    plt.figure(figsize=(20,20))

    for i in range(len(img_set)):
        img = img_set[i]
        plt.subplot(2, 4, i + 1)
        plt.title(title_set[i])

        if len(img.shape) == 3:
            plt.imshow(img) 
        else:
            plt.imshow(img, cmap='gray')  
    
    plt.savefig('lenna_after_convolution.png')
    plt.show()

if __name__ == '__main__':
    main()