import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "./../lenna.jpeg"
img = plt.imread(img_path)
spatial_domain = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

frequency_domain = np.fft.fft2(spatial_domain)
frequency_domain_shifted = np.fft.fftshift(frequency_domain)
frequency_domain_shifted_abs = np.abs(frequency_domain_shifted)

# Lets create Gaussian Low Pass Filter
M, N = spatial_domain.shape       # M->Row, N->Col
H = np.zeros((M, N), dtype=np.float32)

# parameter D0 control the shape of our gaussian filter.
D0 = 25   # cut off frequency
for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M/2) ** 2 + (v - N/2) ** 2)
        H[u, v] = np.exp((-D**2) / (2 * D0 * D0))

# Image filter in frequency domain
G_shifted = frequency_domain_shifted * H
G_shifted_abs = np.abs(G_shifted)

# Inverse fft
# But before perform ifft we need to return back the low frequency to the corner
G = np.fft.ifftshift(G_shifted)
spital_domain_filtered = np.abs(np.fft.ifft2(G))

img_set = [spatial_domain, frequency_domain_shifted_abs, H, G_shifted_abs, spital_domain_filtered]

img_title = [
    'Spital Domain',
    "Frequency Domain Shifted",
    "Gaussian Highpass Filter",
    "F_shifted * H",
    "Back to Spital Domain"
]

plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=.01)
plt.tight_layout()

for i in range(len(img_set)):
    plt.subplot(2,3,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])

plt.show()
