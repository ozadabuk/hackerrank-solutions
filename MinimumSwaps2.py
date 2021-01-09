import math


# Complete the minimumSwaps function below.
import time
def minimumSwaps(arr):
    minSwap = 0
    n = len(arr)
    indices = {v:i for i, v in enumerate(arr)}
    sa = sorted(arr)

    for i, v in enumerate(arr):
        print(indices)
        print(arr)
        print(sa)
        correctVal = sa[i]
        print("correct value at " + str(i) + ": " + str(correctVal))
        if v != correctVal:
            sv = indices[correctVal]
            print("instead, found " + str(v) + " at i:" + str(i) + ", indices[" + str(correctVal) + "]:" + str(sv) + ", swap " + str(arr[sv]) + " with " + str(arr[i]))

            tmp = arr[sv]
            arr[sv] = arr[i]
            arr[i] = tmp
            indices[v] = sv
            minSwap += 1

    #print(arr)
    return minSwap


if __name__ == '__main__':
    f = open("input.txt", "r")
    data = f.readlines()
    data = data[0].split(" ")
    data = [int(x) for x in data]
    startTime = time.time()
    #print(data)
    #data = [7, 1, 3, 2, 4, 5, 6]
    data = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
    #data = [1, 3, 5, 2, 4, 6, 7]
    result = minimumSwaps(data)
    print(time.time()-startTime)
    print(result)