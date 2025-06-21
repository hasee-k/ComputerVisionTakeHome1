import cv2
import os

def average_filter(image_path, kernel_size, color=True):
    if(color):
        img = cv2.imread(image_path)
        clr = "RGB"
    else:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
        clr = "Grayscale"   
    blurred = cv2.blur(img, (kernel_size, kernel_size))
    
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_fitered_kernel_size{kernel_size}_{clr}{ext}"
    output_path = os.path.join(output_folder, output_filename)
    
    
    cv2.imwrite(output_path, blurred)
    
    