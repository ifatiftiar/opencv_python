# Calculate and Display fps

# hint: to calculate fps calculate how many times the while loop in running in a second, (frequency of the while loop)
# f = 1/T
# T -> How much time it takes to reach the end of the while loop
import cv2
import time

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

fps_filter = 30
start_time = time.time()
time.sleep(0.1)
while True:
    end_time = time.time()
    dt = end_time - start_time
    start_time = time.time()
    ret, frame = cam.read()

    if not ret:
        break

    fps = int(1 / dt)
    
    # Applying low pass filter
    fps_filter = fps_filter * 0.95 + fps * 0.05
    fps = str(int(fps_filter))

    cv2.putText(img=frame, 
                text=fps + ' fps',
                org=(100, 50), 
                fontFace=cv2.FONT_HERSHEY_COMPLEX, 
                fontScale=2, 
                color=(0, 255, 0),
                thickness=2)
    cv2.imshow('my window', frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()