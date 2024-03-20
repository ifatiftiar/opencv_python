import cv2

width = 320
height = 240

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


while True:
    _, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('window 01', frame)
    cv2.imshow('window 02', gray_frame)
    cv2.imshow('window 03', gray_frame)
    cv2.imshow('window 04', frame)

    cv2.moveWindow('window 01', 250, 50)
    cv2.moveWindow('window 02', 580, 50)
    cv2.moveWindow('window 03', 250, 330)
    cv2.moveWindow('window 04', 580, 330)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
