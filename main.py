import cv2
import numpy as np
import sys
import argparse

def loadJudge(img, imgName):
    if img == None:
        print "none"
    else:
        print "** "+imgName+" is loaded **"




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Transmissive binary image creater")
    parser.add_argument("-f", help = "path/to/imgfile.png")
    parser.add_argument("-o", help = "path/to/output.png")
    parser.add_argument("-t", help = "threshold value")
    parser.add_argument("-r", help = "intensity of RED(0-255) ")
    parser.add_argument("-g", help = "intensity of GREEN(0-255) ")
    parser.add_argument("-b", help = "intensity of BLUE(0-255) ")

    args = parser.parse_args()

    imgName = args.f
    th = int(args.t)
    r  = int(args.r)
    g  = int(args.g)
    b  = int(args.b)

    src = cv2.imread(imgName, 0) 
    src = np.uint8(src)

    loadJudge(src, imgName) 

    # with alpha channel
    out = np.zeros((src.shape[0], src.shape[1], 4))

    print("** Now converting... **")
    print("** R: "+str(r)+"/ G: "+str(g)+"/ B: "+str(b)+" **")

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            if src[y, x] < th:
                out[y, x, 0] = 255
                out[y, x, 1] = 255
                out[y, x, 2] = 255
                out[y, x, 3] = 0 
            else:
                out[y, x, 0] = b 
                out[y, x, 1] = g 
                out[y, x, 2] = r 
                out[y, x, 3] = 255 

    cv2.imwrite("out.png", out) 

    print("** fin **")
