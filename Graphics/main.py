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
    screenOne = screen.createScreen(6, 3)
    draw.plot(screenOne, 0, 0, [255, 255, 255])
    draw.plot(screenOne, 5, 2, green)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    matrix.printMatrix(screenOne)
    A = matrix.newMatrix(6,4)
    A[3][5] = 'w0w0w0w00w0w'
    matrix.printMatrix(A)
    #screen.display(screenOne)
main()
