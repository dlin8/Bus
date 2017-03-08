#!~/usr/bin/env python3

import Screen
import Line
import Matrix
import Transform
import Parser

edgeMatrix = [ [],[],[],[] ]
tempScreen = Screen.createScreen(4,4)
transformMatrix = Matrix.getIdentityMatrix(tempScreen)

def main():
    green = [0, 255, 0]
    # Line.drawLine(screenOne, [1,0], [499,499], color)
    screenOne = Screen.createScreen(500,500)
    Parser.parseFile('script', screenOne, green, edgeMatrix, transformMatrix)
    Screen.writePpmFile(screenOne, 'test', 'test')
    
main()
