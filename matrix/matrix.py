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
    retMatrix = []

def dotProduct(list1, list2):
    dotProduct = 0
    if( len(list1) != len(list2) )
        return false
    for i in range(0, len(list1)):
        dotProduct = dotProdcut + (list1[i] * list2[i])
    return dotProduct


#Test Cases
edgeMatrix = []
for row in range(0,4):
    edgeMatrix.append([])
    for column in range(0,6):
        edgeMatrix[row].append(row + column)

printMatrix(edgeMatrix)
print('multiplying previous matrix with scalar value \'3\'.')
scalarMultiplication(3, edgeMatrix)
printMatrix(edgeMatrix)
