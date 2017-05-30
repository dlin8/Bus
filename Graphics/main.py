#!~/usr/bin/env python3

# to do list:
# triangle
# relative
# splines
# [] screen.py
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
    draw.sphere(edgeMatrix, 250, 250, 0, 200, 0)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    
    #screen.saveExtension(screenOne, 'pic.png')
    
    # For windows w/o imagemagick properly installed
    # screen.writePpmFile(screenOne, 'pic.ppm')
    
main()
