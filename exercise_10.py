# controlling window position using computer vision
# TODO:
# -> detect the object
# -> put a bounding box around the object
# -> get object location
# -> change the position of the window based on the position of the object
import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

width = 640
height = 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

hue_low = 0
hue_high = 20
sat_low = 174
sat_high = 255
val_low = 57
val_high = 245

curr_win_x = int(1920/2 - width)
curr_win_y = int(1080/2 - height)

def handle_hue_low(val):
    global hue_low
    hue_low = val

def handle_hue_high(val):
    global hue_high
    hue_high = val

def handle_sat_low(val):
    global sat_low
    sat_low = val

def handle_sat_high(val):
    global sat_high 
    sat_high = val

def handle_val_low(val):
    global val_low
    val_low = val

def handle_val_high(val):
    global val_high
    val_high = val

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 255, 235)
cv2.createTrackbar('hue low', 'Trackbars', hue_low, 180, handle_hue_low)
cv2.createTrackbar('hue high', 'Trackbars', hue_high, 180, handle_hue_high)
cv2.createTrackbar('sat low', 'Trackbars', sat_low, 255, handle_sat_low)
cv2.createTrackbar('sat high', 'Trackbars', sat_high, 255, handle_sat_high)
cv2.createTrackbar('val low', 'Trackbars', val_low, 255, handle_val_low)
cv2.createTrackbar('val high', 'Trackbars', val_high, 255, handle_val_high)

cv2.namedWindow('frame')
cv2.moveWindow('frame', curr_win_x, curr_win_y)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([hue_low, sat_low, val_low])
    upper_bound = np.array([hue_high, sat_high, val_high])

    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            x, y, w, h = cv2.boundingRect(mask)
            # cv2.drawContours(frame, [contour], 0, (0, 0, 255), 3)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

            x = np.interp(x, [0, width], [-(1920/2), 1920/2])
            y = np.interp(y, [0, height], [(1080/2), -1080/2])

            cv2.moveWindow('frame', int(curr_win_x+x), int(curr_win_y-y))
    if not ret:
        break
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()