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
y_text = y - 64

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

# Don't print album if it's the same as the title, ussuallymeaning it's a single
ignore_album_if_single = True

# Just ignores genre if empty
ignore_genre_if_empty = True

# Activate text only (true)
just_text_mode = True

if just_text_mode:
    screen = pygame.display.set_mode((scale * 16, scale * 4))
else:
    screen = pygame.display.set_mode(((scale * 16)*1, (scale * 5)*1.8))
    y_text += 128 * (scale//31)

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", fontsize)
cassette_img = pygame.image.load("Icons/Cassette 128x128.png")
fontsize += (fontsize//4)

updatedisplaysize = False
is_single = False


def animation():
    animated_cassette = pygame.transform.rotozoom(cassette_img, (tick % cas_rotaition_limit) - (cas_rotaition_limit // 2), scale//17)
    screen.blit(animated_cassette, (x_cas, y_cas))

def slice_and_print():
    # Split by line
    splitdata = str(metadata).split("\\n")

    # Prep and assign lines
    data_to_text = [str(str(splitdata[0])[2:]),str(splitdata[1]),str(splitdata[2]),str(splitdata[5])]


    # Check if single
    if ignore_album_if_single:
        a = data_to_text[0][12:]
        b = data_to_text[1][12:]
        if a == b:
            is_single = True
        else:
            is_single = False

    line = 0

    # Print text to window
    while line < 4:
        a = text_boxes[line]
        # Check ignore album stuff
        if ignore_album_if_single:
            b = layout[line] != 0
        else:
            b = True
        
        # Test if genre is empty
        c = True
        if layout[line] == 3:
            if str(data_to_text[layout[line]]) == "genre     : ":
                c = False
            else:
                c = True

        # Print text to screen
        if a and b and c:
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
        if not just_text_mode:
            animation()


    # flip() the display to put your work on screen
    pygame.display.flip()

    if updatedisplaysize:
        screen = pygame.display.set_mode((scale * 16, scale * 5))
        updatedisplaysize = False

    clock.tick(clockrate)  # limits FPS to clockrate

pygame.quit()