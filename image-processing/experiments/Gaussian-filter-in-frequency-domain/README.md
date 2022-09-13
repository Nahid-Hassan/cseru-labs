## Frequency Domain Filter - Gaussian Filter

### Import Libraries


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

### Read Image and Convert to Grayscale


```python
img_path = "./../lenna.jpeg"
img = plt.imread(img_path)

spatial_domain = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Convert Spatial Domain to Frequency Domain using `np.fft.fft2(gray)`


```python
frequency_domain = np.fft.fft2(spatial_domain)
```

### Pass Low Frequecny Component to Middle or Center


```python
frequency_domain_shifted = np.fft.fftshift(frequency_domain)
```

### Plot Frequency Domain Images


```python
# first you need to take the absolute value of the 
# frequecny domain image

frequency_domain_abs = np.log1p(np.abs(frequency_domain))
frequency_domain_shifted_abs = np.log1p(np.abs(frequency_domain_shifted))

plt.subplot(1,2,1)
plt.imshow(frequency_domain_abs, cmap='gray')
plt.title("frequency_domain_abs")

plt.subplot(1,2,2)
plt.imshow(frequency_domain_shifted_abs, cmap='gray')
plt.title("frequency_domain_shifted_abs")
```




    Text(0.5, 1.0, 'frequency_domain_shifted_abs')




    
![png](images/output_10_1.png)
    


### Gaussian filter

There are two kinds of gaussian filter.

1. **Gaussian low pass filter** - use to making image blur or smooth
2. **Gaussian high pass filter** - use to making image sharpen

Now try to understand Gaussian low pass filter. Gaussian high pass filter is just (1 - low_pass_filter).

Equation:

```
H(u,v) = exp(-D^2(u,v) / 2*D_not^2)

Here,
   D_not => cut of frequency
    
Calculate D(u,v) from that we calculate D^2
    
D(u,v) = [(u - M/2) ^ 2 + (v - N/2) ^ 2] ^ .5
Here,
        D(u,v) = radius or distance from the center. 
```

For more understanding,

- **Low pass filter**: Low pass filter is the type of frequency domain filter that is used for smoothing the image. It attenuates the high frequency components and preserves the low frequency components. 

- **High pass filter**: High pass filter is the type of frequency domain filter that is used for sharpening the image. It attenuates the low frequency components and preserves the high frequency components. 

### Low Pass Filter

![images](images/guassian.png)

> Sigma and D0 are same.

```python
M, N = spatial_domain.shape       # M->Row, N->Col
H = np.zeros((M, N), dtype=np.float32)

# parameter D0 control the shape of our gaussian filter.

D0 = 10   # cut off frequency
for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M/2) ** 2 + (v - N/2) ** 2)
        H[u, v] = np.exp((-D**2) / (2 * D0 * D0))
```

### Plot Gaussian Low Pass Filter


```python
plt.imshow(H, cmap='gray')
```




    <matplotlib.image.AxesImage at 0x7f94bed3add0>




    
![png](images/output_15_1.png)
    


### Image filter in Frequency Domain


```python
G_shifted = frequency_domain_shifted * H
```


```python
G_shifted_abs = np.log1p(np.abs(G_shifted))
plt.imshow(G_shifted_abs, cmap='gray')
```




    <matplotlib.image.AxesImage at 0x7f94bd3abdc0>




    
![png](images/output_18_1.png)
    


### Inverse FFT

But before perform ifft we need to return back the low frequency to the corner


```python
G = np.fft.ifftshift(G_shifted)

spital_domain_filtered = np.abs(np.fft.ifft2(G))
```


```python
img_set = [spatial_domain, frequency_domain_shifted_abs, H, G_shifted_abs, spital_domain_filtered]

img_title = [
    'Spital Domain',
    "Frequency Domain Shifted",
    "Gaussian Lowpass Filter",
    "F_shifted * H",
    "Back to Spital Domain"
]
```


```python
plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=.01)
plt.tight_layout()

for i in range(len(img_set)):
    plt.subplot(2,3,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])
```


    
![png](images/output_22_0.png)
    


#### High Pass Filter


```python
HPF = 1 - H
```


```python
plt.imshow(HPF, cmap='gray')
```




    <matplotlib.image.AxesImage at 0x7f94bd01eb90>




    
![png](images/output_25_1.png)
    



```python
G_shifted = frequency_domain_shifted * HPF
G_shifted_abs = np.log1p(np.abs(G_shifted))
```


```python
G = np.fft.ifftshift(G_shifted)

spital_domain_filtered = np.abs(np.fft.ifft2(G))
```


```python
img_set = [spatial_domain, frequency_domain_shifted_abs, HPF, G_shifted_abs, spital_domain_filtered]

img_title = [
    'Spital Domain',
    "Frequency Domain Shifted",
    "Gaussian Highpass Filter",
    "F_shifted * HPF",
    "Back to Spital Domain"
]
```


```python
plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=.01)
plt.tight_layout()

for i in range(len(img_set)):
    plt.subplot(2,3,i+1)
    plt.imshow(img_set[i], cmap='gray')
    plt.title(img_title[i])
```


    
![png](images/output_29_0.png)
    

