#!~/usr/bin/env python3

import screen
import line
import matrix

edgeMatrix = []
masterTransformMatrix = []

def main():
    # line.drawLine(screenOne, [1,0], [499,499], color)
    screenOne = screen.createScreen(500, 500)
    color = [0, 255, 255]
    edgeMatrix = []
    for i in range(0,4):
        edgeMatrix.append([])
    matrix.addEdge(edgeMatrix, [100.0, 100.23434,0], [400,200,0])
    matrix.addEdge(edgeMatrix, [400,200,0], [400,400,0])
    matrix.addEdge(edgeMatrix, [400,400,0], [200,400,0])
    matrix.addEdge(edgeMatrix, [200,400,0], [200,200,0])
    matrix.scalarMultiplication(.56, edgeMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, color)
    screen.writePpmFile(screenOne, 255, 'test')
main()
