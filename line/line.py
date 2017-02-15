#!/usr/bin/env

import random

width = 500
height = 500
#width = int(input("width of image: "))
#height = int(input("height of image: "))
colorDepth = 255
matrix = []
color = [0, 255, 0]

for i in range(width):
    matrix.append([])
    for j in range(height):
        matrix[i].append([0, 0, 0])

def writePpmFile(matrix):
    file = open("line.ppm", "w")
    file.write("P3\n")
    file.write("{} {} {}\n".format(width, height, colorDepth))
    for i in range(height):
        for j in range(width):
            file.write("{} {} {}\n".format(matrix[j][i][0], matrix[j][i][1], matrix[j][i][2]))

def plot(matrix, x, y, color):
    matrix[x][y][0] = color[0]
    matrix[x][y][2] = color[2]
    matrix[x][y][1] = color[1]

def drawLine(matrix, a, b, color):
    #Swap points a and b if a is to the right of b.
    if(b[0] < a[0]):
        b[0] = b[0] + a[0]
        b[1] = b[1] + a[1]
        a[0] = b[0] - a[0]
        a[1] = b[1] - a[1]
        b[0] = b[0] - a[0]
        b[1] = b[1] - a[1]
    B = -1 * (b[0] - a[0])

    if(a[1] >= b[1]):
        #Octant I, II
        A = a[1] - b[1]
        if(A >= (-1 * B)):

        else:

    else:
        #Octant VII, VIII
    #Octant I
    A = a[1] - b[1]

    d = (2 * A) + B
    x = a[0]
    y = a[1]
    while(x < b[0]):
        plot(matrix, x, y, color)
        if(d > 0):
            y = y - 1
            d = d + B
        x = x + 1
        d = d + A
    plot(matrix, b[0], b[1], color)

    #Octant II
    A = a[1]- b[1]

    d = A + (2 * B)
    x = a[0]
    y = a[1]
    while(y > b[1]):
        plot(matrix, x, y, color)
        if(d < 0):
            x = x + 1
            d = d + A
        y = y - 1
        d = d + B
    plot(matrix, b[0], b[1], color)

    #Octant VII
    A = b[1] - a[1]

    d = A - (2 * B)
    x = a[0]
    y = a[1]
    while(y < b[1]):
        plot(matrix, x, y color)
        if(d > 0):
            x = x + 1
            d = d + A
        y = y - 1
        d = d - B
    plot(matrix, b[0], b[1], color)

    #Octant VIII
    A =  b[1] - a[1]

    d = (2 * A) - B
    x = a[0]
    y = a[1]
    while(x < b[0]):
        plot(matrix, x, y, color)
        if(d < 0):
            y = y - a
            d = d - B
        x = x + 1
        d = d + A

def drawRandLine():
    randColor = [random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)]
    drawLine(matrix, [0, len(matrix[0]) - 1], [len(matrix) - 1, random.randrange(0, len(matrix[0]) - 1)], randColor)

#drawLine(matrix, [0,499], [400,200], color)
drawLine(matrix, [0, len(matrix[0]) - 1], [len(matrix) - 1, random.randrange(0, len(matrix[0]) - 1)], color)
for i in range(999):
    drawRandLine()
#for i in range(width):
#   print(matrix[i])
writePpmFile(matrix)
