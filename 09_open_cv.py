# Today's lesson: track objects based on colors
import cv2
import numpy as np

width = 480
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# trackbar variables
hue_low = 10
hue_high = 20
sat_low = 0
sat_high = 255
val_low = 0
val_high = 255

# Controlling Trackbars
def on_track_1(val):
    global hue_low
    hue_low = val
    print('hue low', hue_low)

def on_track_2(val):
    global hue_high
    hue_high = val
    print('hue high', hue_high)

def on_track_3(val):
    global sat_low
    sat_low = val
    print('sat high', sat_low)

def on_track_4(val):
    global sat_high
    sat_high = val
    print(sat_high, sat_high)

def on_track_5(val):
    global val_low
    val_low = val
    print('val low', val_low)

def on_track_6(val):
    global val_high
    val_high = val
    print('val high', val)

cv2.namedWindow(winname='trackbars')
cv2.moveWindow(winname='trackbars', x=1000, y=100)
cv2.resizeWindow('trackbars', 430, 230)

cv2.createTrackbar('Hue Low', 'trackbars', 10, 179, on_track_1)
cv2.createTrackbar('Hue High', 'trackbars', 10, 179, on_track_2)
cv2.createTrackbar('Sat Low', 'trackbars', 10, 255, on_track_3)
cv2.createTrackbar('Sat High', 'trackbars', 10, 255, on_track_4)
cv2.createTrackbar('Val Low', 'trackbars', 10, 255, on_track_5)
cv2.createTrackbar('Val High', 'trackbars', 10, 255, on_track_6)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Think this as a box of lower and upper bound. Using this box we will track object on hsv frame based on color
    lower_bound = np.array([hue_low, sat_low, val_low])
    upper_bound = np.array([hue_high, sat_high, val_high])

    # Create a mask
    my_mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    my_object = cv2.bitwise_and(frame, frame, mask=my_mask)
    cv2.imshow('my object', my_object)
    cv2.resizeWindow('my object', 480, 360)
    cv2.moveWindow('my object', 400, 100)
    
    cv2.imshow('my mask', my_mask)
    cv2.resizeWindow('my mask', 480, 360)
    cv2.moveWindow('my mask', 800, 400)

    cv2.imshow('window', frame)
    cv2.moveWindow(winname='window', x=0, y=0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()