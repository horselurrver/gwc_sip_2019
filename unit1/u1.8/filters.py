"""
Tutorial: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

To use: from filters import *
"""
from PIL import Image

# Returns an Image object given either an absolute path or filename in the same folder
def load_img(filename):
    im = Image.open(filename)
    return im
# Load and display image
def show_img(imageObject):
    imageObject.show()
# Save image to computer in the save folder as this file
def save_img(imageObject, filename):
    try:
        imageObject.save(filename)
    except KeyError:
        print("Error: The string '{}' needs a file extension".format(filename))
    except IOError:
        print("Error: File could not be written")
    else:
        print("'{}' was successfully saved!".format(filename))
