#!~/usr/bin/env python3

# to do list:
# get display working
# parser issues
# fix line

import screen
import draw
# import line
# import matrix
# import transform
# import parser

# edgeMatrix = [ [],[],[],[] ]
# tempScreen = Screen.createScreen(4,4)
# transformMatrix = Matrix.getIdentityMatrix(tempScreen)[:]
    
def main():
    green = [0, 255, 0]
    screenOne = screen.createScreen(500, 500)
    draw.drawLine(screenOne, [1,0], [499,499], green)
#    draw.drawLine(screenOne, [0,0], [63,63], green)
    screen.writePpmFile(screenOne, 'pic', 'comment')
main()
