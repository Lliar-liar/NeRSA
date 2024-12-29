import cv2
import numpy as np
import os

def process_image(image_path, value, target_width, target_height):
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    binary_image = np.where(gray_image == value, 255, 0).astype(np.uint8)
    resized_image = cv2.resize(binary_image, (target_width, target_height), interpolation=cv2.INTER_NEAREST)

    return resized_image

def process_directory(input_dir, output_dir, value, target_width, target_height):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_image_path = os.path.join(input_dir, filename)
            output_image = process_image(input_image_path, value, target_width, target_height)
            output_image_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_image_path, output_image)
            print(f"Processed and saved: {output_image_path}")
input_directory = 'path/to/input_directory'  
output_directory = 'path/to/output_directory'  
target_value = 12 
target_width = 800  
target_height = 600  

process_directory(input_directory, output_directory, target_value, target_width, target_height)