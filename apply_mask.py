import cv2
import numpy as np
import os

def apply_mask(original_image, mask):

    return np.where(mask[..., None] == 255, original_image, 0)

def process_directory(original_image_dir, mask_dir, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for mask_filename in os.listdir(mask_dir):
        if mask_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            mask_path = os.path.join(mask_dir, mask_filename)
            original_image_path = os.path.join(original_image_dir, mask_filename)

            if not os.path.exists(original_image_path):
                print(f"Warning: Original image not found for {mask_filename}. Skipping.")
                continue

            original_image = cv2.imread(original_image_path)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

            if original_image is None:
                print(f"Error: Unable to load original image from {original_image_path}")
                continue
            if mask is None:
                print(f"Error: Unable to load mask image from {mask_path}")
                continue
            if original_image.shape[:2] != mask.shape[:2]:
                print(f"Error: The original image and mask must have the same resolution for {mask_filename}. Skipping.")
                continue

            result_image = apply_mask(original_image, mask)
            output_image_path = os.path.join(output_dir, mask_filename)
            cv2.imwrite(output_image_path, result_image)
            print(f"Processed and saved: {output_image_path}")


original_image_dir = 'path/to/original_image_directory'  
mask_dir = 'path/to/mask_directory' 
output_dir = 'path/to/output_directory' 

process_directory(original_image_dir, mask_dir, output_dir)