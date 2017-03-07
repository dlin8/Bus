#!~usr/bin/env python3

import Screen
import Line
import Matrix
import Transform

def parseFile(fileName, screen, color, edgeMatrix, transformMatrix):
    scriptFile = open('{}', 'r'):
    num_lines = sum(1 for line in scriptFile)
    for i in range(0, num_lines):
        for j in range(0, len(argumentLine)):
            if(line[j] == '\n'):
                argumentLine = argumentLine[:j]
            
        for j in range(0, len(commandLine)):
            if(line[j] == '\n'):
                commandLine = commandLine [:j]
        
        completeCommand(screen, color, commandLine, argumentLine, edgeMatrix, transformMatrix)

    
def completeCommand(screen, color, commandLine, argumentLine, edgeMatrix, transformMatrix):
    if(command == 'line'):
        doLine(argumentLine, edgeMatrix)
        
    elif(command == 'ident'):
        doIdent(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'move'):
        doMove(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'scale'):
        doScale(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'rotate'):
        doRotate(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'apply'):
        doApply(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'display'):
        doDisplay(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    elif(command == 'save'):
        doSave(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    else:
        print('invalid command: {}'.format(command))
        
def doLine(argumentLine, edgeMatrix):
    a = [ argumentLine[1], argumentLine[3] ]
    b = [ argumentLine[7], argumentLine[9] ]
    addEdge(edgeMatrix, a, b)

def doIdent(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doMove(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doScale(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doRotate(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doApply(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doDisplay(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass

def doSave(screen, color, argumentLine, edgeMatrix, transformMatrix):
    pass


