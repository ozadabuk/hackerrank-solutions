#!/bin/python3

import time

class Plant:
    def __init__(self, pesticide, days):
        self.pesticide = pesticide
        self.days = days
# Complete the poisonousPlants function below.
def poisonousPlants(a):
    stack = []
    maxDaysAlive = 0

    for pesticide in a:
        daysAlive = 0
        while stack and pesticide <= stack[-1].pesticide:
            daysAlive = max(daysAlive, stack.pop().days)

        if not stack:
            daysAlive = 0
        else:
            daysAlive += 1

        maxDaysAlive = max(maxDaysAlive, daysAlive)

        stack.append(Plant(pesticide, daysAlive))

    return maxDaysAlive


if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    params = lines[1].rstrip("\n")
    params = params.split(" ")
    params1 = [int(x) for x in params]


    #params1 = [3, 1, 10, 7, 3, 5, 6, 6]
    startTime = time.time()
    result = poisonousPlants(params1)
    print(time.time() - startTime)
    print(result)
