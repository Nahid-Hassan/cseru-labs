import numpy as np
from numpy import pi, cos, sqrt

BLOCK_SIZE = 8

# Define the DCT basis functions
"""
The equation for the Discrete Cosine Transform (DCT) of a sequence x[n] of length N is given by:

X[k] = sqrt(2/N) * C[k] * sum(x[n] * cos((pi/N) * (n + 0.5) * k), n=0 to N-1)

where:

X[k] is the kth DCT coefficient of the sequence
C[k] is a normalization constant defined as:
C[k] = 1 for k = 0
C[k] = sqrt(2) for k > 0
N is the length of the sequence
pi is the mathematical constant pi (approximately 3.14159...)
cos() is the cosine function
The above equation is for the Type-II DCT, which is the most common variant used in multimedia applications. 
The Type-III DCT, which is the inverse transform of the Type-II DCT, can be obtained by applying a 
scaling factor of 2/N to the above equation, and swapping the roles of x[n] and X[k].
"""
def alpha(u):
    if u == 0:
        return 1 / sqrt(BLOCK_SIZE)
    else:
        return sqrt(2 / BLOCK_SIZE)

# Perform the DCT on an 8x8 block of image data
def dct(block):
    temp = np.zeros((BLOCK_SIZE, BLOCK_SIZE))
    for v in range(BLOCK_SIZE):
        for u in range(BLOCK_SIZE):
            sum = 0
            for y in range(BLOCK_SIZE):
                for x in range(BLOCK_SIZE):
                    sum += block[y, x] * cos((2*x + 1)*u*pi / (2*BLOCK_SIZE)) \
                                    * cos((2*y + 1)*v*pi / (2*BLOCK_SIZE))
            temp[v, u] = alpha(u) * alpha(v) * sum

    # Copy the DCT coefficients back to the input block
    for y in range(BLOCK_SIZE):
        for x in range(BLOCK_SIZE):
            block[y, x] = temp[y, x]

# Example usage
if __name__ == '__main__':
    # Create an example 8x8 block of image data
    block = np.array([
        [52, 55, 61, 66, 70, 61, 64, 73],
        [63, 59, 55, 90, 109, 85, 69, 72],
        [62, 59, 68, 113, 144, 104, 66, 73],
        [63, 58, 71, 122, 154, 106, 70, 69],
        [67, 61, 68, 104, 126, 88, 68, 70],
        [79, 65, 60, 70, 77, 68, 58, 75],
        [85, 71, 64, 59, 55, 61, 65, 83],
        [87, 79, 69, 68, 65, 76, 78, 94]
    ], dtype=float)

    # Perform the DCT on the block
    dct(block)

    # Print the DCT coefficients
    print("DCT coefficients:")
    print(block)
