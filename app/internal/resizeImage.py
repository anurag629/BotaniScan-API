import cv2

def resizeImage(image, width, height):
    """
    Resizes an image to the specified width and height.
    """
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

