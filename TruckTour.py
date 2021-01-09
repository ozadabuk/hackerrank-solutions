#!/bin/python3

import os
import sys
import time
from collections import deque
#
# Complete the truckTour function below.
#
from operator import sub


def truckTour(petrolpumps):
    # convert pumps list to a circular list
    for i in range(0, len(petrolpumps)):
        p = petrolpumps[i]
        if i < len(petrolpumps)-1:
            petrolpumps[i] = (p[0], p[1], i+1)
        else:
            petrolpumps[i] = (p[0], p[1], 0)
    startPoint = 0
    truckGas = 0
    starts = deque()
    for pump in petrolpumps:
        if pump[0] >= pump[1]:
            starts.append(pump)
    print("Total Start Points:" + str(len(starts)))
    print(str(starts))
    print("Petrol Pumps:")
    print(str(petrolpumps))
    while starts:
        start = starts.popleft()
        print("Start at " + str(start))# + " with " + str(truckGas) + "L gas")

        nextPumpIndex = start[2]
        currentPumpIndex = start[2]-1 if start[2] != 0 else len(petrolpumps) - 1
        current = petrolpumps[currentPumpIndex]
        j = nextPumpIndex
        outOfGas = False
        while j != currentPumpIndex:
            truckGas = truckGas + current[0]
            print("At " + str(current) + " next " + str(petrolpumps[current[2]]) + " gas left:" + str(truckGas - current[1]))
            if truckGas - current[1] >= 0:
                truckGas = truckGas - current[1]
                j = current[2]
                current = petrolpumps[j]
                print("Gas in tank: " + str(truckGas))
            else:
                truckGas = 0
                print("out of gas at " + str(j))
                outOfGas = True
                break
        if not outOfGas:
            startPoint = j
            print("Completed trip at " + str(j) + "\n")
            break
        else:
            print("Start again from next point\n")
        print(str(len(starts)) + " points to start from left")
    return startPoint


if __name__ == '__main__':
    f = open("input.txt", "r")
    petrolpumps = []
    for line in f:
        l = line[:-1]
        n = l.split(" ")
        petrolpumps.append([int(n[0]), int(n[1])])

    #result = truckTour(petrolpumps)

