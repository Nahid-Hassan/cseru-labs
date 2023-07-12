import math
# from pprint import pprint as print

pi = 3.142857
m = 8
n = 8

# Function to find discrete cosine transform and print it
def dctTransform(matrix):
	dct = []
	for i in range(m):
		dct.append([None for _ in range(n)])
	
	print(dct)

	for i in range(m):
		for j in range(n):

			# ci and cj depends on frequency as well as
			# number of row and columns of specified matrix
			if (i == 0):
				ci = 1 / (m ** 0.5)
			else:
				ci = (2 / m) ** 0.5
			if (j == 0):
				cj = 1 / (n ** 0.5)
			else:
				cj = (2 / n) ** 0.5

			# sum will temporarily store the sum of
			# cosine signals
			sum = 0
			for k in range(m):
				for l in range(n):

					dct1 = matrix[k][l] * math.cos((2 * k + 1) * i * pi / (
						2 * m)) * math.cos((2 * l + 1) * j * pi / (2 * n))
					sum = sum + dct1

			dct[i][j] = ci * cj * sum

	for i in range(m):
		for j in range(n):
			print(dct[i][j], end="\t")
		print()

# Driver code
matrix = [[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255],
		[255, 255, 255, 255, 255, 255, 255, 255]]

dctTransform(matrix)
