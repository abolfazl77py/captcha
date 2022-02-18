"""generate captcha image"""

from PIL import Image, ImageDraw, ImageFont
import os
from random import randint, choice


def rand_color():
    return randint(0,999)



def generate_captcha(path, size="""this is for size"""):
    imag = Image.new("RGB",size,color="white")
    imag.save(path, "png")
    capt_img = Image.open(path)
    d1 = ImageDraw.Draw(capt_img)
    font= ImageFont.truetype("img/RansomRegular.ttf", 35)
    d1.text((65, 10), "Dr5Ey6", fill= (0,100,0), font=font)
    capt_img.save(path)

def mathematical_operations():
    randnum2, randnum1 = randint(0,99), randint(0,99)
    m = ('s', 't')
    math_choice = choice(m)
    if math_choice == 't':
        return f"{randnum1} + {randnum2}"
    else:
        return f"{randnum1} - {randnum2}"


def generate_mathematical_captcha(path, size):
    """
    path
    type: str | file direction and its name

    size
    type: tuple | size of image you want
    """
    number = mathematical_operations()
    imag = Image.new("RGB",size,color="white")
    imag.save(path, "png")
    capt_img = Image.open(path)
    d1 = ImageDraw.Draw(capt_img)
    font= ImageFont.truetype("img/RansomRegular.ttf", 35)
    d1.text((65, 10), str(number), fill= (200, 40, 0), font=font)
    capt_img.save(path)

generate_mathematical_captcha()
