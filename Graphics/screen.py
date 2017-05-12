#!~/usr/bin/env python3

from subprocess import Popen, PIPE
from os import remove

# Origin is top left back.
# x increases to the right,
# y increases to the bottom,
# z increases to the front.

def createScreen(width, height):
    screen = []
    for i in range(0, width):
        screen.append([])
        for j in range(0, height):
            screen[i].append([0,0,0])
    return screen

def clearScreen(screen):
    for i in range(0, len(screen)):
        for j in range(0, len(screen[i])):
            screen[i][j] = [0,0,0]

def writePpmFile(screen, fileName):
    file = open('{}'.format(fileName), 'w')
    file.write('P3\n')    # https://en.wikipedia.org/wiki/Netpbm_format#File_format_description
    width = len(screen)
    height = len(screen[0])
    file.write('{} {} 255\n'.format(width, height))
    # file.write('#{}\n'.format(comment))
    for i in range(0, height):
        for j in range(0, width):        # width is nested in height because ppm are written by rows.
            file.write('{} {} {}  '.format(screen[j][i][0], screen[j][i][1], screen[j][i][2])) #RGB
    file.close()

def saveExtension(screen, fileName):
    ppmName = fileName[:fileName.find('.')] + '.ppm'
    writePpmFile(screen, ppmName)
    p = Popen(['convert', ppmName, fileName ], stdin=PIPE, stdout = PIPE)
    p.communicate()
    remove(ppmName)

def display(screen):
    ppmName = 'pic.ppm'
    writePpmFile(screen, ppmName)
    p = Popen(['display', ppmName], stdin=PIPE, stdout = PIPE)
    p.communicate()
    remove(ppmName)
