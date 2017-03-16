#!~/usr/bin/env python3

# to do list:
# parser issues
# comment matrix
# possible issues with transform
# comment new screen

import screen
import draw
import matrix
# import parser

green = [0, 255, 0]
edgeMatrix = [ [],[],[],[] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    screenOne = screen.createScreen(500,500)
    matrix.addEdge(edgeMatrix, [0,0,0], [100,100,30])
    matrix.addEdge(edgeMatrix, [0,0,0], [100,100,60])
    matrix.addEdge(edgeMatrix, [0,0,0], [100,100,90])
    matrix.addEdge(edgeMatrix, [0,0,0], [100,100,120])

    matrix.matrixMultiplication(transformMatrix, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    screen.clearScreen(screenOne)
    
    matrix.matrixMultiplication(matrix.createTranslateMatrix(20,20,-10) ,transformMatrix)

    matrix.matrixMultiplication(transformMatrix, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    screen.clearScreen(screenOne)
    
    matrix.matrixMultiplication(matrix.createScaleMatrix(2,2,2), transformMatrix)

    matrix.matrixMultiplication(transformMatrix, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    screen.clearScreen(screenOne)
    
    matrix.matrixMultiplication(matrix.createRotateMatrix('y', 30) ,transformMatrix)

    matrix.matrixMultiplication(transformMatrix, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    screen.clearScreen(screenOne)
    
    matrix.matrixMultiplication(matrix.createRotateMatrix('z', 30) ,transformMatrix)

    matrix.matrixMultiplication(transformMatrix, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    
main()

    
# def theyDontChange(x):
#     x = x + 2
# def theyDontChange(x):
#     x[0] = 999
# x = [1, 2, 3]
# theyDontChange(x)
# print(x)
