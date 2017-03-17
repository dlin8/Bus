#!~usr/bin/env python3

import screen
import draw
import matrix
import random
import time

def parseFile(fileName, screens, color, edgeMatrix, transformMatrix):
    scriptFile = open('{}'.format(fileName), 'r')
    for line in scriptFile:
        currentLine = line.split()
        print(currentLine[0])
        if(currentLine[0] == 'line'):
            argumentLine = scriptFile.readline().split()
            a = [ int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) ]
            b = [ int(argumentLine[3]), int(argumentLine[4]), int(argumentLine[5]) ]
            matrix.addEdge(edgeMatrix, a, b)
        elif(currentLine[0] == 'ident'):
            matrix.setIdentityMatrix(transformMatrix)
        elif(currentLine[0] == 'move'):
            argumentLine = scriptFile.readline().split()
            moveMatrix = matrix.createTranslateMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]))
            matrix.matrixMultiplication(moveMatrix, transformMatrix)
        elif(currentLine[0] == 'scale'):
            argumentLine = scriptFile.readline().split()
            scaleMatrix = matrix.createScaleMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) )
            matrix.matrixMultiplication(scaleMatrix, transformMatrix)
        elif(currentLine[0] == 'rotate'):
            argumentLine = scriptFile.readline().split()
            rotateMatrix = matrix.createRotateMatrix(argumentLine[0], int(argumentLine[1]))
            matrix.matrixMultiplication(rotateMatrix, transformMatrix)
        elif(currentLine[0] == 'circle'):
            pass
        elif(currentLine[0] == 'hermite'):
            pass
        elif(currentLine[0] == 'bezier'):
            pass
        elif(currentLine[0] == 'apply'):
            matrix.matrixMultiplication(transformMatrix, edgeMatrix)
        elif(currentLine[0] == 'display'):
            matrix.drawEdges(screens, edgeMatrix, color)
            screen.display(screens)
            screen.clearScreen(screens)
            time.sleep(1)
        elif(currentLine[0] == 'save'):
            argumentLine = scriptFile.readline().split()
            matrix.drawEdges(screens, edgeMatrix, color)
            screen.saveExtension(screens, argumentLine[0])
        else:
            print('Bad command, ' + currentLine[0])
        matrix.printMatrix(transformMatrix)
        matrix.printMatrix(edgeMatrix)
