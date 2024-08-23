import cv2
import numpy as np

frame = np.zeros((500, 500, 3), dtype=np.uint8)
draw = False
pnt1 = (0, 0)
pnt2 = pnt1

green = (0, 255, 0)
black = (0, 0, 0)

mode = 'draw'
pen_color = green
eraser_color = black

def mouseClick(evt, xPos, yPos, flag, params):
    global pnt1, pnt2, draw

    if evt == cv2.EVENT_LBUTTONDOWN:
        draw = True
        pnt1 = (xPos, yPos)
        pnt2 = pnt1

    if evt == cv2.EVENT_MOUSEMOVE and draw:
        pnt2 = (xPos, yPos)

    if evt == cv2.EVENT_LBUTTONUP:
        draw = False

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    cv2.line(frame, pnt1, pnt2, pen_color if mode == 'draw' else eraser_color, 2 if mode == 'draw' else 20)
    pnt1 = pnt2

    cv2.imshow('FRAME', frame)
    
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
    elif key == ord('d'):
        mode = 'draw'
    elif key == ord('e'):
        mode = 'eraser'

cv2.destroyAllWindows()