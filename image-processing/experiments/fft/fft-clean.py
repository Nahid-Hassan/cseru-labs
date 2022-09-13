import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "./../lenna.jpeg"
img = plt.imread(img_path)

spital_domain = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

frequency_domain = np.fft.fft2(spital_domain)
frequency_domain_shifted = np.fft.fftshift(frequency_domain)


M, N = spital_domain.shape       # M->Row, N->Col
H = np.zeros((M, N), dtype=np.float32)

D0 = 5   # cut off frequency
for u in range(M):
    for v in range(N):
        D = np.sqrt(((u - M/2) ** 2) + ((v - N/2) ** 2))
        H[u, v] = np.exp((-D**2) / (2 * D0 * D0))

G_shifted = frequency_domain_shifted * (1-H)

G = np.fft.ifftshift(G_shifted)
spital_domain_filtered = np.abs(np.fft.ifft2(G_shifted))

img_set = [spital_domain, spital_domain_filtered]
img_title = ['Spital domain', 'filtered spital domain']

for i in range(len(img_set)):
    plt.subplot(1,2,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])

plt.show()