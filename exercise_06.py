import cv2

width = 780
height = 460

evt = 0
roi_exist = False
start = None
end = None

def mouse_click(event, x_pos, y_pos, flags, params):
    global evt
    global start
    global end

    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        start = (x_pos, y_pos)
        print('lbtn mouse event: ', evt)
    
    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        end = (x_pos, y_pos)
        print('rbtn mouse event', evt)

    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow(winname='mouse click')
cv2.setMouseCallback(window_name='mouse click', on_mouse=mouse_click)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    if evt == 1 or evt == 4:
        if  start and end:
            roi = frame[start[1]:end[1], start[0]:end[0]]
            cv2.imshow(winname='roi', mat=roi)
            cv2.moveWindow(winname='roi', x=830, y = 100)
            roi_exist = True
            cv2.rectangle(img=frame, pt1=start, pt2=end,color=(255, 0, 0), thickness=2)

    if evt == 2 and roi_exist:
        cv2.destroyWindow(winname='roi')
        roi_exist = False

    cv2.imshow(winname='mouse click', mat=frame)
    cv2.moveWindow(winname='mouse click', x= 200, y = 100)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()