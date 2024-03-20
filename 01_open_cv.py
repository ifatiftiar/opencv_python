# Install openCV and launch webcam
import cv2

# print(cv2.__version__)
cam = cv2.VideoCapture(0) # create a camera object and capture video

while True:
    _, frame = cam.read() # grabbing a frame from the camera

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # creating a new gray frame

    # ************
    # We read a frame and show a frame, read a frame and show a frame; We can
    # make the magic here. We can do things to the frame and show the frame.
    # This is the place where the magic happens.
    # ************

    # cv2.imshow('my webcam', frame)
    cv2.imshow('my webcam', gray_frame)
    cv2.moveWindow('my webcam', 0, 0) # moves the window to (0, 0) when the program loads instead of just putting the window in a random position

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release() # making our camera free when the program is closed. If we don't do this it may block our camera.