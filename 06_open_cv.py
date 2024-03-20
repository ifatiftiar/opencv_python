# Today lesson:  Process Mouse Clicks
import cv2

width = 720
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

evt = 0

def mouse_click(event, x_pos, y_pos, flags, params):
    global evt
    global pnt
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        pnt = (x_pos, y_pos)
        print('Mouse event was: ', event)
        print('at position', (x_pos, y_pos))
    if  event == cv2.EVENT_LBUTTONUP:
        evt = event
        pnt = (x_pos, y_pos)
        print('Mouse event was: ', event)
        print('at position', (x_pos, y_pos))

cv2.namedWindow(winname='my window')
cv2.setMouseCallback('my window', mouse_click)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    if evt == 1:
        cv2.circle(img=frame, center=pnt, radius=10, color=(255, 0, 0), thickness=-1)
    if  evt == 4:
        cv2.circle(img=frame, center=pnt, radius=10, color=(255, 0, 0), thickness=-1)

    cv2.imshow('my window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
