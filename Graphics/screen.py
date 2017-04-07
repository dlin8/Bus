#!~/usr/bin/env python3


from subprocess import Popen, PIPE
from os import remove
import screen


# FUNction list:
## createScreen(width, height)                         L22
## clearScreen(screen)                                 L42
## writePpmFile(screen, fileName, #<1>#comment)        L53
## saveExtension(screen, fname)                        L85
## display(screen)                                     L101


# createScreen(width, height)
# Creates a 2D array representing pixels to later write as a ppm file.
## arguments:
## width: int; width of screen.
## height: int; height of screen.
def createScreen(width, height):
    screen = []
    
    for i in range(0, width):
        screen.append([])
        for j in range(0, height):
            screen[i].append([0,0,0])
            
    return screen
# All functions conform to drawing and accessing where the origin is in the to right:
# x increases from to the right,
# y increases from to the bottom,
# z increases from to the front.
# Positions relative to the screen.


# clearScreen(screen)
# Sets all 'pixels' to black.
## arguments:
## screen: list of lists; the screen to be cleared.
def clearScreen(screen):
    for i in range(0, len(screen) ):
        for j in range(0, len(screen[i]) ):
            screen[i][j] = [0,0,0]

            
# writePpmFile(screen, fileName, #<1>#comment)
# Writes the data from a screen to a ppm file.
## arguments:
## screen: list of lists; the screen to be written.
## fileName: string; fileName of the screen.
def writePpmFile(screen, fileName):
    file = open('{}'.format(fileName), 'w')
    # creates new file with fileName and open it to edit.
    
    file.write('P3\n')
    # This line specifies the file format for the ppm image file.
    # for more info on ppm file formats:
    # https://en.wikipedia.org/wiki/Netpbm_format#File_format_description

    width = len(screen)
    height = len(screen[0])
    file.write('{} {} 255\n'.format( width, height ) )
    # This line specifies the width, height, and color depth of the ppm image file.
    
    #<1># If ever you wish to include a comment with the file:
    # file.write('#{}\n'.format(comment))

    for i in range(0, height):
        for j in range(0, width):
            # width is nested in height because ppm are listed row by row.
            # Rows correspond to screen height.
            file.write('{} {} {}  '.format( screen[j][i][0], screen[j][i][1], screen[j][i][2] ) )
            # 2 spaces after a pixel to make each pixel stand out when viewed as text.
            
    file.close()


# saveExtension(screen, fileName)
# Saves screen as file with filename fileName.
## arguments:
## screen: list of lists; the screen to be written.
## fileName: string; includes the desired extension.
def saveExtension(screen, fileName):
    ppmName = fileName[:fileName.find('.')] + '.ppm'
    writePpmFile(screen, ppmName)
    # Create a ppm file from screen
    p = Popen(['convert', ppmName, fileName ], stdin=PIPE, stdout = PIPE)
    p.communicate()
    # Convert the ppm file to fileName which includes the desired extenstion.
    remove(ppmName)
    # Remove the ppm file.
    # Don't think it's necessary, but I might be ignorant.


# display(screen)
# Saves screen as an image file, displays file, removes file
## arguments:
## screen: list of lists; the screen to be displayed.
def display(screen):
    ppmName = 'pic.ppm'
    writePpmFile(screen, ppmName)
    # Create a ppm file from screen
    p = Popen(['display', ppmName], stdin=PIPE, stdout = PIPE)
    p.communicate()
    # Display the file.
    remove(ppmName)
    # Remove the file.
