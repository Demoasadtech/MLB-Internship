#Sobel operator edge detection along horizontal and vertical axis
import cv2
img=cv2.imread("Day16/input_images/document.png")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2BGRA)
sobel=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
'''
cv2.imshow("original",img)
cv2.imshow("sobel_operator",sobel)
cv2.waitKey(0)
cv2.destroyAllWindows'''

'''
laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplace = cv2.convertScaleAbs(laplacian)
cv2.imshow("original",img)
cv2.imshow("laplaician_operator",laplace)
cv2.waitKey(0)
cv2.destroyAllWindows
'''

canny=cv2.Canny(gray,150,250)
cv2.imshow("original",img)
cv2.imshow("canny_operator",canny)
cv2.imwrite("Day16/output_images/canny.png",canny)
cv2.waitKey(0)
cv2.destroyAllWindows

