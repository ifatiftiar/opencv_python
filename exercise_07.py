# Exercise: Moving and resizing window using trackbars
import cv2

width = 780
height = 460
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

pos_x = 0
pos_y = 0

def handle_move_x_trackbar(val):
    global pos_x
    pos_x = val
    cv2.moveWindow(winname='window', x=pos_x, y=pos_y)

def handle_move_y_trackbar(val):
    global pos_y
    pos_y = val
    cv2.moveWindow(winname='window', x=pos_x, y=pos_y)

def handle_set_width(val):
    global width 
    width = val
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def handle_set_height(val):
    global height
    height = val

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow(winname='window')
cv2.namedWindow(winname='trackbars')
cv2.resizeWindow(winname='trackbars', width=400, height=200)

cv2.createTrackbar('move window x', 'trackbars', 0, 900, handle_move_x_trackbar)
cv2.createTrackbar('move window y', 'trackbars', 0, 300, handle_move_y_trackbar)
cv2.createTrackbar('set  width', 'trackbars', 0, 1280, handle_set_width)
cv2.createTrackbar('set  height', 'trackbars', 0, 800, handle_set_width)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow('window', frame)
    cv2.moveWindow(winname='window',  x=pos_x, y=pos_y)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
