#!~/usr/bin/env python3

# to do list:
# triangle
# relative
# splines
# Clean
# [X] screen.py
# [ ] draw.py
# [ ] matrix.py
# [ ] parser.py
# [ ] 


import screen
import draw
import matrix
import parser

green = [0, 255, 0]
edgeMatrix = [ [],[],[],[] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    screenOne = screen.createScreen(500, 500)

    draw.box(edgeMatrix, 250, 250, 0, 100, 100, 100)
    
    matrix.matrixMultiplication(matrix.createRotateMatrix('z', 30), edgeMatrix)
    draw.box(edgeMatrix, 250, 250, 0, 100, 100, 100)
    #matrix.matrixMultiplication(matrix.createRotateMatrix('x', -45), edgeMatrix)
    matrix.matrixMultiplication(matrix.createRotateMatrix('y', -45), edgeMatrix)
    
    
    matrix.drawPolygons(screenOne, edgeMatrix, green)
    #screen.saveExtension(screenOne, 'pic.png')
    screen.display(screenOne)
    # For windows w/o imagemagick properly installed
    # screen.writePpmFile(screenOne, 'pic.ppm')

main()
