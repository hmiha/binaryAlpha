import cv2
import numpy as np
import sys
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Transmissive binary image creater")
    parser.add_argument("-f", help = "path/to/imgfile")
    parser.add_argument("-t", help = "threshold value")

    args = parser.parse_args()
    imgName = args.f
    th = int(args.t)


    src = cv2.imread(imgName, 0) 
    src = np.uint8(src)
    if src == None:
        print "none"
    else:
        print imgName,"is loaded"

    out = np.zeros((src.shape[0], src.shape[1], 3))
    print src.shape[0]
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            if src[y, x] < th:
                out[y, x, 0] = 255
                out[y, x, 1] = 255
                out[y, x, 2] = 255
            else:
                out[y, x, 0] = 0
                out[y, x, 1] = 0
                out[y, x, 2] = 255

    cv2.imwrite("out.png", out) 
