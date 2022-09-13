import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "./../lenna.jpeg"
img = plt.imread(img_path)

# for making variable name convenient we just rename gray image to spatial_domain
spatial_domain = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# transform the image into frequency domain
frequency_domain = np.fft.fft2(spatial_domain)
# to move low frequency to corner to middle
frequency_domain_shifted = np.fft.fftshift(frequency_domain)

# Gaussian filter

"""
There are two kinds of gaussian filter.

1. Gaussian low pass filter - use to making image blur or smooth
2. Gaussian high pass filter - use to making image sharpen

Understand Gaussian low pass filter. Gaussian high pass filter is just (1 - low_pass_filter).

Equation:

    H(u,v) = exp(-D^2(u,v) / 2*D_not^2)
    Here,
        D_not => cut of frequency (maximize the cutoff frequency make image more smooth)
    
    D(u,v) = [(u - M/2) ^ 2 + (v - N/2) ^ 2] ^ .5
    Here,
        D(u,v) = radius or distance from the center. 

For more understanding,

Low pass filter: Low pass filter is the type of frequency domain filter that is used for smoothing the image. It attenuates the high frequency components and preserves the low frequency components. 

High pass filter: High pass filter is the type of frequency domain filter that is used for sharpening the image. It attenuates the low frequency components and preserves the high frequency components. 
"""

# Lets create Gaussian Low Pass Filter
M, N = spatial_domain.shape       # M->Row, N->Col
H = np.zeros((M, N), dtype=np.float32)

# parameter D0 control the shape of our gaussian filter.
D0 = 25   # cut off frequency

for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M/2) ** 2 + (v - N/2) ** 2)
        H[u, v] = np.exp((-D**2) / (2 * D0 * D0))

# High pass frequency
HPF = 1 - H

# Image filter in frequency domain
G_shifted = frequency_domain_shifted * H

# Inverse fft
# But before perform ifft we need to return back the low frequency to the corner
G = np.fft.ifftshift(G_shifted)
spital_domain_filtered = np.abs(np.fft.ifft2(G))

for i in range(len(img_set)):
    # print(img_set[i].shape, img_set[i][0][0])
    plt.subplot(2,4,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])

plt.show()
