#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    totalBribes = 0
    for pos, val in enumerate(q):
        #print("pos:" + str(pos) + " val:" + str(val))
        if (val-1) - pos > 2:
            print("Too chaotic")
        for j in range(max(0, val-2), pos):
            #print("\tj:" + str(j) + " max(0," + str(val-2) + "):" + str(max(0, val-2)) + " q[" + str(j) + "]:" + str(q[j]) + " - " + str(val))
            if q[j] > val:
                totalBribes += 1
    print(totalBribes)

if __name__ == '__main__':

    f = open("input.txt", "r")
    data = f.readlines()
    data = data[0].split(" ")
    data = [int(x) for x in data]
    print(data)
    data = [5, 1, 2, 3, 7, 8, 6, 4]
    minimumBribes(data)


