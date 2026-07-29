

import cv2 as cv
import numpy as np
import datetime
import os
image=cv.imread("Day14/Sample input images/f1.png")
'''if image is None:
    print("image is not found")
    exit()
cv.imshow("image show ", image)
print("Shape :", image.shape)
print("Size  :", image.size)
print("Data Type :", image.dtype)
print("Type :", type(image))'''
'''
cv.rectangle(image,(20,20),(250,250),(255,0,0),-1)
cv.imshow("line ", image)
cv.waitKey(0)
cv.destroyAllWindows()'''
'''
cv.circle(image,(300,300),100,(255,0,0),-1)
cv.imshow("line ", image)
cv.waitKey(0)
cv.destroyAllWindows()'''
'''
cv.putText(image,"how are you",(300,300),cv.FONT_HERSHEY_DUPLEX,2,(255,0,0),3)
cv.imshow("line ", image)
cv.waitKey(0)
cv.destroyAllWindows()'''
'''
rotate=cv.rotate(image,cv.ROTATE_90_CLOCKWISE)
cv.imshow("line ", rotate)
cv.waitKey(0)
cv.destroyAllWindows()'''

'''
flip=cv.flip(image,-1)
cv.imshow("line ", flip)
cv.waitKey(0)
cv.destroyAllWindows()'''

'''
crop=image[100:300,300:500]
cv.imshow("line ", crop)
cv.waitKey(0)
cv.destroyAllWindows()'''






'''
Coding Practice

Implement the following programs:

Read an image and display its dimensions, number of channels, and file size.
Convert a color image to grayscale.
Resize an image to different resolutions.
Crop different regions of an image.
Rotate the image by 90°, 180°, and 270°.
Flip the image horizontally and vertically.
Draw:

   
Rectangle
Circle
Line
Polygon
Add custom text (your name and today's date) on the image.
Save all processed images into an output folder.'''





#practice problems 

image=cv.imread("Day14/Sample input images/f1.png")
height, width, channels = image.shape
file_size=os.path.getsize("Day14/Sample input images/f1.png")
print("Width :", width)
print("Height:", height)
print("Channels:", channels)
print("file Size:", file_size)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

'''
cv.imshow("Original", image)
cv.imshow("Gray", gray)      # convert RGB & BGR  to gray scale
'''
re_size=cv.resize(image,(300,300))  #resize image
#cv.imshow("resize",re_size)
crop=image[250:500,400:600]
#cv.imshow("resize",crop)    #crop images
rotate90 = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)   # rotate images
rotate180 = cv.rotate(image, cv.ROTATE_180)
rotate270 = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
'''
cv.imshow("Original", image)
cv.imshow("90 Degree", rotate90)
cv.imshow("180 Degree", rotate180)
cv.imshow("270 Degree", rotate270)'''

horizontal = cv.flip(image, 1)  # flip image
vertical = cv.flip(image, 0)
both = cv.flip(image, -1)
'''
cv.imshow("Original", image)   
cv.imshow("Horizontal Flip", horizontal)
cv.imshow("Vertical Flip", vertical)
'''
cv.rectangle(
    image,
    (50, 50),
    (250, 200),
    (255, 0, 0),
    3
)
cv.circle(
    image,
    (450, 125),
    70,
    (0, 255, 0),
    3
)
#cv.imshow("Rectangle", image)

# Draw Polygon
points = np.array([
    [500, 400],
    [650, 350],
    [750, 450],
    [700, 550],
    [550, 550]
], np.int32)

points = points.reshape((-1, 1, 2))

cv.polylines(
    image,
    [points],
    True,
    (255, 0, 255),
    3
)

cv.putText(    #add name
    image,
    "Name: Asad",
    (50, 560),
    cv.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 0, 0),
    2
)


# Add Today Date
today = datetime.datetime.now().strftime("%d-%m-%Y")  #shw current date and time

cv.putText(   #show time on image
    image,
    f"Date: {today}",
    (230, 350),
    cv.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 0, 0),
    2
)
cv.imshow("image", image)
cv.imwrite("Day14/output_images/practice_output1.png",image)
cv.waitKey(0)  
cv.destroyAllWindows()