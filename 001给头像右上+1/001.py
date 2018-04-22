'''
给图片右上角+1
'''

from PIL import Image, ImageFont, ImageDraw


def Addnum(file, new_file):
    im = Image.open(file)
    width,height = im.size

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("yahei.ttc",min(width//6,height//6))
    draw.text((width*0.75,height*0.075),'1',font=font,fill=(255,33,33,255))

    im.save(new_file)


ImageFile = '001.png'
NewImage = 'new-001.png'
Addnum(ImageFile, NewImage)
