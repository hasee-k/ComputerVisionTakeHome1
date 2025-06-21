import cv2
import os


def reduce_intensity_levels(image_path, levels, color=True):
    
    if(color):
        img = cv2.imread(image_path)
        clr = "RGB"
    else:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
        clr = "Grayscale"   
     
    factor = 256 // levels
    reduced_img = (img // factor) * factor

 
 
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_reduced_{levels}_levels_{clr}{ext}"
    output_path = os.path.join(output_folder, output_filename)

    cv2.imwrite(output_path, reduced_img)

