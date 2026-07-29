'''
Image Processing Toolkit

Build a menu driven Python application using OpenCV that allows a user to perform different operations on an image.

The application should support:

Load an image
Convert to grayscale
Resize image
Rotate image
Flip image
Crop image
Draw shapes
Add custom text
Save the processed image'''



import cv2
import os
image = None
def load_image():
    global image
    path = input("Enter image path: ")
    image = cv2.imread(path)

def grayscale():
    global image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

def resize():
    global image
    w = int(input("Width: "))
    h = int(input("Height: "))
    image = cv2.resize(image, (w, h))

def rotate():
    global image

    print("1. 90")
    print("2. 180")
    print("3. 270")

    ch = input("Choice: ")

    if ch == "1":
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif ch == "2":
        image = cv2.rotate(image, cv2.ROTATE_180)

    elif ch == "3":
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

def flip_image():
    global image

    print("1. Horizontal")
    print("2. Vertical")
    print("3. Both")

    choice = input("Enter Choice: ")

    if choice == "1":
        image = cv2.flip(image, 1)

    elif choice == "2":
        image = cv2.flip(image, 0)

    elif choice == "3":
        image = cv2.flip(image, -1)

    print("Image Flipped Successfully")

def crop_image():
    global image

    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    w = int(input("Enter Width: "))
    h = int(input("Enter Height: "))

    image = image[y:y+h, x:x+w]

    print("Image Cropped Successfully") 

def draw_shape():
    global image

    print("\n1. Rectangle")
    print("2. Circle")
    print("3. Line")

    choice = input("Enter Choice: ")

    if choice == "1":

        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))

        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        b = int(input("Enter Blue Value (0-255): "))
        g = int(input("Enter Green Value (0-255): "))
        r = int(input("Enter Red Value (0-255): "))


        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            color = (b, g, r),
            thickness = int(input("Enter Thickness: "))
        )
        
    elif choice == "2":

        x = int(input("Enter Center X: "))
        y = int(input("Enter Center Y: "))

        radius = int(input("Enter Radius: "))
        b = int(input("Enter Blue Value (0-255): "))
        g = int(input("Enter Green Value (0-255): "))
        r = int(input("Enter Red Value (0-255): "))

        cv2.circle(
            image,
            (x, y),
            radius,
            color = (b, g, r),
            thickness = int(input("Enter Thickness: "))
        )

    elif choice == "3":

        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        b = int(input("Enter Blue Value (0-255): "))
        g = int(input("Enter Green Value (0-255): "))
        r = int(input("Enter Red Value (0-255): "))
        cv2.line(
            image,
            (x1, y1),
            (x2, y2),
            color = (b, g, r),
            hickness = int(input("Enter Thickness: "))
        )

    else:
        print("Invalid Choice")
        return

    print("Shape Drawn Successfully")
    
def add_text():
    global image

    text = input("Enter Text: ")

    x = int(input("Enter X Position: "))
    y = int(input("Enter Y Position: "))
    b = int(input("Enter Blue Value (0-255): "))
    g = int(input("Enter Green Value (0-255): "))
    r = int(input("Enter Red Value (0-255): "))
    cv2.putText(
        image,
        text,
        (x,y),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color = (b, g, r),
        thickness = int(input("Enter Thickness: "))
    )

    print("Text Added Successfully") 

def save_image():
    global image

    filename = input("Enter File Name: ")

    cv2.imwrite(filename, image)

    print("Image Saved Successfully")     

def preview_image():
    global image

    cv2.imshow("Output Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

import os

def delete_image():
    filename = input("Enter File Name to Delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("Image Deleted Successfully")
    else:
        print("File Not Found")      

while True:
    print(f'{"="*15}Image Processing Toolkit{"="*15}')
    print("1. Load Image")
    print("2. Grayscale")
    print("3. Resize")
    print("4. Rotate")
    print("5. Flip")
    print("6. Crop")
    print("7. Draw Shape")
    print("8. Add Text")
    print("9. Preview")
    print("10. Save")
    print("11. Delete")
    print("0. Exit")
    print("="*54)

    choice = input("Enter Choice =>(0 to 11): ")

    if choice == "1":
        load_image()

    elif choice == "2":
        grayscale()

    elif choice == "3":
        resize()

    elif choice == "4":
        rotate()

    elif choice == "5":
        flip_image()
    
    elif choice == "6":
        crop_image()
    
    elif choice == "7":
        draw_shape()

    elif choice == "8":
        add_text()
        
    elif choice == "9":
        preview_image()
        
    elif choice == "10":
        save_image() 

    elif choice == "11":
        delete_image()        

    elif choice == "0":
        break        