import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Cassette Deck")
clock = pygame.time.Clock()
running = True
tick = 0

x = 0
y = 0

#Text offset
x_text = x + 0
y_text = y + 0

# Cassette offset
x_cas = x + 10
y_cas = y - 20

#updaterate/speed
clockrate = 20
scale = 64
fontsize = scale

# Limit the maximum angle in degres
cas_rotaition_limit = 25

# set true/false to toggle album title artist genre
text_boxes = [True,True,True,True]

# Move value to position to display
# Example 3 to the first one to disply genre first<
layout = [0,1,2,3]

# Activate text only (true)
just_text_mode = False

if just_text_mode:
    screen = pygame.display.set_mode((scale * 16, scale * 5))
else:
    screen = pygame.display.set_mode(((scale * 16)*1, (scale * 5)*1.8))
    y_text += 128 * (scale//31)

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", fontsize)
cassette_img = pygame.image.load("Icons/Cassette 128x128.png")
fontsize += (fontsize//4)

updatedisplaysize = False

def slice_and_print():
    # Split by line
    splitdata = str(metadata).split("\\n")

    # Prep and assign lines
    data_to_text = [str(str(splitdata[0])[2:]),str(splitdata[1]),str(splitdata[2]),str(splitdata[5])]

    line = 0

    # Print text to window
    while line < 4:
        if text_boxes[line]:
            GAME_FONT.render_to(screen, (x_text, (fontsize*line)+y_text), str(data_to_text[layout[line]]), (0, 0, 0))
            line +=1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    tick += 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,0,255,0))

    # grab data from vlc
    a = subprocess.run(['vlc-ctrl',  'info'], stdout=subprocess.PIPE)
    metadata = a.stdout


    # Check for vlc metadata
    if str(metadata) == "b''":
        GAME_FONT.render_to(screen, (100, 100), "No vlc data found :(", (0, 0, 0))
    else:
        slice_and_print()
        animated_cassette = pygame.transform.rotozoom(cassette_img, (tick % cas_rotaition_limit) - (cas_rotaition_limit // 2), scale//17)
        screen.blit(animated_cassette, (x_cas, y_cas))

    # flip() the display to put your work on screen
    pygame.display.flip()

    if updatedisplaysize:
        screen = pygame.display.set_mode((scale * 16, scale * 5))
        updatedisplaysize = False

    clock.tick(clockrate)  # limits FPS to clockrate

pygame.quit()