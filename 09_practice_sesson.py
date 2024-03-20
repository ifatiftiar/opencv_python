import cv2
import numpy as np

width = 680
height = 360

hue_low = 168
hue_high = 179
sat_low = 199
sat_high = 255
val_low = 0
val_high = 255

from_color = np.zeros([50, 300, 3], dtype=np.uint8)
from_color = cv2.cvtColor(from_color, cv2.COLOR_BGR2HSV)

to_color = np.zeros([50, 300, 3], dtype=np.uint8)
to_color = cv2.cvtColor(to_color, cv2.COLOR_BGR2HSV)

def handle_to_color():
    to_color[:,:] = (hue_high, sat_high, val_high)
    cv2.imshow('to color', to_color)
handle_to_color()

def handle_from_color():
    from_color[:, :] = (hue_low, sat_low, val_low)
    cv2.imshow('from color', from_color)

handle_from_color()


def change_hue_low(val):
    global hue_low
    hue_low = val
    handle_from_color()

def change_hue_high(val):
    global hue_high
    hue_high = val
    handle_to_color()

def change_sat_low(val):
    global sat_low
    sat_low = val
    handle_from_color()

def change_sat_high(val):
    global sat_high
    sat_high = val
    handle_to_color()

def change_val_low(val):
    global val_low
    val_low = val
    handle_from_color()

def change_val_high(val):
    global val_high
    val_high = val
    handle_to_color()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 430, 250)

cv2.createTrackbar('hue low', 'trackbars', hue_low, 179, change_hue_low)
cv2.createTrackbar('hue high', 'trackbars', hue_high, 179, change_hue_high)
cv2.createTrackbar('sat low', 'trackbars', sat_low, 255, change_sat_low)
cv2.createTrackbar('sat high', 'trackbars', sat_high, 255, change_sat_high)
cv2.createTrackbar('val low', 'trackbars', val_low, 255, change_val_low)
cv2.createTrackbar('val high', 'trackbars', val_high, 255, change_val_high)


while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if not ret:
        break

    lower_bound = np.array([hue_low, sat_low, val_low])
    upper_bound = np.array([hue_high, sat_high, val_high])

    my_mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    my_object = cv2.bitwise_and(frame, frame, mask=my_mask)

    cv2.imshow('my object', my_object)
    cv2.resizeWindow('my object', 640, 360)

    cv2.imshow('my mask', my_mask)
    cv2.resizeWindow('my mask', 640, 360)

    cv2.imshow('window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

