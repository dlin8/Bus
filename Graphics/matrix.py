#!/usr/bin/env python3

import screen
import line

#Make it floaty

def printMatrix(matrix):
    printString = ''
    rows = len(matrix)
    columns = len(matrix[0])
    for row in range (0, rows):
        for column in range (0, columns):
            printString = printString + str(matrix[row][column]) + ' '
        printString = printString + '\n'
    print(printString)

def scalarMultiplication(scalar, matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for row in range(0, rows):
        for column in range(0, columns):
            matrix[row][column] = matrix[row][column] * scalar

# This function is specific to 4xN edge matrix multiplied BY a 4x4 matrix
def matrixMultiplication(matrix, edgeMatrix):
    if len(matrix[0]) != len(edgeMatrix):
        print('matrices cannot be multiplied.')
        return false
    retMatrix = []
    tempList = []
    for row in range( len(matrix) ):
        retMatrix.append([])
        for column in range( len(edgeMatrix[row]) ):
            for i in range( len(edgeMatrix) ):
                tempList.append(edgeMatrix[column][i])
            retMatrix[row].append(dotProduct(matrix[row], tempList))
            tempList = []
    '''
    for row in range( len(retMatrix) ):
        if( row >= len(edgeMatrix) ):
            edgeMatrix.append([])
        for column in range( len(retMatrix[row]) ):
            edgeMatrix[row][column] = retMatrix[row][column]
    '''
    edgeMatrix = retMatrix[:]
    return edgeMatrix
            
                                  
def dotProduct(list1, list2):
    dotProduct = 0
    if len(list1) != len(list2):
        print('lists of unequal lengths')
        return false
    for i in range(0, len(list1)):
        dotProduct = dotProduct + (list1[i] * list2[i])
    return dotProduct

def getIdentityMatrix(matrix):
    length = max(len(matrix), len(matrix[0]))
    retMatrix = []
    for r in range(0, length):
        retMatrix.append([])
        for c in range(0, length):
            if(r == c):
                retMatrix[r].append(1)
            else:
                retMatrix[r].append(0)
    return retMatrix

#adds a point to edgeMatrix
def addPoint(matrix, a):
    matrix[0].append(a[0])
    matrix[1].append(a[1])
    matrix[2].append(a[2])
    matrix[3].append(1)

#adds an edge to edgeMatrix using addPoint
def addEdge(matrix, a, b):
    addPoint(matrix, a)
    addPoint(matrix, b)

def drawEdges(screen, edgeMatrix, color):
    for i in range(0, len(edgeMatrix[0]) - 1, 2):
        line.drawLine(screen, [edgeMatrix[0][i], edgeMatrix[1][i]], [edgeMatrix[0][i+1], edgeMatrix[1][i+1]], color)

