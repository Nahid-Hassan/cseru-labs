import numpy as np
import matplotlib.pyplot as plt
import cv2


# if show any environmental issue
os.environ["QT_QPA_PLATFORM"] = "wayland"


# --------- Image Path ----------- #
img_path = "lenna.jpeg"

# ----------- Read Image as Original format -------#
rgb = plt.imread(img_path)

# shape, min pixel value, max pixel value
print(rgb.shape, rgb.max(), rgb.mean())

# split red, green, and blue
# img[row, col, channel]
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# convert rgb to gray scale
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

# ------------------------- Custom gray ------------------ #

"""
New grayscale image = ( (0.3 * R) + (0.59 * G) + (0.11 * B) ).
"""

# convert gray to binary
# _ is used for dummy variable in python (convention)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# --------------------- Custom binary --------------- #

"""
img[img > 150] = 255
img[img <= 150] = 0
"""

# calculate histogram using calcHist()
red_hist = cv2.calcHist([img], [0], None, [256], [0,256])
# or
red_hist = cv2.calcHist([red], [0], None, [256], [0,256])
green_hist = cv2.calcHist([img], [1], None, [256], [0,256])
# or
green_hist = cv2.calcHist([green], [0], None, [256], [0, 256])


### ---------------- Custom Histogram ------------------------#
def calFreq(img):
	d = dict()
	for i in range(0, 256):
		d[i] = 0
	
	for row in img:
		for x in row:
			d[x] += 1

	return d

# return a dictionary
blue_hist = calFreq(blue) 
# or 
blue_hist = calFreq(img[:, :, 2])

# x is the key and y is the values
x, y = blue_hist.items()

# --------- Convolution -------------#

# ---- some common filter --------------#
# all the filter applying to 2d image -----# 

# middle row is zero, upper is negative and lower is oposite
horz_kernel = np.array([-5, -10, -5], [0,0,0], [5,10,5]) 

# middle column is zero.
vert_kernel = np.array([-5, 0, 5], [-10, 0, 10], [-5, 0, 5])

# blur
box_blur = np.ones((3,3)) / 9

# sharpen
shapren_kernel = np.array([0, -1, 0],[-1, 5, -1],[0, -1, 0])

# edge_d_kernel 
edge_kernel = np.array([-1,-1,-1],[-1,8,-1],[-1,-1,-1])


# ---------- filter using cv2.filter2d() ------------
# filter2d(2d_image, ddepth, kernel) ---> return 2d image
# default ddepth is equal -1, that means output image also 
# same depth as input image.

horz_filtered = cv2.filter2d(gray, -1, horz_kernel)

# ---------------- Custom convolution ------------------

# ------------------------------------------------------


## --------------- Point Processing -----------------------

"""
a = np.full((20,20), 100) # create 20 x 20 matrix, where all the values are 100
b = np.zeros((20,20))     # create 20 x 20 matrix, where all the values are 0

# Alert - Numpy Broadcasting............
"""

# ------------- Bit Slicing -----------------
    r,c = grayscale.shape

    bit1 = np.zeros((r,c),dtype = np.uint8)
    bit2 = np.zeros((r,c),dtype = np.uint8)
    bit3 = np.zeros((r,c),dtype = np.uint8)
    bit4 = np.zeros((r,c),dtype = np.uint8)
    bit5 = np.zeros((r,c),dtype = np.uint8)
    bit6 = np.zeros((r,c),dtype = np.uint8)
    bit7 = np.zeros((r,c),dtype = np.uint8)
    bit8 = np.zeros((r,c),dtype = np.uint8)

    for i in range(r):
        for j in range(c):
            bit1[i][j]=grayscale[i][j] & 1


    bit2 = grayscale & 2
    bit3 = grayscale & 4
    bit4 = grayscale & 8
    bit5 = grayscale & 16
    bit6 = grayscale & 32
    bit7 = grayscale & 64
    bit8 = grayscale & 128


## masking -----------------------

    mask = np.zeros((r,c),dtype=np.uint8)
    mask[40:120,50:250] = 255
    mask = mask & grayscale
    
##  add nosie & medianblur

    r,c = noise.shape
    t = (r*c)//50
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i%2==0):
            noise[x,y] = 255
        else:
            noise[x,y] = 0
    #avaraging filter
    avg_noise = cv2.filter2D(noise, -1, avg_kernal)
    gaussain_noise = cv2.filter2D(noise, -1, gaussain_kernal)
    median_blur = cv2.medianBlur(noise, 3)
    
## --------------- hist shifting -------------
left,right,narrow = gray.copy(),gray.copy(),gray.copy()
	
	for i in range(r):
		for j in range(c):
			if(narrow[i][j]<=100):
				narrow[i][j]=100
			elif(narrow[i][j]>=180):
				narrow[i][j]=180
	
	
	#print(right.shape)
	
	left = left -80
	right = right+50
	
	org_calchist = cv2.calcHist([gray],[0],None,[256],[0,255])
	lef_hist = cv2.calcHist([left],[0],None,[256],[0,255])
	ri_hist = cv2.calcHist([right],[0],None,[256],[0,255])
	nr_hist = cv2.calcHist([narrow],[0],None,[256],[0,255])

## ----------------- morphological ---------------

"""
Concept:

In Python OpenCV,

    1) when you perform erosion operation it actually remove the white pixels and vice versa.
    2) when you perform dilation operation it actually adding the white pixels and vice versa.  

    # Opening -> Erosion >> Dilation
    # Closing -> Dilation >> Erosion 
"""

    erosion = cv2.erode(gray, kernel=kernel, iterations=1)
    dilation = cv2.dilate(gray, kernel=kernel, iterations=1)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel=kernel)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel=kernel)
    
#### custom erotion and dialation

def erosion(img, kernal):
    r, c = img.shape
    x, y = kernal.shape
    out = np.zeros((r-x-1, c-y-1))
    for i in range(r-x-1):
        for j in range(c-y-1):
            sum = np.sum(np.multiply(img[i:i+x, j:j+y], kernal))
            if(sum == 2295):
                out[i][j] = 255
    return out


def dilation(img, kernal):
    r, c = img.shape
    x, y = kernal.shape
    out = np.zeros((r-x-1, c-y-1))
    for i in range(r-x-1):
        for j in range(c-y-1):
            sum = np.sum(np.multiply(img[i:i+x, j:j+y], kernal))
            if(sum >= 255):
                out[i][j] = 255
    return out

########### ----------- Equal Hist ------------------------ ###########
 equ = cv2.equalizeHist(gray)
