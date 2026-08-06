# create contour 
import cv2

img = cv2.imread("Day17/input_images/p1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY_INV
)

contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for cnt in contours:

    area = cv2.contourArea(cnt)

    if area < 100:
        continue

    # Draw contour
    cv2.drawContours(img, [cnt], -1, (0,255,0), 2)






'''   # Area
    print("Area:", area)

    # Perimeter
    perimeter = cv2.arcLength(cnt, True)
    print("Perimeter:", perimeter)

    # Bounding Rectangle
    x, y, w, h = cv2.boundingRect(cnt)

    cv2.rectangle(
        img,
        (x,y),
        (x+w,y+h),
        (255,0,0),
        2
    )

    # Minimum Enclosing Circle
    (cx,cy), radius = cv2.minEnclosingCircle(cnt)

    cv2.circle(
        img,
        (int(cx), int(cy)),
        int(radius),
        (0,0,255),
        2
    )'''

cv2.imshow("Contours", img)
cv2.imwrite("detected_results", img)
cv2.waitKey(0)
cv2.destroyAllWindows()