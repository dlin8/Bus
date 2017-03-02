#!/usr/bin/env python3

def drawLine(matrix, a, b, color):
    #Swap points a and b if a is to the right of b.
    if(b[0] < a[0]):
        b[0] = b[0] + a[0]
        b[1] = b[1] + a[1]
        a[0] = b[0] - a[0]
        a[1] = b[1] - a[1]
        b[0] = b[0] - a[0]
        b[1] = b[1] - a[1]
        
    #Plot point b
    plot(matrix, b[0], b[1], color)

    x = a[0]
    y = a[1]
            
    B = -1 * (b[0] - a[0])
    
    if a[1] >= b[1]:
        #Octant I, II
        A = a[1] - b[1]
        if A >= (-1 * B):
            #Octant II
            d = A + (2 * B)
            while(y > b[1]):
                plot(matrix, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + A
                y = y - 1
                d = d + B
        else:
            #Octant I
            d = (2 * A) + B
            while(x < b[0]):
                plot(matrix, x, y, color)
                if(d > 0):
                    y = y - 1
                    d = d + B
                x = x + 1
                d = d + A
    else:
        #Octant VII, VIII
        A = a[1] - b[1]
        if A >= B:
            #Octant VIII
            d = (2 * A) - B
            while(x < b[0]):
                plot(matrix, x, y, color)
                if(d < 0):
                    y = y + 1
                    d = d - B
                x = x + 1
                d = d + A
        else:
            #Octant VII
            d = A - (2 * B)
            while(y < b[1]):
                plot(matrix, x, y, color)
                if(d > 0):
                    x = x + 1
                    d = d + A
                y = y + 1
                d = d - B
    plot(matrix, b[0], b[1], color)

def randColor():
    randColor = [random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)]
    return randColor
def drawRandLine():
    randColor = [random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)]
    x = [random.randrange(0, len(matrix)), random.randrange(0, len(matrix[0]))]
    y = [random.randrange(0, len(matrix)), random.randrange(0, len(matrix[0]))]
    drawLine(matrix, x, y, randColor)

#for i in range(20):
#    drawRandLine()

#for i in range(width):
#   print(matrix[i])

drawLine(matrix, [0,0], [499,499], randColor())
drawLine(matrix, [0,499], [499,0], randColor())
drawLine(matrix, [249,0], [249,499], randColor())
drawLine(matrix, [0,249], [499,249], randColor())

drawLine(matrix, [249,249], [499,124], randColor())
drawLine(matrix, [249,249], [374, 0], randColor())
drawLine(matrix, [249,249], [124,0], randColor())
drawLine(matrix, [249,249], [0,124], randColor())
drawLine(matrix, [249,249], [0,374], randColor())
drawLine(matrix, [249,249], [124,499], randColor())
drawLine(matrix, [249,249], [374,499], randColor())
drawLine(matrix, [249,249], [499,374], randColor())

writePpmFile(matrix)
