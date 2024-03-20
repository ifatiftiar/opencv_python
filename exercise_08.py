# Today lesson: Making a rainbow color window (applying the knowledge of HSV color space)
import cv2
import numpy as np

height = 255
width = 180

window_1 = np.zeros([width, height, 3], dtype=np.uint8)


for i in range(0, width):
    for j in range(0, height):
        window_1[i, j] = ((i % 180), (j % 255), 255)

window_1 = cv2.cvtColor(window_1, cv2.COLOR_HSV2BGR)
print('done')
while True:
    cv2.imshow('window 1', window_1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
