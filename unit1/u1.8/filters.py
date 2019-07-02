"""
Tutorial: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
Docs: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
How to loop through pixels: https://www.reddit.com/r/learnprogramming/comments/4w1duu/how_can_i_loop_through_every_pixel_in_an_image/

To use: from filters import *
"""
from PIL import Image

darkConstant = 2
brightConstant = 2
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
# Applies obama's filter to image
# Returns new image with the filter applied
def obamacon(imageObject):
    outputName = 'obamacon.png'
    out = Image.new('I', imageObject.size)
    # Get height and width of image
    width, height = imageObject.size
    # x and y represent position of pixel in image
    for x in range(width):
        for y in range(height):
            colorValues = imageObject.getpixel((x,y))
            total = sum(colorValues)
            # Check intensities
            if total < 182: # Low
                imageObject.putpixel((x, y), (0, 51, 76))
            elif total < 364: # Medium-Low
                imageObject.putpixel((x, y), (217, 26, 33))
            elif total < 546: # Medium-High
                imageObject.putpixel((x, y), (112, 150, 158))
            else: # High
                imageObject.putpixel((x, y), (252, 227, 166))
    imageObject.save(outputName)
    show_img(load_img(outputName))

# Map function for making image darker
def darkerMult(n):
    return n // darkConstant

# Map function for making image brighter
def brighterMult(n):
    return n * brightConstant

def adjustBrightness(imageObject, brighter):
    outputName = 'brighter.png' if brighter else 'darker.png'
    out = Image.new('I', imageObject.size)
    # Get height and width of image
    width, height = imageObject.size
    print('Brighter!') if brighter else print('Darker!')
    for x in range(width):
        for y in range(height):
            if brighter:
                imageObject.putpixel((x, y), tuple(map(brighterMult, imageObject.getpixel((x, y)))))
            else:
                imageObject.putpixel((x, y), tuple(map(darkerMult, imageObject.getpixel((x, y)))))
    imageObject.save(outputName)
    show_img(load_img(outputName))
