import matplotlib.pyplot as plt
import cv2

def main():
	img_path = 'sunset.jpg'
	print(img_path)
	rgb = plt.imread(img_path)
	print(rgb.shape, rgb.max(), rgb.min())
	
	red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
	print(red.shape, red.max(), red.min())
	
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	print(grayscale.shape, grayscale.max(), grayscale.min())
	
	_, binary = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
	
	
	'''	Plot histograms. '''
	plt.figure(figsize = (20, 20))
	plt.subplot(2, 3, 1)
	plt.title('RGB')
	plt.imshow(rgb)
	plt.subplot(2, 3, 2)
	plt.title('Red')
	plt.imshow(red)
	plt.subplot(2, 3, 3)
	plt.title('Green')
	plt.imshow(green)
	plt.subplot(2, 3, 4)
	plt.title('Blue')
	plt.imshow(blue)
	plt.subplot(2, 3, 5)
	plt.title('Grayscale')
	plt.imshow(grayscale, cmap='gray')
	plt.subplot(2, 3, 6)
	plt.title('Binary')
	plt.imshow(binary, cmap='gray')
	plt.show()


if __name__ == '__main__':
	main()