#!~/usr/bin/env python3

import screen
import matrix
import math

def plot(screen, x, y, color):
    width = len(screen)
    height = len(screen[0])
    if(x >= width or x < 0 or
       y >= height or y < 0):
        print('Out of bounds! ({}, {}) not drawn.'.format(x, y))
        return False
        print('Out of bounds! Wrapping ({}, {}).'.format(x, y)) #Option to draw by modulo.
        x = x%width
        y = y%height
    screen[x][y] = color

# Bresenham's line algorithm.
def drawLine(screen, a, b, color):
    # Octants:
    # \3|2/
    # 4\|/1
    # -----
    # 5/|\8
    # /6|7\

    # Reminder that the origin is in the top left, and y increments top to bottom
    # Any work with y-values should have this in mind.
    
    # Swap points a and b if b is to the left of a.
    # Only have to deal with octants 1, 2, 8, and 7.
    if(b[0] < a[0]):
        b[0] = b[0] + a[0]
        a[0] = b[0] - a[0]
        b[0] = b[0] - a[0]
        
        b[1] = b[1] + a[1]
        a[1] = b[1] - a[1]
        b[1] = b[1] - a[1]

    x = a[0]
    y = a[1]

    # y = mx + b
    # 0 = mx - y + b
    # m = dy / dx
    # multiply both sides by dx.
    # 0 = (dy * x) - (dx * y) + (dx * b)
    
    # 0 = Ax + By + C
    # A =  dy
    # B = -dx
    # C =  dx * b
    
    B = -1 * (b[0] - a[0])
    # (B = -dx) point b is always to the right of a.

    # Midpoint calculations:
    # f(X0 + i, Y0 + j) = A(X0+i) + B(Y0+j) + C
    # = AX0 + Ai + BY0 + Bj + C
    #   AX0 + BY0 + C = 0
    # = Ai + Bj
    # i is 0.5 or 1, j is 1 or 0.5, representative of midpoint coordinates.
    # Multiply by 2 to avoid division. Won't affect accuracy because we only check the sign.
    
    if b[1] <= a[1]:   # Octants 1, 2 : [0, pi/2)
        A = a[1] - b[1]
        if abs(A) >= abs(B):
            # Octant 2
            # [pi/4, pi/2)
            # [?][?]
            # [X][_]
            # X=current pixel, ?=candidates.
            # f(X+0.5, Y+1)
            # f(X+1, Y+2)
            # A + 2B
            d = A + (2 * B)
            while(y >= b[1]):
                plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + (2*A)
                y = y - 1
                d = d + (2*B)
        else:
            # Octant 1
            # [0, pi/4)
            # [_][?]
            # [X][?]
            # f(X+1, Y+0.5)
            # f(X+2, Y+1)
            # 2A + B
            d = (2 * A) + B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d > 0):
                    y = y - 1
                    d = d + (2*B)
                x = x + 1
                d = d + (2*A)
    else:   # Octants 7, 8 : (0, -pi/2]
        A = a[1] - b[1]
        if abs(A) >= abs(B):
            # Octant 7
            # [-pi/2, -pi/4]
            # [X][_]
            # [?][?]
            # f(X+0.5, Y-1)
            # f(X+1, Y-2)
            # d = A - 2B
            d = A - (2 * B)
            while(y <= b[1]):
                plot(screen, x, y, color)
                if(d > 0):
                    x = x + 1
                    d = d + (2*A) 
                y = y + 1
                d = d - (2*B)
        else:
            # Octant 8
            # (-pi/4, 0)
            # [X][?]
            # [_][?]
            # f(X+1, Y-0.5)
            # f(X+2, Y-1)
            # d = 2A - B
            d = (2 * A) - B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d < 0):
                    y = y + 1
                    d = d - (2*B)
                x = x + 1
                d = d + (2*A)

def circle(edgeMatrix, x, y, z, r, step):
    if step < (1 / (r * r)):
        step = (1 / (r * r))
    t = 0
    while t < 1:
        matrix.addEdge(edgeMatrix,
                       
                       [r*math.cos( 2*math.pi*t ) + x,
                        r*math.sin( 2*math.pi*t ) + y,
                        z,
                        1],
                       
                       [r * math.cos( 2*math.pi*(t+step) ) + x,
                        r * math.sin( 2*math.pi*(t+step) ) + y,
                        z,
                        1]
                       
                       )
        t = t + step
        

