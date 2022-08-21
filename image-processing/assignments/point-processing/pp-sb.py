'''	
	------------------
	Point processing.
	------------------
	Sangeeta Biswas
	Associate Professor
	Dept. of Computer Science & Engineering
	University of Rajshahi
	Rajshahi, Bangladesh
	
	7.6.2022
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	'''	Load an RGB image.	'''
	img_path = 'sunset.jpg'
	rgb = plt.imread(img_path)
	print(rgb.shape)
		
	'''	Convert the RGB image into grayscale and binary image.	'''
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	print(grayscale.shape)
	
	'''	Negative by point processing. '''
	#	1st way of Negation
	processed_img1 = 255 - grayscale
	
	#	2nd way of Negation
	r, c = grayscale.shape
	processed_img2 = np.zeros((r,c), dtype = np.uint8)
	for x in range(r):
		for y in range(c):
			processed_img2[x, y] = 255 - grayscale[x, y]
		
	'''	Plot images. '''
	img_set = [rgb, grayscale, processed_img1, processed_img2]
	title_set = ['RGB', 'Grayscale', 'Negative-1', 'Negative-2']
	plot_img(img_set, title_set)

def plot_img(img_set, title_set):
	n = len(img_set)
	plt.figure(figsize = (20, 20))
	for i in range(n):
		img = img_set[i]
		ch = len(img.shape)
	
		plt.subplot( 2, 2, i + 1)
		if (ch == 3):
			plt.imshow(img_set[i])
		else:
			plt.imshow(img_set[i], cmap = 'gray')
		plt.title(title_set[i])
	plt.show()		
	
if __name__ == '__main__':
	main()