#!~/usr/bin/env python3

def createScreen(width, height):
    screen = []
    for i in range(0, width):
        screen.append([])
        for j in range(0, height):
            screen[i].append([0,0,0])
    return screen

def plot(screen, x, y, color):
    width = len(screen)
    height = len(screen[0])
    if(x > width or y > height):
        print('Out of bounds!')
        return false
    screen[x][y][0] = color[0]
    screen[x][y][2] = color[2]
    screen[x][y][1] = color[1]

def writePpmFile(screen, colorDepth, fileName):
    width = len(screen)
    height = len(screen[0])
    file = open('{}.ppm'.format(fileName), 'w')
    file.write('P3\n')
    file.write('{} {} {}\n'.format( width, height, colorDepth ) )
    for i in range(0, height):
        for j in range(0, width):
            file.write('{} {} {}  '.format( screen[j][i][0], screen[j][i][1], screen[j][i][2] ) )
        file.write('\n')
    file.close()
