import cv2
import numpy as np

frame = np.zeros((500, 500, 3), dtype=np.uint8)

draw = False
p1 = (0, 0) # top left corner point
p2 = p1 # bottom right corner point

def mouseClick(evt, xPos, yPos, flags, params):
    global draw, p1, p2
    # print(f'evt:{evt} xPos:{xPos} yPos:{yPos}')
    # print(flags)
    # print(params)
    if evt == cv2.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (xPos, yPos)
        p2 = p1

    if evt == cv2.EVENT_MOUSEMOVE and draw:
        p2 = (xPos, yPos)
    
    if evt == cv2.EVENT_LBUTTONUP:
        draw = False

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    frame = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
    cv2.imshow('FRAME', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
