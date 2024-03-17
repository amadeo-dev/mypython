import cv2
import numpy as np


img = cv2.imread('fd.jpg')
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25 )


cv2.imshow('image',img)
cv2.waitKey(2000)


im2 = np.zeros((5, 5, 5), dtype = np.uint8)

print(im2)