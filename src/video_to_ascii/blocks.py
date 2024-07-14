import cv2
from os import system
from PIL import Image

system("clear")
video = cv2.VideoCapture("cat.webm")

frame_number = 0

while True:
    success, frame = video.read()
    if success:
        cv2.imwrite(f"frames/frame_{frame_number}.jpg", frame)
    else:
        break

    frame_number += 1

video.release()

def average_lum(X, Y, r, c, grid):
    lum = 0
    for y in range(c):
        for x in range(r):
            current = grid[X+x,Y+y]
            lum += (0.3 * current[0]) + (0.59 * current[1]) + (0.11 * current[2])

    return int((lum // (c*r)))

def draw(img, width, height):
    pixelmap = img.load()

    rows = []
    for y in range(0, height-c, c):
        cols = []
        for x in range(0, width-r, r):
            lum = average_lum(x, y, r, c, pixelmap)
            
            cols.append(ascii[lum*(len(ascii)-1)//255])
        rows.append(cols)

    for row in rows:
        print("".join(row))

ascii = " .,:;ox%#@"
for i in range(frame_number):
    img = Image.open(f"frames/frame_{i}.jpg")
    width, height = img.size

    # r = width // 60
    # c = height // 30
    r = 5
    c = 10

    draw(img, width, height)
