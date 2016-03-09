import sys
from PIL import Image

if __name__ == "__main__":
    param = sys.argv

    if len(param) == 1 or len(param) > 3:
        sys.exit(0)

    image = Image.open(param[1])

    # Size of the one image.
    size = image.size[1] / 2

    if len(param) == 3 and param[2] == "-t":
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

        new_image.save("cubemap_t_" + image.filename)

    else:
        new_image = Image.new("RGB", (size * 6, size))

        image_0 = image.crop((0, 0, size, size))
        new_image.paste(image_0, (size, 0))
        image_1 = image.crop((size, 0, size * 2 , size))
        new_image.paste(image_1, (size * 5, 0))
        image_2 = image.crop((size * 2, 0, size * 3, size))
        new_image.paste(image_2, (0, 0))
        image_3 = image.crop((0, size, size, size * 2))
        new_image.paste(image_3, (size * 3, 0))
        image_4 = image.crop((size, size, size * 2, size * 2))
        new_image.paste(image_4, (size * 2, 0))
        image_5 = image.crop((size * 2, size, size * 3, size * 2))
        new_image.paste(image_5, (size * 4, 0))

        new_image.save("cubemap_" + image.filename)
