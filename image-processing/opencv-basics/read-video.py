import cv2 as cv

# read image
# VideoCapture() take,
# path of the video
# Or
# take 0, 1, 2 as argument when you want to access camera 
# 0 -> webcam
# 1 -> camera 1 connected to your system
# 2 -> camera 2 connected to your system
capture = cv.VideoCapture('videos/girl-dance.mp4')

# read video frame by frame
while True:
    is_true, frame = capture.read()
    if is_true:
        cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
