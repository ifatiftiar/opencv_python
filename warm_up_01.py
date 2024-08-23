import cv2
import numpy as np
from os.path import join

antony_img = cv2.imread(join('demoImages', 'known', 'Anthony Fauci.jpg'))
bill_img = cv2.imread(join('demoImages', 'known', 'Bill Barr.jpg'))

antony_img = cv2.resize(antony_img, (300, 300))
bill_img = cv2.resize(bill_img, (300, 300))

compound_img = np.concatenate((antony_img, bill_img), axis=1)
compound_img_gray = cv2.cvtColor(compound_img, cv2.COLOR_BGR2GRAY)

compound_img_color = cv2.cvtColor(compound_img_gray, cv2.COLOR_GRAY2BGR)


final_res = np.concatenate((compound_img, compound_img_color), axis=0)

cv2.imshow('Final Output', final_res)
cv2.waitKey()
cv2.destroyAllWindows()