def curve(edgeMatrix, x0, y0, x1, y1, x2, y2, x3, y3, step, curveType):
    if step == 0:
        step = 1 / 100.0
    coefX = matrix.generateCoef( x0, x1, x2, x3, curveType )
    coefY = matrix.generateCoef( y0, y1, y2, y3, curveType )
    newX = x0
    newY = y0
    t = 0
    while t < 1:
        t = t + step
        oldX = newX
        oldY = newY
        newX = (coefX[0][0] * math.pow(t, 3)) + (coefX[1][0] * math.pow(t, 2)) + (coefX[2][0] * t) + coefX[3][0]
        newY = (coefY[0][0] * math.pow(t, 3)) + (coefY[1][0] * math.pow(t, 2)) + (coefY[2][0] * t) + coefY[3][0]
        
        matrix.addEdge( edgeMatrix, [oldX, oldY, 0], [newX, newY, 0] )

        
def box(edgeMatrix, x, y, z, w, h, d):
    #front
    matrix.addPolygon( edgeMatrix, [x, y, z], [x, y+h, z], [x+w, y, z] )
    matrix.addPolygon( edgeMatrix, [x, y+h, z], [x+w, y+h, z], [x+w, y, z] )
    #top
    matrix.addPolygon( edgeMatrix, [x, y, z-d], [x, y, z], [x+w, y, z-d] )
    matrix.addPolygon( edgeMatrix, [x, y, z], [x+w, y, z], [x+w, y, z-d] )
    #bottom
    matrix.addPolygon( edgeMatrix, [x, y+h, z], [x, y+h, z-d], [x+w, y+h, z] )
    matrix.addPolygon( edgeMatrix, [x, y+h, z-d], [x+w, y+h, z-d], [x+w, y+h, z] )
    #left
    matrix.addPolygon( edgeMatrix, [x, y, z-d], [x, y+h, z-d], [x, y, z] )
    matrix.addPolygon( edgeMatrix, [x, y+h, z-d], [x, y+h, z], [x, y, z] )
    #right
    matrix.addPolygon( edgeMatrix, [x+w, y, z], [x+w, y+h, z], [x+w, y, z-d] )
    matrix.addPolygon( edgeMatrix, [x+w, y+h, z], [x+w, y+h, z-d], [x+w, y, z-d] )
    #back
    matrix.addPolygon( edgeMatrix, [x+w, y, z-d], [x+w, y+h, z-d], [x, y, z-d] )
    matrix.addPolygon( edgeMatrix, [x+w, y+h, z-d], [x, y+h, z-d], [x, y, z-d] )

    
def sphere(edgeMatrix, cx, cy, cz, r, step):
    if step == 0:
        step = .025
    phi = 0
    while phi < (2 * math.pi):
        rotate = [ [1, 0, 0, 0],
                   [0, math.cos(phi), math.sin(phi), 0],
                   [0, math.sin(phi), -1 * math.cos(phi) ,0],
                   [0, 0, 0, 1] ]
        theta = 0
        while theta < math.pi:
            semicircle = [ [r * math.cos(theta)],
                           [r * math.sin(theta)],
                           [0],
                           [1] ]
            matrix.matrixMultiplication( rotate, semicircle )
            matrix.addEdge( edgeMatrix,
                            [semicircle[0][0]+cx, semicircle[1][0]+cy, semicircle[2][0]+cz],
                            [semicircle[0][0]+cx, semicircle[1][0]+cy, semicircle[2][0]+cz] )
            theta = theta + (math.pi / 30)
        phi = phi + (step * 2 * math.pi)

        
def torus(edgeMatrix, cx, cy, cz, r, R, step):
    if step == 0:
        step = .025
    phi = 0
    while phi < (2 * math.pi):
        rotate = [ [math.cos(phi), 0, math.sin(phi), 0],
                   [0, 1, 0, 0],
                   [ -1 * math.sin(phi), 0, math.cos(phi) ,0],
                   [0, 0, 0, 1] ]
        theta = 0
        while theta < (2 * math.pi):
            circle = [ [ (r * math.cos(theta) ) + R],
                       [r * math.sin(theta)],
                       [0],
                       [1] ]
            matrix.matrixMultiplication( rotate, circle )
            matrix.addEdge( edgeMatrix,
                            [circle[0][0]+cx, circle[1][0]+cy, circle[2][0]+cz],
                            [circle[0][0]+cx, circle[1][0]+cy, circle[2][0]+cz] )
            theta = theta + (2 * math.pi / 30)
        phi = phi + (step * 2 * math.pi)
