#!~/usr/bin/env python3

# to do list:
# triangle
# relative
# splines
# [ ] draw.py
# [ ] matrix.py
# [ ] parser.py
# [ ] 

import screen
import draw
import matrix
import parser

green = [0, 255, 0]
edgeMatrix = [ [], [], [], [] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    screenOne = screen.createScreen(500, 500)
    # drawLine test.
    # for i in range (0, 500, 100):
    #     matrix.addEdge(edgeMatrix, [249, 249, 0], [499, i, 0])
    #     matrix.addEdge(edgeMatrix, [249, 249, 0], [i, 0, 0])
    #     matrix.addEdge(edgeMatrix, [249, 249, 0], [0, i + 100, 0])
    #     matrix.addEdge(edgeMatrix, [249, 249, 0], [i + 100, 499, i])
    # matrix.addEdge(edgeMatrix, [0, 0, 0], [499, 499, 0])
    # matrix.addEdge(edgeMatrix, [0, 499, 0], [499, 0, 0])
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
main()
