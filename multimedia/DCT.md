# Discrete Cosine Transform

DCT stands for Discrete Cosine Transform, and it is a widely used technique in multimedia processing, particularly in image and video compression. The DCT is a mathematical operation that transforms a signal from the spatial domain into the frequency domain. In other words, it converts a signal from a time-varying function of position into a time-varying function of frequency.

The DCT is similar to the better-known Fourier Transform (FT), but it is more efficient in processing signals that are periodic or have a relatively short duration. The DCT has many applications in multimedia processing, including image and video compression, audio compression, and signal processing.

In image and video compression, the DCT is used to transform blocks of image or video data from the spatial domain to the frequency domain. This makes it possible to remove high-frequency components from the data, which can be quantized and encoded more efficiently than the original data. The resulting compressed data can be transmitted or stored more efficiently, with less storage space and bandwidth required. When the compressed data is decoded, the DCT is used again to transform the frequency-domain data back into the spatial domain.

**Spatial Domain**:

In image processing, the spatial domain refers to the two-dimensional space in which an image is represented. In other words, it is the space in which the pixel values of an image are arranged.

In the spatial domain, an image is represented as a matrix of pixels, where each pixel has a specific location in the image and a corresponding intensity value. The spatial domain representation of an image provides information about the spatial relationships between pixels and the structure of the image.

Processing an image in the spatial domain involves manipulating the pixel values directly. Common operations in the spatial domain include filtering, thresholding, and morphological operations. These operations can be used to enhance or modify specific features of an image, such as edges, textures, or shapes.

However, some operations, such as compression and encryption, are more efficient when performed in the frequency domain using techniques such as the Discrete Cosine Transform (DCT) or the Fourier Transform. These operations involve transforming the image from the spatial domain to the frequency domain, manipulating the frequency coefficients, and then transforming it back to the spatial domain.

![images](DCT_Equation.ppm)

> An important video to [JPEG](https://youtu.be/Kv1Hiv3ox8I)

```py
import numpy as np

m, n = 8, 8


def dctTransform(matrix):
    dct = np.zeros((m, n))

    for i in range(m):
        for j in range(n):

            ci = 1 / (m ** 0.5) if i == 0 else (2 / m) ** 0.5
            cj = 1 / (n ** 0.5) if j == 0 else (2 / n) ** 0.5

            sum = 0
            for k in range(m):
                for l in range(n):

                    dct1 = matrix[k][l] * np.cos((2 * k + 1) * i * np.pi / (
                        2 * m)) * np.cos((2 * l + 1) * j * np.pi / (2 * n))
                    sum = sum + dct1

            dct[i][j] = ci * cj * sum

    for i in range(m):
        for j in range(n):
            print(round(dct[i][j], 5), end="\t")
        print()

if __name__ == '__main__':
    matrix = np.ones((m, n)) * 255.0
    dctTransform(matrix)
```
