#!~/usr/bin/env python3

import math
import Matrix

# a, b, and c being the amount that each coordinate is translated by.
def createTranslateMatrix(a, b, c):
    translateMatrix = []
    for i in range(0,4):
        translateMatrix.append([])
        for j in range(0,4):
            if(i == j):
                translateMatrix[i].append(1)
            else:
                translateMatrix[i].append(0)
    translateMatrix[0][3] = a
    translateMatrix[1][3] = b
    translateMatrix[2][3] = c
    
# a, b, and c being the amount that each coordinate is scaled by.
# Scales with respect to origin
def createScaleMatrix(a, b, c):
    scaleMatrix = []
    for i in range(0,4):
        scaleMatrix.append([])
        for j in range(0,4):
            if(i == j):
                scaleMatrix[i].append(1)
            else:
                scaleMatrix[i].append(0)
    scaleMatrix[0][0] = a
    scaleMatrix[1][1] = b
    scaleMatrix[2][2] = c

def createRotateMatrixX(theta):
    theta = math.radians(theta)
    for i in range(0,4):
        rotateMatrix.append([])
        for j in range(0,4):
            if(i == j):
                rotateMatrix[i].append(1)
            else:
                rotateMatrix[i].append(0)
    rotateMatrix[0][0] = math.cos(theta)
    rotateMatrix[0][1] = (-1 * math.sin(theta))
    rotateMatrix[1][0] = math.sin(theta)
    rotateMatrix[1][1] = math.cos(theta)
    
    

    
# def createRotateMatrixY(theta):

# def createRotateMatrixZ(theta):

def createRotateMatrix(axis, theta):
    theta = math.radians(theta)
    rotateMatrix = []
    for i in range(0,4):
        rotateMatrix.append([])
        for j in range(0,4):
            if(i == j):
                rotateMatrix[i].append(1)
            else:
                rotateMatrix[i].append(0)
    if(axis == '0' or axis == 'x'):
        # y = ycostheta - zsintheta
        rotateMatrix[1][1] = math.cos(theta)        #ycostheta
        rotateMatrix[1][2] = (-1 * math.sin(theta)) #-zsintheta
        # z = zcostheta + ysintheta
        rotateMatrix[2][2] = math.cos(theta)        #zcostheta
        rotateMatrix[2][1] = math.sin(theta)        #ysintheta
        
    elif(axis == '1' or axis == 'y'):
        # z = zcostheta - xsintheta
        rotateMatrix[2][2] = math.cos(theta)        #zcostheta
        rotateMatrix[2][0] = (-1 * math.sin(theta)) #-xsintheta
        # x = xcostheta + zsintheta
        rotateMatrix[0][0] = math.cos(theta)        #xcostheta
        rotateMatrix[0][2] = math.sin(theta)        #zsintheta
        
    elif(axis == '2' or axis == 'z'):
        # x = xcostheta - ysintheta
        rotateMatrix[0][0] = math.cos(theta)        #xcostheta
        rotateMatrix[0][1] = (-1 * math.sin(theta)) #-ysintheta
        # y = ycostheta + xsinthetat
        rotateMatrix[1][1] = math.cos(theta)        #ycostheta
        rotateMatrix[1][0] = math.sin(theta)        #xsintheta
    print(theta)
    Matrix.printMatrix(rotateMatrix)
