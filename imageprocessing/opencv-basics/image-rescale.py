import cv2 as cv

img = cv.imread('images/images.jpeg')

cv.imshow('girl', img)

def rescale_frame(frame, scale=.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('girl picture after resize', rescale_frame(img))

cv.waitKey(0)
