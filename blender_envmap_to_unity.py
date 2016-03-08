import sys
from PIL import Image

if __name__ == "__main__":
    param = sys.argv

    image = Image.open(param[1])
#    image.save("hoge.png")

    # Size of the one image.
    size = image.size[1] / 2

    new_image = Image.new("RGB", (size * 4, size * 3))

    image_0 = image.crop((0, 0, size, size))
    new_image.paste(image_0, (0, size))
    image_1 = image.crop((size, 0, size * 2 , size))
    new_image.paste(image_1, (size * 3, size))
    image_2 = image.crop((size * 2, 0, size * 3, size))
    new_image.paste(image_2, (size * 2, size))
    image_3 = image.crop((0, size, size, size * 2))
    new_image.paste(image_3, (size, size * 2))
    image_4 = image.crop((size, size, size * 2, size * 2))
    new_image.paste(image_4, (size, 0))
    image_5 = image.crop((size * 2, size, size * 3, size * 2))
    new_image.paste(image_5, (size, size))

    new_image.save("cubemap_" + image.filename)
