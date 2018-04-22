import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 随机字母
def RndChar():
    return chr(random.randint(65, 90))


# 随机颜色1
def RndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def RndColor1():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 设置宽高
width, height = 240, 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('/home/wangpei/PycharmProjects/littletest/011 生成验证码图片/yahei.ttc', size=36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=RndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), RndChar(), font=font, fill=RndColor1())
# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show('code.jpg')
