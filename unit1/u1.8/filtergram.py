from filters import *

"""
Part 1:
- Load image from computer
- Save image to new file on computer under different filename
"""

filename = 'chikorita.png'
savename = 'chikorita2.png'

if __name__ == "__main__":
    im = load_img(filename)
    show_img(im)
    save_img(im, savename)
