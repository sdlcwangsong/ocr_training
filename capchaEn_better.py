#!/usr/bin/env python
#coding: utf-8
import PIL.Image, PIL.ImageDraw, PIL.ImageFont, PIL.ImageFilter
import string, random
 
fontPath = "/System/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/"
 
# 获得随机四个字母
def getRandomChar():
    return [random.choice(string.digits) for _ in range(5)]
 
# 获得颜色
def getRandomColor():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
 
# 获得验证码图片
def getCodePiture():
    width = 250
    height = 100
    # 创建画布
    image = PIL.Image.new('RGB', (width, height), (255, 255, 255))
    font = PIL.ImageFont.truetype(fontPath + 'VeraIt.ttf', 40)
    draw = PIL.ImageDraw.Draw(image)
    # 创建验证码对象
    code = getRandomChar()
    print(code)
    # 把验证码放到画布上
    for t in range(5):
        draw.text((50 * t + 10, 25), code[t], font=font, fill=getRandomColor())
    # 填充噪点
    #for _ in range(random.randint(0,0)):
    #    draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())
    # 模糊处理
    #image = image.filter(PIL.ImageFilter.BLUR)
    # 保存名字为验证码的图片
    image.save('capcha.jpg', 'jpeg');
 
if __name__ == '__main__':
    getCodePiture()