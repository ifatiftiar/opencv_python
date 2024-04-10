# Detect face and eye
import cv2
import time

width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

face_cascade = cv2.CascadeClassifier(r'.env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'.env\Lib\site-packages\cv2\data\haarcascade_eye.xml')

start_time = time.time()
time.sleep(0.1)
while True:
    end_time = time.time()
    dt = end_time - start_time
    start_time = time.time()
    start = time.time()
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(frame_gray, 1.3, 5)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for eye in eyes:
        x, y, w, h = eye
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    fps = int(1/dt)
    cv2.putText(frame, f'{fps} FPS', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 0), 2)

    cv2.imshow('window', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
