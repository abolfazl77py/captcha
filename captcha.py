"""generate captcha image"""

from PIL import Image, ImageDraw, ImageFont
import string
from random import randint, choice


def rand_color():
    return choice(["red", "blue", "gray", "green", "black", "pink"])

def rand_str():
    return ''.join(choice(string.digits + string.ascii_letters) for i in range(6))


def captcha_generator(path, size=(250, 50)):
    imag = Image.new("RGB",size,color="white")
    imag.save(path, "png")
    capt_img = Image.open(path)
    d1 = ImageDraw.Draw(capt_img)
    font= ImageFont.truetype("font/RansomRegular.ttf", 35)
    d1.text((65, 10),rand_str(), fill=rand_color(), font=font)
    capt_img.save(path)

def mathematical_operations():
    randnum1, randnum2 = randint(0,99), randint(0,99)
    m = ('sum', 'subtract')
    math_choice = choice(m)
    if math_choice == 'sum':
        return f"{randnum1} + {randnum2}"
    else:
        if randnum1 >= randnum2:
            return f"{randnum1} - {randnum2}"
        return f"{randnum2} - {randnum1}"


def mathematical_captcha(path, size= (250, 50)):
    """
    path
    type: str | file direction and its name (.png)

    size
    type: tuple | size of image you want
    """
    number = mathematical_operations()
    imag = Image.new("RGB",size,color="white")
    imag.save(path, "png")
    capt_img = Image.open(path)
    d1 = ImageDraw.Draw(capt_img)
    font= ImageFont.truetype("font/RansomRegular.ttf", 35)
    d1.text((65, 1), str(number), fill= rand_color(), font=font)
    capt_img.save(path)

