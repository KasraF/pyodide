from CSE8AImage import *

def convert_to_red():
    img = load_img("cat.jpg")
    for y in range(height(img)):
        for x in range(width(img)):
            pix = img[y][x]
            img[y][x] = [pix[0],0,0]
    save_img(img, "red-cat.jpg")

convert_to_red()
