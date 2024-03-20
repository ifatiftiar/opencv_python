# creating multiple windows and showing them in order

import cv2

width = 1280
height = 720

rows = int(input('How many rows, Boss: '))
cols = int(input('How many columns: '))

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (int(width / cols), int(height /rows)))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        break

    for i in range(rows):
        for j in range(cols):
            # trying to guess the matrix when rows = 2 and cols = 3
            # [(0,0), (0, 1), (0, 2)]
            # [(1,0), (1, 1), (1, 2)]

            window_name = f'window {i}x{j}'
            if (i + j) % 2 != 0:
                # show gray frame
                cv2.imshow(window_name, gray_frame)
            else:
                # show bgr 
                cv2.imshow(window_name, frame)

            cv2.moveWindow(window_name, int(width/cols) * j, int(height/rows * i) + 60)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()