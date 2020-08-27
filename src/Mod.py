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


def denary_binary(x, forcebitlen=None):
    """
    Takes a denary value and returns binary in a string
    :param x: denary num to be converted
    :param forcebitlen: returns binary string of certain length
    :return: binary string
    """
    out = ""
    if forcebitlen is not None:
        topbound = forcebitlen
    else:
        topbound = math.floor(math.log(x, 2))
    for i in range(topbound, -1, -1):
        if x - 2**i >= 0:
            out += "1"
            x -= 2**i
        else:
            out += "0"
    return out
