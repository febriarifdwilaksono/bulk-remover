import torch
from rembg import remove
from PIL import Image
import cv2
import numpy as np

class BackgroundRemover:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = None

    def remove_background(self, image_path, mode='standard'):
        try:
            # Open image
            img = Image.open(image_path).convert('RGBA')
            
            # Remove background using rembg
            output = remove(img, model_name='u2net' if mode == 'standard' else 'u2netp')
            
            # Save result
            output_path = image_path.replace('.png', '_no_bg.png').replace('.jpg', '_no_bg.png')
            output.save(output_path)
            
            return output_path
        except Exception as e:
            raise Exception(f'Error processing image: {str(e)}')
