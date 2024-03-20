# Today's goal: Understanding images as 2D array
import cv2
import numpy as np 

# frame = np.zeros([3,2], dtype=np.uint8)
# frame[1,1] = 1
# frame[2,0] = 1

# frame = np.zeros([256, 256], dtype=np.uint8)
# frame[0:125, 0: 125] = 1
# frame[0:125, 125: ] = 1
# frame[:, 254:] = 100

# drawing images
frame = np.zeros([256, 256], dtype=np.uint8)
# frame[20:60, 50:90] = 255
# frame[0, 0:] = 255
# frame[:, :125] = 255
# frame[:, :] = 125
# frame[:, 125:] = 255
# frame[:125, :] = 255
# frame[125:, :] = 255
# frame[125, 125] = 255

# -> Let's create colorful images
# frame = np.zeros([256, 256, 3], dtype=np.uint8)
# frame[:85, :] = [255, 0, 0] # BGR color format, so that's blue color
# frame[86:, :] = [0, 0, 255]
# frame[170:, :] = [0, 255, 0]

while True:
    cv2.imshow(winname='my image', mat=frame)
    cv2.moveWindow(winname='my image', x=500, y=200)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()