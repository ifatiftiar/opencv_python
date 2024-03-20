# exercise
import cv2, random

width = 780
height = 460
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# total rows: 480 and total columns = 640
row_start = 0
row_end = 200
col_start = 0
col_end = 200
row_direction = 1
col_direction = 1
dy = random.randint(3, 8)
dx = random.randint(3, 8)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    bgr_gray_frame = cv2.cvtColor(src=gray_frame, code=cv2.COLOR_GRAY2BGR)
    frame_roi = frame[row_start:row_end, col_start:col_end] # getting the region of interest

    bgr_gray_frame[row_start:row_end, col_start:col_end] = frame_roi

    row_start += dy * row_direction
    row_end += dy * row_direction
    col_start += dx * col_direction
    col_end += dx * col_direction

    # bounce back the colored region when it reaches the edge
    if row_start <= 0 or row_end >= 480:
        row_direction *= -1

    if col_start <= 0 or col_end >=640:
        col_direction *= -1

    cv2.imshow('window', bgr_gray_frame)
    cv2.moveWindow('window', 450, 100)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
