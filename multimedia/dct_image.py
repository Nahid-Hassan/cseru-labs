import numpy as np
from PIL import Image

def dct2(block):
    """
    Apply 2D DCT to an 8x8 block of image data.
    """
    # Compute 1D DCT on rows
    dct_rows = np.apply_along_axis(dct, axis=1, arr=block)
    # Compute 1D DCT on columns
    dct_cols = np.apply_along_axis(dct, axis=0, arr=dct_rows)
    return dct_cols

def idct2(block):
    """
    Apply 2D inverse DCT to an 8x8 block of DCT coefficients.
    """
    # Compute 1D inverse DCT on columns
    idct_cols = np.apply_along_axis(idct, axis=0, arr=block)
    # Compute 1D inverse DCT on rows
    idct_rows = np.apply_along_axis(idct, axis=1, arr=idct_cols)
    return idct_rows

# Load an image and convert it to grayscale
image = Image.open('panda.jpg').convert('L')

# Convert the image to a numpy array of floats
data = np.asarray(image, dtype=float)

# Compute the DCT of 8x8 blocks of the image
dct_blocks = []
for i in range(0, data.shape[0], 8):
    for j in range(0, data.shape[1], 8):
        block = data[i:i+8, j:j+8]
        dct_block = dct2(block)
        dct_blocks.append(dct_block)

# Convert the DCT coefficients to a numpy array
dct_data = np.asarray(dct_blocks)

# Do something with the DCT coefficients here...

# Compute the inverse DCT to reconstruct the image
reconstructed_blocks = []
for i in range(dct_data.shape[0]):
    dct_block = dct_data[i]
    block = idct2(dct_block)
    reconstructed_blocks.append(block)

# Convert the reconstructed blocks to a numpy array
reconstructed_data = np.asarray(reconstructed_blocks)

# Reshape the reconstructed data to match the original image shape
reconstructed_data = reconstructed_data.reshape(data.shape)

# Convert the reconstructed data to an image and save it
reconstructed_image = Image.fromarray(reconstructed_data.astype('uint8'), mode='L')
reconstructed_image.save('reconstructed_image.jpg')
