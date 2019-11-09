#!/usr/bin/env python3

import numpy as np
import random

def print_eca_help():
    print('#---------------------------------------------------------#')
    print('#                                                         #')
    print('# Simple implementation of elementary cellular automata   #')
    print('# Usage:                                                  #')
    print('#     ./pyeca.py [options]                                #')
    print('# Options:                                                #')
    print('# -w -- width of output image in pixels, default is 240   #')
    print('# -h -- height of output image in pixels, default is 320  #')
    print('# -r -- rule, default is 0                                #')
    print('# -o -- name of output image, default is eca              #')
    print('#                                                         #')
    print('# It also could be imported in other script and used      #')
    print('# as function:                                            #')
    print('# import pyeca                                            #')
    print('# ...                                                     #')
    print('# myvar = eca(width, height, rule)                        #')
    print('#                                                         #')
    print('#---------------------------------------------------------#')


def eca(width, height, rule, seed=0):
    np.random.seed(0)
    gen = np.zeros((height, width), dtype=np.uint8)
    gen[0]=np.random.randint(0,2,width)

    for i in range(height-1):
        gen[i+1][1:width-1]=(rule>>(4*gen[i][0:width-2] + 2*gen[i][1:width-1] + gen[i][2:width]))%2
        gen[i+1][0]=(rule>>(4*gen[i][-1] + 2*gen[i][0] + gen[i][1]))%2
        gen[i+1][width-1]=(rule>>(4*gen[i][width-2] + 2*gen[i][width-1] + gen[i][0]))%2

    return gen


if __name__=='__main__':
    from PIL import Image
    import sys

    width = 240
    height = 320
    rule = 0
    name='eca'

    i=0

    while i < len(sys.argv):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            print_eca_help()
            exit(0)
        if sys.argv[i] == "-w":
            if i+1 >= len(sys.argv) or not(sys.argv[i+1].isnumeric()) or int(sys.argv[i+1]) < 3 or int(sys.argv[i+1]) > 3000:
                raise Exception("width value should be a natural value between 3 and 3000")
            width = int(sys.argv[i+1])
            i+=2
            continue
        if sys.argv[i] == "-h":
            if i+1 >= len(sys.argv) or not(sys.argv[i+1].isnumeric()) or int(sys.argv[i+1]) < 3 or int(sys.argv[i+1]) > 3000:
                raise Exception("height value should be a natural value between 3 and 3000")
            height = int(sys.argv[i+1])
            i+=2
            continue
        if sys.argv[i] == "-r":
            if i+1 >= len(sys.argv) or not(sys.argv[i+1].isnumeric()) or int(sys.argv[i+1]) < 0 or int(sys.argv[i+1]) > 255:
                raise Exception("rule should be a natural value between 0 and 255")
            rule = int(sys.argv[i+1])
            i+=2
            continue
        if sys.argv[i] == '-o':
            name=sys.argv[i+1]
            i+=2
            continue
        i+=1

    print("width : ", width, "; height : ", height, "; rule : ", rule)
    Image.fromarray(eca(width, height, rule)*255).save(name+'.png')
