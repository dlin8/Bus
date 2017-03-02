#!~/usr/bin/env python3

import screen
import line
def main():
    screenOne = createScreen(500,500)
    color = [0, 255, 255]
    plot(screenOne, 0, 0, color)
    plot(screenOne, 500, 500, color)
    writePpmFile(screenOne, 255, test.ppm)
main()
