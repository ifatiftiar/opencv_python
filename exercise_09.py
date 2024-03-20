# DETECT MULTIPLE COLOR OPENCV
import cv2
import numpy as np

width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

hue_low_1 = 61
hue_high_1 = 93
hue_low_2 = 21
hue_high_2 = 85
sat_low = 70
sat_high = 170
val_low = 75
val_high = 255

def handle_hue_low_1(val):
    global hue_low_1
    hue_low_1 = val

def handle_hue_high_1(val):
    global hue_high_1
    hue_high_1 = val

def handle_hue_low_2(val):
    global hue_low_2
    hue_low_2 = val

def handle_hue_high_2(val):
    global hue_high_2
    hue_high_2 = val

def handle_sat_low(val):
    global sat_low
    sat_low = val

def handle_sat_high(val):
    global sat_high
    sat_high = val

def handle_val_low(val):
    global sat_low
    sat_low = val

def handle_val_high(val):
    global sat_high
    sat_high = val

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 400, 300)
cv2.createTrackbar('hue low 1', 'trackbars', hue_low_1, 179, handle_hue_low_1)
cv2.createTrackbar('hue high 1', 'trackbars', hue_high_1, 179, handle_hue_high_1)
cv2.createTrackbar('hue low 2', 'trackbars', hue_low_2, 179, handle_hue_low_2)
cv2.createTrackbar('hue high 2', 'trackbars', hue_high_2, 179, handle_hue_high_2)
cv2.createTrackbar('sat low', 'trackbars', sat_low , 255,  handle_sat_low)
cv2.createTrackbar('sat high', 'trackbars', sat_high, 255,  handle_sat_high)
cv2.createTrackbar('val low', 'trackbars',  val_low, 255,  handle_val_low)
cv2.createTrackbar('val high', 'trackbars',  val_high, 255,  handle_val_high)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound_1 = np.array([hue_low_1, sat_low, val_low])
    upper_bound_1 = np.array([hue_high_1, sat_high, val_high])

    lower_bound_2 = np.array([hue_low_2, sat_low, val_low])
    upper_bound_2 = np.array([hue_high_2, sat_high, val_high])

    mask_1 = cv2.inRange(frame_hsv, lower_bound_1, upper_bound_1)
    mask_2 = cv2.inRange(frame_hsv, lower_bound_2, upper_bound_2)
    mask_comp = mask_1 | mask_2

    my_obj = cv2.bitwise_or(frame, frame, mask=mask_comp)

    cv2.imshow('my mask', mask_1)
    cv2.imshow('my mask 2', mask_2)
    cv2.imshow('window', my_obj)

    cv2.resizeWindow('my mask', 350, 250)
    cv2.resizeWindow('my mask 2', 350, 250)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()