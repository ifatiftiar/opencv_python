import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

width = 640
height = 480
screen_width = 1920
screen_height = 1080

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break

    roi = frame[0:int(height), 0:int(width/2)]
    roi_2 = frame[0:int(height), int(width/2):int(width)]
    '''
    # roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi_bgr = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
    frame[0:int(height), 0:int(width/2)] = roi_bgr
    '''
    roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_2_rgb = cv2.cvtColor(roi_2, cv2.COLOR_BGR2RGB)
    frame[0:int(height), 0:int(width/2)] = roi_hsv
    frame[0:int(height), int(width/2):int(width)] = roi_2_rgb

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()