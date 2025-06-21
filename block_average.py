import cv2
import numpy as np  
import os


def block_average(image_path, block_size, color=True):
    
    if(color):
        img = cv2.imread(image_path)
        clr = "RGB"
        h, w, _ = img.shape
    else:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
        clr = "Grayscale"  
        h, w = img.shape
    
    
    img_copy = img.copy()

    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            block = img[i:i+block_size, j:j+block_size]
            if block.size == 0:
                continue
            avg = int(np.mean(block))
            img_copy[i:i+block_size, j:j+block_size] = avg

    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)   
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_block_average{block_size}x{block_size}_{clr}{ext}"
    output_path = os.path.join(output_folder, output_filename)
    cv2.imwrite(output_path, img_copy)
