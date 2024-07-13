from PIL import Image

img = Image.open(str(input("Enter photos name: ")))
pixelmap = img.load()

list = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']
ascii = [list[-i] for i in range(len(list)+1) if i != 0]

def resize_img(img, new_width=150):
    width, height = img.size
    new_height = int(new_width * (height / width) / 2)
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
