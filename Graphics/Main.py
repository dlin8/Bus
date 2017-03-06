#!~/usr/bin/env python3

import Screen
import Line
import Matrix
import Transform

edgeMatrix = []
masterTransformMatrix = []

def main():
    # Line.drawLine(screenOne, [1,0], [499,499], color)
    screenOne = Screen.createScreen(500, 500)
    color = [0, 255, 255]
    edgeMatrix = []
    # for i in range(0,4):
    #     edgeMatrix.append([])
    # Matrix.addEdge(edgeMatrix, [100.0, 100.23434,0], [400,200,0])
    # Matrix.addEdge(edgeMatrix, [400,200,0], [400,400,0])
    # Matrix.addEdge(edgeMatrix, [400,400,0], [200,400,0])
    # Matrix.addEdge(edgeMatrix, [200,400,0], [200,200,0])
    # Matrix.scalarMultiplication(.56, edgeMatrix)
    # Matrix.drawEdges(screenOne, edgeMatrix, color)
    #Screen.writePpmFile(screenOne, 'test', 'main')
    # The master matrix is the multiplicand to maintain the proper order of transformations.
    # Matrix multiplication is not always commutative.
#    masterTransformMatrix = matrixMultiplication(translateMatrix, masterTransformMatrix)
    Transform.createTranslateMatrix(1,2,3)
    Transform.createScaleMatrix(2,2,2)
    Transform.createRotateMatrix('x',30)
    Transform.createRotateMatrix('y',60)
    Transform.createRotateMatrix('z',90)
    
main()
