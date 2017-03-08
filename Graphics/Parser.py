#!~usr/bin/env python3

import Screen
import Line
import Matrix
import Transform

def parseFile(fileName, screen, color, edgeMatrix, transformMatrix):
    # with as closes file automatically, reopen after number of lines is got
    # with open('{}'.format(fileName), 'r') as scriptFile:
    #     num_lines = sum(1 for line in scriptFile)
    scriptFile = open('{}'.format(fileName), 'r')
    for line in scriptFile:
        line = line.split()
        completeCommand(scriptFile, screen, color, line, edgeMatrix, transformMatrix)

def completeCommand(scriptFile, screen, color, commandLine, edgeMatrix, transformMatrix):
    if(commandLine[0] == 'line'):
        argumentLine = scriptFile.readline().split()
        doLine(argumentLine, edgeMatrix)
        
    elif(commandLine[0] == 'ident'):
        doIdent(transformMatrix)
        
    elif(commandLine[0] == 'move'):
        argumentLine = scriptFile.readline().split()
        doMove(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'scale'):
        argumentLine = scriptFile.readline().split()
        doScale(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'rotate'):
        argumentLine = scriptFile.readline().split()
        doRotate(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'apply'):
        doApply(screen, color, edgeMatrix)
        
    elif(commandLine[0] == 'display'):
        argumentLine = scriptFile.readline().split()
        doDisplay(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(commandLine[0] == 'save'):
        argumentLine = scriptFile.readline().split()
        doSave(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    else:
        print('invalid command: {}'.format(commandLine[0]))

def doLine(argumentLine, edgeMatrix):
    a = [ int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) ]
    b = [ int(argumentLine[3]), int(argumentLine[4]), int(argumentLine[5]) ]
    Matrix.addEdge(edgeMatrix, a, b)
    
def doIdent(transformMatrix):
    transformMatrix = Matrix.getIdentityMatrix(transformMatrix)

def doMove(argumentLine, transformMatrix):
    moveMatrix = Transform.createTranslateMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]))
    transformMatrix = Matrix.matrixMultiplication(moveMatrix, transformMatrix)

def doScale(argumentLine, transformMatrix):
    scaleMatrix = Transform.createScaleMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) )
    transformMatrix = Matrix.matrixMultiplication(scaleMatrix, transformMatrix)
    
def doRotate(argumentLine, transformMatrix):
    rotateMatrix = Transform.createRotateMatrix(argumentLine[0], int(argumentLine[1]))
    transformMatrix = Matrix.matrixMultiplication(rotateMatrix, transformMatrix)

def doApply(screen, color, edgeMatrix):
    Matrix.drawEdges(screen, edgeMatrix, color)

def doDisplay(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doSave(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass


