# Today lesson: Face detection using OPENCV
import cv2

width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

face_cascade = cv2.CascadeClassifier(r'.env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    
    for face in faces:
        x, y, w, h = face
        print(f'x={x}, y={y}, w={w}, h={h}')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)

    cv2.imshow('window', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
