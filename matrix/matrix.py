#!/usr/bin/env python3'''
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
            
                                  
def dotProduct(list1, list2):
    dotProduct = 0
    if len(list1) != len(list2):
        print('lists of unequal lengths')
        return false
    for i in range(0, len(list1)):
        dotProduct = dotProduct + (list1[i] * list2[i])
    return dotProduct


#Test Cases
edgeMatrix = []
for row in range(0,4):
    edgeMatrix.append([])
    for column in range(0,4):
        if(column == 4):
            edgeMatrix[row].append(1)
        else:
            edgeMatrix[row].append(row + column)

printMatrix(edgeMatrix)
print('multiplying previous matrix with scalar value \'3\'.')
scalarMultiplication(3, edgeMatrix)
printMatrix(edgeMatrix)
print('multiplying previous matrix with itself.')
matrixMultiplication(edgeMatrix, edgeMatrix)
printMatrix(edgeMatrix)
