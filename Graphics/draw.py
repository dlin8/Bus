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
        # Swapping values without a third variable.
        # Possibility for overflow errors.
        b[0] = b[0] + a[0]
        a[0] = b[0] - a[0]
        b[0] = b[0] - a[0]
        
        b[1] = b[1] + a[1]
        a[1] = b[1] - a[1]
        b[1] = b[1] - a[1]

    x = a[0]
    y = a[1]
    # Initialize x and y coordinates of current pixel to be drawn.

    # y = mx + b
    ## m = dy / dx
    # 0 = mx - y + b
    # multiply both sides by dx.
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
    # One coordinate will always be incremented.
    # The other coordinate will either be or not be incremented.
    # This depends on the midpoint of these two possible spaces for the new pixel.
    # The midpoint is substituted into the standard form of the equation representing the line.
    # Depending on whether this value is positive or negative,
    # We can determine that most of the line resides in one or the other space.
    # And we can then decide to increment or not increment to have the next pixel be in that space.

    # Midpoint calculations:
    # f(X0 + i, Y0 + j) = A(X0+i) + B(Y0+j) + C
    # = AX0 + Ai + BY0 + Bj + C
    #                               AX0 + BY0 + C = 0
    # = Ai + Bj
    # i is 0.5 or 1, j is 1 or 0.5, representative of midpoint coordinates.
    # Multiply by 2 to avoid division.
    # Increment A and B twice as well to stay consistent with this scaled value of midpoint.
    
    if a[1] >= b[1]:
        # Octants 1, 2, horizontal line, or perfect diagonal SW - NE.
        # [0, pi/2)
        # If point a is LOWER than point b, see reminder text.
        # Also track if a and b are of same height for trivial case. (Hoz. line)
        
        A = a[1] - b[1]
        # A = dy
        
        if abs(A) >= abs(B):
            # If y increases faster than x, or increase at the same rate:
            # Line resides in octant 2 or between octants 1 and 2 for 45 deg line.
            # [pi/4, pi/2)
            
            # ##2/
            # ##/
            # #/
            # /
            # picture of an octant 2 line.

            # [?][?]
            # [X][_]
            # how next pixel is decided.

            # f(X+0.5, Y+0.1)
            # f(X+1, Y+2)
            # A + 2B
            
            d = A + (2 * B)
            # B is negative!
            # Initial value of midpoint.
            # A positive value indicates that A > 2B.
            # Therefore, the x-coordinate of the midpoint, the conditional coordinate is too high.
            # Therefore, if d is > 0, do not increment x.
            # Otherwise, if d is < 0, do increment x.
            # if d = 0 dont increment, stays consistent with other 3 quadrants.
            
            while(y >= b[1]):
                plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + (2*A)
                y = y - 1
                d = d + (2*B)
        else:
            # Otherwise, the line resides in octant 1.
            # [0, pi/4)

            # ####/
            # #___#
            # /###1
            # picture of octant 1 line

            # [_][?]
            # [X][?]
            # how next pixel is decided.

            # f(X+1, Y+0.5)
            # f(X+2, Y+1)
            # 2A + B

            # Here the conditional coordinate is Y. Reminder text.
            # B is the only negative term.
            # d > 0 means that Y is too low.
            d = (2 * A) + B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d > 0):
                    y = y - 1 #REMINDER TEXT
                    d = d + (2*B)
                x = x + 1
                d = d + (2*A)
    else:
        # Otherwise the point a is HIGHER than b.
        # Octant VII, VIII, edge cases.
        # (0, -pi/2]
        
        A = a[1] - b[1]
        #
        if abs(A) >= abs(B):
            # Y changes faster or equal to X, Octant 7 or perfect diagonal NW-SE.
            # [-pi/4, -pi/2]

            # [X][_]
            # [?][?]

            # f(X+0.5, Y-1)
            # f(X+1, Y-2)
            # d = A - 2B

            d = A - (2 * B)
            while(y <= b[1]):
                plot(screen, x, y, color)
                if(d > 0):
                    # X is not high enough
                    x = x + 1
                    d = d + (2*A) 
                y = y + 1
                # Reminder text.
                d = d - (2*B)
                # Decrement because y is DECREASING, b term must decrease as well.
                # Confusing because b is actually negative, so d is actually increasing.
            
        else:
            # Octant 8.
            # (0, -pi/4)

            # [X][?]
            # [_][?]

            # f(X+1, Y-0.5)
            # f(X+2, Y-1)
            # d = 2A - B
            
            d = (2 * A) - B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d < 0):
                    # Y is too high.
                    y = y + 1
                    d = d - (2*B)
                x = x + 1
                d = d + (2*A)
            
