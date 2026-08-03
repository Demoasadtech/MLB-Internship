'''Morphological Operations


Learn and implement:

Erosion
Dilation
Opening
Closing
Morphological Gradient
Top Hat
Black Hat'''

import cv2
import numpy as np
img=cv2.imread("Day16/input_images/document.png")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2BGRA)
#kernel = np.ones((5,5), np.uint8)
eros=cv2.erode(gray,kernel=(5,5),iterations=10)
dialte=cv2.dilate(gray,kernel=(5,5),iterations=10)
opening = cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel=(5,5))
close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel=(5,5))
gradient = cv2.morphologyEx(gray,cv2.MORPH_GRADIENT,kernel=(5,5))
top_hat = cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,kernel=(5,5))
black_hat = cv2.morphologyEx(gray,cv2.MORPH_BLACKHAT,kernel=(5,5))
cv2.imshow("original",img)
cv2.imshow("erosion",eros)
cv2.imshow("dilation",dialte)
cv2.imshow("opening",opening)
cv2.imshow("close",close)
cv2.imshow("gradient",gradient)
cv2.imshow("top_hat",top_hat)
cv2.imshow("black_hat",black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows
