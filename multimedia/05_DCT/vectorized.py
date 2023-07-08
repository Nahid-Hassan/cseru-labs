import numpy as np

def dct_2d(image):
    # Get image dimensions
    height, width = image.shape
    
    # Create an output array of the same size as the input image
    dct_result = np.zeros_like(image, dtype=np.float64)
    
    # Compute the 2D DCT
    for u in range(height):
        for v in range(width):
            sum = 0.0
            for x in range(height):
                for y in range(width):
                    cos_x = np.cos((2 * x + 1) * u * np.pi / (2 * height))
                    cos_y = np.cos((2 * y + 1) * v * np.pi / (2 * width))
                    sum += image[x, y] * cos_x * cos_y
            dct_result[u, v] = sum / np.sqrt(height) / np.sqrt(width)
            
    return dct_result

# Example usage
image = np.array([[100, 200, 150],
                  [50, 75, 125],
                  [225, 180, 210]])

dct_result = dct_2d(image)
print(dct_result)
