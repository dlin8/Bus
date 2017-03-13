#!~/usr/bin/env python3

# to do list:
# get display working
# parser issues

import screen
import imageMagick
import draw
# import matrix
# import transform
# import parser

# edgeMatrix = [ [],[],[],[] ]
# tempScreen = Screen.createScreen(4,4)
# transformMatrix = Matrix.getIdentityMatrix(tempScreen)[:]
    
def main():
    green = [0, 255, 0]
    screenOne = screen.createScreen(500, 500)
    # Line tests
    ## Diagonals, vertical, horizontal
    draw.drawLine(screenOne, [0,0], [499,499], green)
    draw.drawLine(screenOne, [0,499], [499,0], green)
    draw.drawLine(screenOne, [0,40], [499,40], green)
    draw.drawLine(screenOne, [40,0], [40,499], green)

    ## Quadrants
    draw.drawLine(screenOne, [0,400], [499,200], green)
    draw.drawLine(screenOne, [0,200], [499,400], green)
    draw.drawLine(screenOne, [0,450], [40,0], green)
    draw.drawLine(screenOne, [0,50], [40,499], green)

    ## Many lines
    for i in range(0,500,15):
        draw.drawLine(screenOne, [250,250], [499,i], green)
    for i in range(0,500,10):
        draw.drawLine(screenOne, [250,250], [0,i], green)
    for i in range(0,500,25):
        draw.drawLine(screenOne, [250,250], [i,0], green)
    for i in range(0,500,15):
        draw.drawLine(screenOne, [250,250], [i,499] , green)
    screen.writePpmFile(screenOne, 'lineTest')
    imageMagick.display(screenOne)
main()
