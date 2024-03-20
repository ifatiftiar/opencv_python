# Drawing a Chessboard
import cv2
import numpy as np 

rows = 8
cols = 8
square_size = 50
my_board = 'my favourite chess board'

board_frame = np.zeros([rows*square_size, cols*square_size, 3], dtype=np.uint8)
print(board_frame)
for i in range(rows):
    for j in range(0, cols):
        # -> [(i, j)] -> [(0, 0), (0, 1), (0, 2), ..........., (0, 7)]
        color = (164, 201, 59) if (i + j) % 2 == 0 else  (255, 255, 255)
        # color = ((i + j) % 2) * 255
        board_frame[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = color

        # [0:50, 0:50, black], [0:50, 50:100, white], [0:50, 100:150, black]

while True:
    cv2.imshow(winname=my_board, mat=board_frame)
    cv2.moveWindow(my_board, 450, 150)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()

