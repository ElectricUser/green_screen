import cv2 as cv
# "videos/greenscreen-demo.mp4"
cap = cv.VideoCapture("videos/greenscreen-demo.mp4")
background = cv.imread("images/beach_bg.jpeg")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    background_rsz = cv.resize(background, frame.shape[:2][::-1])

    # convert to hsv
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define green range
    lower_green = (30, 50, 80)
    higher_green = (80, 255, 255)

    # create mask to detect greens
    mask = cv.inRange(frame_hsv, lower_green, higher_green)

    masked_frame = cv.bitwise_and(frame, frame, mask=mask)

    res = frame - masked_frame

    masked_background = cv.bitwise_and(background_rsz, background_rsz, mask=mask)

    result = res + masked_background

    cv.imshow('frame', result)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
