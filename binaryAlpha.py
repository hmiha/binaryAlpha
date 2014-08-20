#!/usr/bin/env python
#
# 
# binaryAlpha.py
#
# Aug. 2014.
#  coded by Hajime MIHARA
#  http://omilab.naist.jp/~mihara/index.html
#

import cv2
import numpy as np
import argparse

def add2parser(parser):
    parser.add_argument("-f", help = "path/to/imgfile.png")
    parser.add_argument("-o", help = "path/to/output.png")
    parser.add_argument("-t", help = "threshold value")
    parser.add_argument("-r", help = "intensity of RED(0-255) ")
    parser.add_argument("-g", help = "intensity of GREEN(0-255) ")
    parser.add_argument("-b", help = "intensity of BLUE(0-255) ")

    return parser


def loadJudge(img, imgName):
    if img == None:
        print "none"
    else:
        print "** "+imgName+" is loaded **"

def binarize(src, out):

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            if src[y, x] < th:
                out[y, x, 0:2] = 255
                out[y, x, 3] = 0 
            else:
                out[y, x, 0] = b 
                out[y, x, 1] = g 
                out[y, x, 2] = r 
                out[y, x, 3] = 255 
    return out

if __name__ == "__main__":

    msg = "Transmissive binary image creater"
    parser = argparse.ArgumentParser(description = msg)

    add2parser(parser)

    args = parser.parse_args()

    imgName = args.f
    outName = args.o
    th = int(args.t)
    r  = int(args.r)
    g  = int(args.g)
    b  = int(args.b)

    src = np.uint8(cv2.imread(imgName, 0)) 

    loadJudge(src, imgName) 

    print("** Now converting... **")
    print("** R: "+str(r)+"/ G: "+str(g)+"/ B: "+str(b)+" **")

    out = np.zeros((src.shape[0], src.shape[1], 4))
    binarize(src, out)

    cv2.namedWindow("out")
    cv2.imshow("out", out)
    cv2.waitKey(0)
    cv2.imwrite(outName, out) 


    print("** fin **")
