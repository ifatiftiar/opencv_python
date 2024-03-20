# Today lesson:  Trackbars in OpenCV
import cv2

def handle_trackbar1(value):
    global x_pos
    x_pos = value


def handle_trackbar2(value):
    global y_pos
    y_pos = value

def handle_trackbar3(value):
    global radius
    radius = value

def handle_trackbar4(value):
    global thickness
    thickness = value

    if thickness == 0:
        thickness = -1

width = 780
height = 460
x_pos = int(width / 2)
y_pos = int(height / 2)
radius = 30
thickness = 1

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow(winname='trackbars')
cv2.resizeWindow(winname='trackbars', width=400, height=200)
cv2.moveWindow(winname='trackbars', x = width + 250, y =100)
cv2.createTrackbar('x_pos', 'trackbars', 0, width, handle_trackbar1)
cv2.createTrackbar('y_pos', 'trackbars', 0, height, handle_trackbar2)
cv2.createTrackbar('radius', 'trackbars', 0, int(height/2), handle_trackbar3)
cv2.createTrackbar('tickness', 'trackbars', 0, 7, handle_trackbar4)


while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    cv2.circle(img=frame, center=(x_pos, y_pos), radius=radius, color=(255, 255, 0), thickness=thickness)
    cv2.imshow('window', frame)
    cv2.moveWindow(winname='window', x=350, y = 100)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
