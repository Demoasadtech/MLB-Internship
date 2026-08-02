'''
rightness Adjustment
Contrast Adjustment
Gaussian Blur
Median Blur
Bilateral Filter
Image Sharpening'''
import cv2
import numpy as np
img=cv2.imread("Day15/input_images/vehicle.png")
bright=cv2.convertScaleAbs(img,alpha=2,beta=10)    # for brightness ,alpha represents contrast
'''
cv2.imshow("bright",bright)
cv2.waitKey(0)
cv2.destroyAllWindows'''


kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharp = cv2.filter2D(   #image sharpening
    img,
    -1,
    kernel
)
g_blur=cv2.GaussianBlur(img,(5,5),0)  #guassianBlur
m_blur=cv2.medianBlur(img,5)      #medianblur
b_blur=cv2.bilateralFilter(img,9,150,165)  #bilateralfilter
cv2.imshow("g_blur",g_blur)
cv2.imshow("m_blur",m_blur)
cv2.imshow("b_blur",b_blur)
cv2.imshow("sharpening",sharp)
cv2.imshow("original_image",img)
cv2.waitKey(0)
cv2.destroyAllWindows
