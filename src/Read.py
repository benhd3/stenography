from PIL import Image
import PIL

def get_image(src):
    """
    :param src: image path
    :return: returns an image object
    """
    try:
        img = Image.open(src)
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError
    except PIL.UnidentifiedImageError:
        print("File is not an image")
        raise PIL.UnidentifiedImageError
    return img