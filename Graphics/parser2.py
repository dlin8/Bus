
#!~usr/bin/env python3

import screen
import draw
import matrix
import random

def parseFile(fileName, screen, color, edgeMatrix, transformMatrix):
    scriptFile = open('{}'.formate(fileName), 'r')
    for line in scriptFile:
        currentLine = line.split()
        if(currentLine[0] == 'line'):
            argumentLine = scriptFile.readline().split()
            a = [ int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) ]
            b = [ int(argumentLine[3]), int(argumentLine[4]), int(argumentLine[5]) ]
            matrix.addEdge(edgeMatrix, a, b)
        elif(currentLine[0] == 'ident'):
            transformMatrix = matrix.setIdentityMatrix(transformMatrix)
        elif(currentLine[0] == 'move'):
            moveMatrix = matrix.createTranslateMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]))
            matrixMultiplication(moveMatrix, trnasformMatrix)
        elif(currentLine[0] == 'scale'):
            scaleMatrix = matrix.createScaleMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) )
            matrixMultiplication(scaleMatrix, trnasformMatrix)
        elif(currentLine[0] == 'rotate'):
            rotateMatrix = matrix.createRotateMatrix(argumentLine[0], int(argumentLine[1]))
            matrixMultiplication(rotateMatrix, trnasformMatrix)
        elif(currentLine[0] == 'circle'):
        elif(currentLine[0] == 'hermite'):
        elif(currentLine[0] == 'bezier'):
        elif(currentLine[0] == 'apply'):
        elif(currentLine[0] == 'display'):
        elif(currentLine[0] == 'save'):
        else:
            print('Bad command, ' + currentLine[0])
