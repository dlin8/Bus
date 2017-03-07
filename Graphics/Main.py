#!~/usr/bin/env python3

import Screen
import Line
import Matrix
import Transform

edgeMatrix = []
transformMatrix = []

def main():
    # Line.drawLine(screenOne, [1,0], [499,499], color)
    scriptFile =  open('script', 'r')
    #for line in scriptFile:
    #    print(line)
    num_lines = sum(1 for line in scriptFile)
    print(num_lines)
main()
