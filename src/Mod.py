from .Read import *
import os


def encrypt_image_lsb(img_src, plaintext_src, img_out=None):
    """
    :param img_src: file path to image which is to be encrypted
    :param img_out: directory to export image to, default ./out folder
    :param plaintext_src: the text file to be encrypted into the image
    :return: Exports encrypted image file
    """
    if not os.path.isfile(img_src):
        raise FileNotFoundError("Image file not found")

    if not os.path.isfile(plaintext_src):
        raise FileNotFoundError("Plaintext file not found")

    if img_out is not None:
        if not os.path.isdir(img_out):
            raise NotADirectoryError("Image export path not found")

    # Display image properties
    analyse_image(img_src)


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
