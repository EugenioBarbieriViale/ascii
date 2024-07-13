from PIL import Image

img = Image.open("man.png")

# Change pixel block size
r = 5
c = 13


pixelmap = img.load()
ascii = " .,:;ox%#@"

width, height = img.size

img = img.convert("L")

def average_lum(X, Y, r, c, grid):
    lum = 0
    for y in range(c):
        for x in range(r):
            current = grid[X+x,Y+y]
            lum += (0.3 * current[0]) + (0.59 * current[1]) + (0.11 * current[2])

    return int((lum // (c*r)))

rows = []
for y in range(0, height-c, c):
    cols = []
    for x in range(0, width-r, r):
        lum = average_lum(x, y, r, c, pixelmap)
        
        cols.append(ascii[lum*(len(ascii)-1)//255])
    rows.append(cols)

for row in rows:
    print("".join(row))
