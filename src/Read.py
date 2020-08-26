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


def get_pixel_map(img):
    """
    :param img: Image object
    :return: pixel map of image object
    """
    pixels = img.load()
    return pixels


def get_image_dim(img):
    """
    :param img: image object
    :return: image dimensions
    """
    return img.size


def get_lsb(dim):
    """
    Gets the number of least significant bits that can be used for encryption
    :param dim: dimensions of image
    :return: number of least significant bits
    """
    # temp bytes_per_pix till proper implementation
    bytes_per_pix = 3
    lsbs = dim[0] * dim[1] * bytes_per_pix  # least significant bits
    return lsbs