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
    draw.plot(screenOne, 249, 249, green)
    draw.plot(screenOne, 500, 500, green)
    #screen.saveExtension(screenOne, 'pic.png')
    screen.display(screenOne)
    # For windows w/o imagemagick properly installed
    # screen.writePpmFile(screenOne, 'pic.ppm')

main()
