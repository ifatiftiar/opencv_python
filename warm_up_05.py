import cv2
import math
import numpy as np
from os.path import join

corners = []

# Load the input image
input_image = cv2.imread(join('demoImages', 'caligraphy.jpg'))

# Get the image width, height and resize the image
height, width, _ = input_image.shape
input_image = cv2.resize(input_image, (int(width * 0.4), int(height * 0.4)))

# Callback functions
def get_corners(event, x, y, flags, params):
    global corners
    if event == cv2.EVENT_LBUTTONDOWN:
        corners.append([x, y])
        if len(corners) == 4:
            output_width = int(math.dist(corners[0], corners[1]))
            output_height = int(math.dist(corners[0], corners[2]))
            roi_corners = np.float32(corners)
            output_corners = np.float32([[0, 0], [output_width, 0], [0, output_height], [output_width, output_height]])
            get_output(roi_corners, output_corners, output_width, output_height)
            corners = []

# Get Result
def get_output(roi_corners, output_corners, output_width, output_height):
    # Compute the perspective transformation matrix
    perspective_matrix = cv2.getPerspectiveTransform(roi_corners, output_corners)

    # Apply the perspective transformation to the input image
    output_image = cv2.warpPerspective(input_image, perspective_matrix, (output_width, output_height))

    # Display the input and output images
    cv2.imshow('Output Image', output_image)

cv2.namedWindow('Input Image')
cv2.setMouseCallback('Input Image', get_corners)
cv2.imshow('Input Image', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()