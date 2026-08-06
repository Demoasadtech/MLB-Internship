import cv2

img = cv2.imread("Day17/input_images/p1.png")  # load image
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # convert grayscale

_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)   # convert into binary (bakcground is black and object is white like matrix)

contours, _ = cv2.findContours(   # find contour means find external edges and bounding area of object
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for cnt in contours:   #load all object in image one by one

    epsilon = 0.02 * cv2.arcLength(cnt, True)       #calculate perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)   # find important points

    corners = len(approx)

    x,y,w,h = cv2.boundingRect(approx)

    if corners == 3:  #draw and text condition
        shape = "Triangle"

    elif corners == 4:

        ratio = w / float(h)

        if 0.95 <= ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif corners >= 8:
        shape = "Circle"

    else:
        shape = "Polygon"

    cv2.drawContours(img,[approx],-1,(0,255,0),3)  #draw contours

    cv2.putText(   #show text
        img,
        shape,
        (x,y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,0,0),
        2
    )

cv2.imshow("Shapes", img)
cv2.imwrite("Day17/output_images/label_results.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()