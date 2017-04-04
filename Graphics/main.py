#!~/usr/bin/env python3

# to do list:
# parser issues
# comment matrix
# possible issues with transform
# comment new screen

import screen
import draw
import matrix
import parser

green = [0, 255, 0]
edgeMatrix = [ [],[],[],[] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    #screenOne = screen.createScreen(500,500)
    #draw.circle(edgeMatrix, 250, 250, 0, 50, .00001)
    #matrix.drawEdges(screenOne, edgeMatrix, green)
    
    # screen.display(screenOne)
    screenOne = screen.createScreen(500, 500)
    matrix.addPolygon( edgeMatrix, [0,0,0], [0,100,0], [100, 100, 0] )
    matrix.addPolygon( edgeMatrix, [100,0,300], [100,100,300], [200, 100, 300] )
    for i in range(0, 300):
        matrix.addPoint( edgeMatrix, [.33 * i, 0, i ] )
        matrix.addPoint( edgeMatrix, [.33 * i, 0, i ] )
        matrix.addPoint( edgeMatrix, [.33 * i, 0, i ] )
    #draw.box(edgeMatrix, 100, 100, 100, 100, 200, 300)
    matrix.printMatrix(edgeMatrix)
    matrix.matrixMultiplication(matrix.createRotateMatrix('x', 30), edgeMatrix)
    matrix.matrixMultiplication(matrix.createRotateMatrix('y', 15), edgeMatrix)
    matrix.drawPolygons(screenOne, edgeMatrix, green)
    matrix.printMatrix(edgeMatrix)
    #matrix.printMatrix(edgeMatrix)
    screen.display(screenOne)
    # screen.writePpmFile(screenOne, 'pic.ppm')

main()

    
# def theyDontChange(x):
#     x = x + 2
# def theyDontChange(x):
#     x[0] = 999
# x = [1, 2, 3]
# theyDontChange(x)
# print(x)
