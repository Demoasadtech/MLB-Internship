# translation code  
import cv2
import numpy as np
img=cv2.imread("Day15/input_images/landscape.png")
rows,cols=img.shape[:2]
scale = np.float32([
    [1, 0, 100],
    [0, 1, -50]
])
translate=cv2.warpAffine(img,scale,(cols,rows))
'''cv2.imshow("translated",translate)
cv2.waitKey(0)
cv2.destroyAllWindows'''

#Rotation
center=(cols//2,rows//2)
rotate=cv2.getRotationMatrix2D(center,30,1)
rotation=cv2.warpAffine(img,rotate,(cols,rows))
'''cv2.imshow("Rotation",rotation)
cv2.waitKey(0)
cv2.destroyAllWindows'''


'''
Scaling
Affine Transformation
Perspective Transformation'''

scaled=cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_CUBIC
)
'''
cv2.imshow("scales_image",scaled)
cv2.waitKey(0)
cv2.destroyAllWindows'''

pts1 = np.float32([
    [50,50],
    [200,50],
    [50,200]
])
pts2 = np.float32([
    [10,100],
    [200,50],
    [100,250]
])
affine = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(img, affine, (cols, rows))
'''
cv2.imshow("Affine", result)
cv2.waitKey(0)
cv2.destroyAllWindows'''

pts1 = np.float32([
    [56,65],
    [368,52],
    [28,387],
    [389,390]
])
pts2 = np.float32([
    [25,34],
    [300,0],
    [0,400],
    [250,230]
])
perspective = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, perspective, (cols,rows))
cv2.imshow("Perspective", result)
cv2.imwrite("Day15/output_images/tilt.png",result)
cv2.waitKey(0)
cv2.destroyAllWindows()