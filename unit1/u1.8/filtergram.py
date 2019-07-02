from filters import *

"""
Part 1:
- Load image from computer
- Save image to new file on computer under different filename
"""

filename1 = 'chikorita.png'
filename2 = 'trump.jpg'
savename = 'chikorita2.png'

if __name__ == "__main__":
    im = load_img(filename2)
    # obamacon(im)
    adjustBrightness(im, True)
    # darker(im)
    # show_img(im)
    # save_img(im, savename)
