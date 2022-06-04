import cv2 as cv

capture = cv.VideoCapture('videos/girl-dance.mp4')


def rescale_frame(frame, scale = .75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    is_true, frame = capture.read()

    if is_true:
        cv.imshow('frame original', frame)
        cv.imshow('frame resize', rescale_frame(frame))


    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
