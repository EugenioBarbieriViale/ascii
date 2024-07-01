from PIL import Image

img = Image.open("input.png")

pixelmap = img.load()
ascii = " .,:;ox%#@"

def resize_img(img, new_width=150):
    width, height = img.size
    new_height = int(new_width * (height / width))
    return (new_width, new_height)

img = img.resize(resize_img(img))
width, height = img.size

img = img.convert("L")

rows = []
for i in range(height):
    cols = []
    for j in range(width):
        p = img.getpixel((j,i))

        cols.append(ascii[p*(len(ascii)-1)//255])
    rows.append(cols)

for row in rows:
    print("".join(row))
