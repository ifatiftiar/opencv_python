# Today's Lesson: Putting Text, Rectangles and Circles on images
import cv2

width = 1260
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# setting width and height of windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cam.set(cv2.CAP_PROP_FPS, 30) # setting FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    # frame[50:130, :] = (0, 255, 0) -> directly manupulating the frame [2D array]

    cv2.rectangle(img=frame, pt1=(0, 50), pt2=(400, 200), color=(0, 255, 0),thickness= -1) # -> a thickness of negative one makes the shape solid
    cv2.circle(img=frame, center=(int(width/2), int(height/2)), radius=150, color=(255, 0, 0,), thickness=3)
    cv2.putText(img=frame, text='Boom boom!!', org=(100, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 0, 255))

    cv2.imshow('window', frame)
    cv2.moveWindow('window', 150, 50)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
