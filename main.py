from PIL import Image

img = Image.open("ex.png")

pixelmap = img.load()
text = " .,:;ox%#@"

def img_resize(img):
    width, height = img.size

    w = width // len(text)
    h = height // len(text)

    img = img.resize((w, h))

    return img

def get_lum(pixel):
    # lum = (0.3 * p[0]) + (0.59 * p[1]) + (0.11 * p[2])
    return ((pixel[0] + pixel[1] + pixel[2])//3) * (len(text)-1) // 255


img = img_resize(img)
# img = img.convert("L")

width, height = img.size

for y in range(height):
    for x in range(width):
        p = img.getpixel((x, y))

        lum = get_lum(p)
        print(text[lum], end="")

    print("")
