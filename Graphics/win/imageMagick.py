#!~/usr/bin/env python3

#???

from subprocess import Popen, PIPE
from os import remove
import screen

def saveExtension( screen, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screens ):
    ppm_name = 'pic'
    screen.writePpmFile(screens, ppm_name)
    Popen( ['display', ppm_name+'.ppm' ], stdin=PIPE, stdout = PIPE )
