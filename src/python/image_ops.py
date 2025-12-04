import cv2
import numpy as np
from PIL import Image

class ImageProcessor:
    @staticmethod
    def resize_image(image_path, size=(512, 512)):
        img = cv2.imread(image_path)
        resized = cv2.resize(img, size)
        return resized

    @staticmethod
    def apply_blur(image, radius=5):
        return cv2.GaussianBlur(image, (radius, radius), 0)

    @staticmethod
    def apply_shadow(image, offset=(5, 5), color=(0, 0, 0)):
        pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return pil_img

    @staticmethod
    def color_replace(image, old_color, new_color):
        lower = np.array(old_color) - 10
        upper = np.array(old_color) + 10
        mask = cv2.inRange(image, lower, upper)
        image[mask > 0] = new_color
        return image
