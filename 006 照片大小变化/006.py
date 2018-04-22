from PIL import Image
import glob, os

def new_size():
    for file in glob.glob('/home/wangpei/PycharmProjects/littletest/006 照片大小变化/pictures/*.jpg'):
        filepath, filename = os.path.split(file)
        im = Image.open(file)
        w, h = im.size
        if w > 640:
            x = w / 640.0
            w = 640
            h = int(w / x)
        if h > 1136:
            x = w / 1136.0
            h = 1136
            w = int(h / x)
        new_im = im.resize((w, h), Image.ANTIALIAS)
        new_im.save('new_' + filename)

new_size()
