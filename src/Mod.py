from .Read import *
import os
import math


def analyse_image(src):
    """
    describes information about image
    :param src: path to image
    """
    img = get_image(src)
    filename = os.path.basename(src)
    print("File Name: " + filename)
    print("Image Format: " + img.format)
    print(f"Image Dimensions (pixels): w:{img.size[0]} h:{img.size[1]}")
    print(f"File Size: {os.stat(src).st_size / 1000}Kb")
    print("Image Mode: " + img.mode)
    print(f"Max encryption file size: {str(get_lsb(img.size) / 8000)}Kb")
