"""generate captcha image"""
from PIL import Image, ImageDraw, ImageFont
import os
from random import randint, choice

def generate_captcha(path, size):
    imag = Image.new("RGB",size,color="white")
    imag.save(path, "png")
    capt_img = Image.open(path)
    d1 = ImageDraw.Draw(capt_img)
    font= ImageFont.truetype("img/RansomRegular.ttf", 35)
    d1.text((65, 10), "Dr5Ey6", fill= (100,50,0), font=font)
    capt_img.save(path)

def math_captcha():
    randnum2, randnum1 = randint(0,99), randint(0,99)
    m = ('s', 't')
    math_choice = choice(m)
    if math_choice == 's':
        print(f"{randnum1} + {randnum2} :{randnum1 + randnum2}")
    else:
        print(f"{randnum1} - {randnum2} :{randnum1 - randnum2}")

math_captcha()
# generate_captcha("res.png", (200,50))
# imag = Image.new("RGB",(400,200),color="white")
# imag.save('img/image.png', "png")
# img = Image.open("img/image.png")
# d1 = ImageDraw.Draw(img)
# font= ImageFont.truetype("img/RansomRegular.ttf", 30)
# d1.text((65, 10), "Dr5Ey6", fill= (255,0,0), font=font)
# img.show()
# img.save("img/result.png")

# def generate_captcha():
#     img.save('image.png', "png")

# try:
#     os.chdir("img")
# except FileNotFoundError:
#     os.mkdir("img")