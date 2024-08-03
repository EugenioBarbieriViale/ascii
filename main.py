from PIL import Image
import pygame, sys

img = Image.open("ex.png")

pixelmap = img.load()
text = " .,:;ox%#@"

def img_resize(img):
    width, height = img.size

    w = width // len(text)
    h = height // len(text)

    img = img.resize((w, h))
    # img = img.resize((1000, 800))

    return img

def get_lum(pixel):
    # return int((0.3 * pixel[0]) + (0.59 * pixel[1]) + (0.11 * pixel[2]))
    return ((pixel[0] + pixel[1] + pixel[2])//3) * (len(text)-1) // 255


img = img_resize(img)
# img = img.convert("L")

width, height = img.size

pygame.init()
clock = pygame.time.Clock()

X, Y = 1500, 1000

screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption("ASCII")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    font = pygame.font.SysFont("Comic Sans MS", len(text))

    for y in range(height):
        for x in range(width):
            p = img.getpixel((x, y))

            lum = get_lum(p)

            display_text = font.render("{c}".format(c = text[lum]), 1, (255,255,255))
            
            dx = x*8
            dy = y*9

            screen.blit(display_text, (dx, dy))


    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

pygame.quit()
