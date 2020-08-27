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
    :param forcebitlen: returns binary string of certain length (will not shorten a binary string)
    :return: binary string
    """
    bin = format(x, "b")

    if forcebitlen is None:
        return bin

    if len(bin) < forcebitlen:
        bin = "0" * (forcebitlen - len(bin)) + bin
    return bin


def binary_denary(bin):
    """
    Takes a binary string and returns a denary value
    :param bin: binary string
    :return: denary value
    """
    total = 0
    count = 0
    for i in range(len(bin) - 1, -1, -1):
        if bin[i] == "1":
            total += 2 ** count
        count += 1
    return total


def text_binary(text):
    for i in text:
        print(format(ord(i), "b"))
