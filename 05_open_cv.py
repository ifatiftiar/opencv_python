# Today's lesson: Understanding Region of Interest
import cv2

width = 680
height = 320
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_roi = frame[280: 370, 200: 400]
    frame_roi_gray = cv2.cvtColor(src=frame_roi, code=cv2.COLOR_BGR2GRAY)
    frame_roi_bgr = cv2.cvtColor(src=frame_roi_gray, code=cv2.COLOR_GRAY2BGR)

    frame[280: 370, 200: 400] = frame_roi_bgr

    cv2.imshow('window', frame)
    cv2.imshow('frame roi', frame_roi)
    cv2.imshow('frame gray roi', frame_roi_gray)

    cv2.moveWindow(winname='window', x = 300, y = 100)
    cv2.moveWindow(winname='frame roi', x = 960, y = 100)
    cv2.moveWindow(winname='frame gray roi', x = 960, y = 230)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()