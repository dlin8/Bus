#!~/usr/bin/env python3

# to do list:
# parser issues
# comment matrix
# possible issues with transform
# comment new screen

import screen
import draw
import matrix
import parser

green = [0, 255, 0]
edgeMatrix = [ [],[],[],[] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    screenOne = screen.createScreen(500,500)
    parser.parseFile('script', screenOne, green, edgeMatrix, transformMatrix)
main()

    
# def theyDontChange(x):
#     x = x + 2
# def theyDontChange(x):
#     x[0] = 999
# x = [1, 2, 3]
# theyDontChange(x)
# print(x)
