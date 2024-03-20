# Today lesson: Understanding HSV color space
import cv2
import numpy as np

width = 780
height = 460
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
evt = 0
x_val = 0
y_val = 0

def mouse_click(event, x_pos, y_pos, flags, params):
    global evt
    global x_val
    global y_val
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        x_val = x_pos
        y_val = y_pos
    if event == cv2.EVENT_MOUSEMOVE:
        # here event is zero
        evt = event
        x_val = x_pos
        y_val = y_pos


# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('window')
cv2.setMouseCallback('window', mouse_click)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    if evt == 1:
        x = np.zeros([250, 250, 3], dtype=np.uint8)
        y = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        clr = y[y_val][x_val]
        x[:] = clr
        cv2.putText(x, str(clr), (10, 70), 2, 1, (255, 255, 255), 1)
        cv2.imshow('window color picker', x)
        cv2.moveWindow('window color picker', width, 0)
        evt = 0

    cv2.imshow('window', frame)
    cv2.moveWindow('window', 120, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
