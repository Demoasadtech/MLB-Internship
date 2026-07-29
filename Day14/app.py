import gradio as gr     # import libraries
import cv2

SAMPLE_IMAGES = [       # sample image creation
    "Day14/Sample input images/f1.png",
    "Day14/Sample input images/f2.png",
    "Day14/Sample input images/f3.png",
    "Day14/Sample input images/f4.png",
    "Day14/Sample input images/f5.png"
    ]

def process_image(       #function for process images
    image,
    operation,
    width,
    height,
    rotate_angle,
    flip_type,
    crop_x,
    crop_y,
    crop_width,
    crop_height,
    shape_type,       
    shape_x1,          
    shape_y1,           
    shape_x2,          
    shape_y2,           
    text_input,          
    text_x,              
    text_y,               
    color_blue,
    color_green,
    color_red,
    thickness,
    rad_ius
):

    if image is None:             # check image exist
        return None, "⚠️ Please upload an image before proceeding."

    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)   # load image in RAM

    #  Grayscale operation
    if operation == "Grayscale":
        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )
        img = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

    # Resize operation

    elif operation == "Resize":
        img = cv2.resize(
            img,
            (int(width), int(height))
        )

    #  Rotate operation

    elif operation == "Rotate":
        if rotate_angle == "90":
            img = cv2.rotate(
                img,
                cv2.ROTATE_90_CLOCKWISE
            )
        elif rotate_angle == "180":
            img = cv2.rotate(
                img,
                cv2.ROTATE_180
            )
        elif rotate_angle == "270":
            img = cv2.rotate(
                img,
                cv2.ROTATE_90_COUNTERCLOCKWISE
            )


        #  Flip opeeration

    elif operation == "Flip":
        if flip_type == "Horizontal":
            img = cv2.flip(img, 1)
        elif flip_type == "Vertical":
            img = cv2.flip(img, 0)
        elif flip_type == "Both":
            img = cv2.flip(img, -1)


       #  Crop operation 

    elif operation == "Crop":
        x = int(crop_x)
        y = int(crop_y)
        w = int(crop_width)
        h = int(crop_height)
        img = img[y:y+h, x:x+w]

    # Draw Shape operation

    elif operation == "Draw Shape":
        c_r=int(color_red)
        c_g=int(color_green)
        c_b=int(color_blue)
        x1 = int(shape_x1)
        y1 = int(shape_y1)
        x2 = int(shape_x2)
        y2 = int(shape_y2)
        if shape_type == "Rectangle":
            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (c_b, c_g, c_r),
                thickness=int(thickness)
            )

        elif shape_type == "Circle":
            radius = int(rad_ius)
            cv2.circle(
                img,
                (x1, y1),
                radius,
                (c_b, c_g, c_r),
                thickness=input(thickness)
            )

        elif shape_type == "Line":
            cv2.line(
                img,
                (x1, y1),
                (x2, y2),
                (c_b, c_g, c_r),
                thickness=input(thickness)
            )

    #  Add Text operation  

    elif operation == "Add Text":
        c_r=int(color_red)
        c_g=int(color_green)
        c_b=int(color_blue)  
        cv2.putText(
            img,
            text_input,
            (int(text_x), int(text_y)),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (c_b, c_g, c_r),
            thickness=int(thickness)
        )

     # return output & convert BGR to RGB  & save file
    output = cv2.cvtColor(
            img,
           cv2.COLOR_BGR2RGB
           )
    cv2.imwrite("processed_image.png", img)   
    return output, "processed_image.png"

    # show slected operation inputs
def update_visibility(operation):
    return (
        gr.update(visible=(operation == "Resize")),       
        gr.update(visible=(operation == "Resize")),       
        gr.update(visible=(operation == "Rotate")),       
        gr.update(visible=(operation == "Flip")),       
        gr.update(visible=(operation == "Crop")),    
        gr.update(visible=(operation == "Crop")),    
        gr.update(visible=(operation == "Crop")),        
        gr.update(visible=(operation == "Crop")),         
        gr.update(visible=(operation == "Draw Shape")),   
        gr.update(visible=(operation == "Draw Shape")), 
        gr.update(visible=(operation == "Draw Shape")), 
        gr.update(visible=(operation == "Draw Shape")), 
        gr.update(visible=(operation == "Draw Shape")), 
        gr.update(visible=(operation == "Add Text")),     
        gr.update(visible=(operation == "Add Text")), 
        gr.update(visible=(operation == "Add Text")), 
        gr.update(visible=(operation == "Draw Shape" or operation == "Add Text")), 
        gr.update(visible=(operation == "Draw Shape" or operation == "Add Text")), 
        gr.update(visible=(operation == "Draw Shape" or operation == "Add Text")),
        gr.update(visible=(operation == "Draw Shape" or operation == "Add Text")),
        gr.update(visible=(operation == "Circle")),                            
        
    )

