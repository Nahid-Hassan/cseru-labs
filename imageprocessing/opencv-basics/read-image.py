import cv2 as cv

# imread function take the relative or absolute path of the images
# and return the matrix of the images
img = cv.imread('./images/images.jpeg')
print(img)
# imshow function is used for showing the image 
# it take two arguments an optional name and matrix
cv.imshow('Beautiful Girl', img)

# waitkey() function of Python OpenCV allows users to display a 
# window for given milliseconds or until any key is pressed. It takes 
# time in milliseconds as a parameter and waits for the given time to 
# destroy the window, if 0 is passed in the argument it waits till any key is pressed.
cv.waitKey(5000)


#! issue
# python has no in-built machanism to deal with large image 
