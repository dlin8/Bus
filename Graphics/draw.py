#!~/usr/bin/env python3

import screen

# plot(screen, x, y, color)
# Plots a point on a screen.
## parameters:
## screen: list of lists; screen to plot point onto.
## x: int; x-coordinate of point.
## y: int; y-coordinate of point.
## color: list [R,G,B]; color of point.
def plot(screen, x, y, color):
    width = len(screen)
    height = len(screen[0])
    if(x >= width or y >= height):
        print('Out of bounds!')
        return False
    screen[x][y] = color

## Produces weird lines with some coordinates, needs revision

# drawLine(screen, a, b, color)
# Draws a line on a screen
## paramaters:
## screen: list of lists; screen to plot point onto.
## a: list [x-coordinate, y-coordinate]; coordinates of one endpoint of line.
## b: list [x-coordinate, y-coordinate]; coordinates of other endpoint of line.
## color: list [R,G,B]; color of line
def drawLine(screen, a, b, color):
    # Picture of Octants:
    # \3##|##2/
    # #\##|##/#
    # ##\#|#/##
    # 4##\|/##1
    # ---------
    # 5##/|\##8
    # ##/#|#\##
    # #/##|##\#
    # /6##|##7\

    # Reminder that the origin is in the top left, and y increments top to bottom.
    # Any work with y-values should have this in mind.
    
    # Swap points a and b if a is to the right of b.
    # Only have to deal with octants 1, 2, 7, and 8 as a result where we start from the left and draw to the right.
    if(b[0] < a[0]):
        # Swapping values without a third variable
        # Possibility for overflow errors
        b[0] = b[0] + a[0]
        a[0] = b[0] - a[0]
        b[0] = b[0] - a[0]
        
        b[1] = b[1] + a[1]
        a[1] = b[1] - a[1]
        b[1] = b[1] - a[1]

    x = a[0]
    y = a[1]
    # Initialize x and y coordinates of current pixel to be drawn

    # y = mx + b
    ## m = dy / dx
    # 0 = mx - y + b
    # multiply both sides by dx
    # 0 = (dy * x) - (dx * y) + (dx * b)
    # 0 = Ax + By + C
    # A =  dy
    # B = -dx
    # C =  dx * b
    
    B = -1 * (b[0] - a[0])
    # (B = -dx) point b is always to the right of a because we swapped if not.
    # b[0] >= a[0]
    # B = -1 * (b[0] - a[0])

    # Algorithm follows this general structure:
    #####################PASS#########################
    
    if a[1] <= b[1]:
        # Octants 1 or 2 or horizontal line
        # If point a is HIGHER than point b, see reminder text.
        # Also track if a and b are of same height for trivial case.
        
        A = b[1] - a[1]
        # A = dy
        
        if A >= (-1 * B):
            # If y increases faster than x, or increase at the same rate:
            # Line resides in octant 2 or between octants 1 and 2
            
            # ##2/
            # ##/
            # #/
            # /
            
            d = A + (2 * B)
            # Initial value of midpoint.
            # A positive value indicates that A > 2B
            # Therefore, the x-coordinate of the midpoint, the only coordinate we really care about, is higher than it should be.
            # Therefore, if d is > 0, do not increment x.
            # Otherwise, if d is < 0, do increment x.
            
            while(y < b[1]):
                plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + A
                y = y - 1
                d = d + B
        else:
            # Otherwise, the line resides in octant 1
            
            d = (2 * A) + B
            while(x < b[0]):
                plot(screen, x, y, color)
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
                plot(screen, x, y, color)
                if(d < 0):
                    y = y + 1
                    d = d - B
                x = x + 1
                d = d + A
        else:
            #Octant VII
            d = A - (2 * B)
            while(y < b[1]):
                plot(screen, x, y, color)
                if(d > 0):
                    x = x + 1
                    d = d + A
                y = y + 1
                d = d - B
    plot(screen, b[0], b[1], color)