#UI operation
with gr.Blocks(title="Image Processing Toolkit") as app:

    gr.Markdown(
            """
            # 🤖 🛠️ Image Processing Toolkit
            Upload an image and perform different processing  operations on images
    
            **Developed by Muhammad Asad Ali**
            """
        )
    
    with gr.Row():

        input_image = gr.Image(
            type="numpy",
            label="Upload Image"
        )
        if SAMPLE_IMAGES:
             gr.Examples(
                examples=SAMPLE_IMAGES,
                inputs=input_image,
                label="Or try a sample image",
                 )
        output_image = gr.Image(
            label="Processed Image"
        )
    download_file = gr.File(
    label="Download Processed Image"
)    

    operation = gr.Dropdown(
        choices=[
            "Grayscale",
            "Resize",
            "Rotate",
            "Flip",
            "Crop",
            "Draw Shape",
            "Add Text"
        ],
        value="Grayscale",
        label="Select Operation"
    )

    rotate_angle = gr.Dropdown(    # selection operation
            choices=[
                    "90",
                    "180",
                    "270"
                ],
                value="90",
                label="Rotate Angle",
                visible=False
            )
    
    width = gr.Number(
        value=600,
        label="Width",
        visible=False
    )

    height = gr.Number(
       value=400,
       label="Height",
       visible=False
    )

    flip_type = gr.Dropdown(
       choices=[
            "Horizontal",
            "Vertical",
            "Both"
        ],
        value="Horizontal",
        label="Flip Type",
        visible=False
    )

    crop_x = gr.Number(
       value=0,
       label="Crop X",
       visible=False
    )

    crop_y = gr.Number(
       value=0,
       label="Crop Y",
       visible=False
    )

    crop_width = gr.Number(
       value=100,
       label="Crop Width",
       visible=False
    )

    crop_height = gr.Number(
     value=100,
     label="Crop Height",
     visible=False
    )

    #Draw Shape inputs
    shape_type = gr.Dropdown(
        choices=["Rectangle", "Circle", "Line"],
        value="Rectangle",
        label="Shape Type",
        visible=False
    )

    shape_x1 = gr.Number(
        value=50,
        label="Shape X1 (or center X for circle)",
        visible=False
    )

    shape_y1 = gr.Number(
        value=50,
        label="Shape Y1 (or center Y for circle)",
        visible=False
    )

    shape_x2 = gr.Number(
        value=150,
        label="Shape X2 (or edge point X for circle)",
        visible=False
    )

    shape_y2 = gr.Number(
        value=150,
        label="Shape Y2 (or edge point Y for circle)",
        visible=False
    )

    #Add Text inputs
    text_input = gr.Textbox(
        value="Learning AI/ML is like debugging life nothing works on the first try😅",
        label="Text",
        visible=False
    )

    text_x = gr.Number(
        value=50,
        label="Text X",
        visible=False
    )

    text_y = gr.Number(
        value=50,
        label="Text Y",
        visible=False
    )
    color_blue = gr.Number(
    value=0,
    label="Blue (0-255)",
    visible=False
)

    color_green = gr.Number(
    value=0,
    label="Green (0-255)",
    visible=False
)

    color_red = gr.Number(
    value=255,
    label="Red (0-255)",
    visible=False
)

    thickness = gr.Number(
    value=2,
    label="Thickness",
    visible=False
)

    rad_ius = gr.Number(
    value=50,
    label="Circle Radius",
    visible=False
)

    # when dropdown visibilty update
    operation.change(
        fn=update_visibility,
        inputs=operation,
        outputs=[
            width,
            height,
            rotate_angle,
            flip_type,
            crop_x,
            crop_y,
            crop_width,
            crop_height,
            shape_type,
            shape_x1,
            shape_y1,
            shape_x2,
            shape_y2,
            text_input,
            text_x,
            text_y,
            color_blue,
            color_green,
            color_red,
            thickness,
            rad_ius


        ]
    )

    with gr.Row():

     process_btn = gr.Button(
        "Process Image",
        variant="primary"
    )

     clear_btn = gr.ClearButton(   #for clear images & data
        components=[
            input_image,
            output_image,
            operation,
            width,
            height,
            rotate_angle,
            flip_type,
            crop_x,
            crop_y,
            crop_width,
            crop_height,
            shape_type,
            shape_x1,
            shape_y1,
            shape_x2,
            shape_y2,
            text_input,
            text_x,
            text_y,
            color_blue,
            color_green,
            color_red,
            thickness,
            rad_ius,
            download_file
        ],
        value="Clear"
    )
     
    process_btn.click(
      fn=process_image,
      
   inputs=[
     input_image,
     operation,
     width,
     height,
     rotate_angle,
     flip_type,
     crop_x,
     crop_y,
     crop_width,
     crop_height,
     shape_type,
     shape_x1,
     shape_y1,
     shape_x2,
     shape_y2,
     text_input,
     text_x,
     text_y,
     color_blue,
     color_green,
     color_red,
     thickness,
     rad_ius
      ],

    outputs=[
    output_image,
    download_file
]
    

)
    
if __name__ == "__main__":
    app.launch()