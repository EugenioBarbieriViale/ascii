import cv2
from os import system
from PIL import Image

system("mkdir frames/")

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

def resize_img(img, new_width=150):
    width, height = img.size
    new_height = int(new_width * (height / width) / 2)
    return (new_width, new_height)

ascii = " .,:;ox%#@"
for i in range(frame_number):
    img = Image.open(f"frames/frame_{i}.jpg")
    img = img.resize(resize_img(img))
    img = img.convert("L")

    width, height = img.size
    rows = []
    for i in range(height):
        cols = []
        for j in range(width):
            p = img.getpixel((j,i))

            cols.append(ascii[p*(len(ascii)-1)//255])
        rows.append(cols)

    for row in rows:
        print("".join(row))

system("rm -r frames/")
