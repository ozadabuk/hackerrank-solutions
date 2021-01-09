from collections import deque
import math
import time


def downToZero(N):
    if N == 0:
        return 0
    openList = deque()
    closedList = set()
    start = (N, 0)
    end = None
    openList.append(start)

    while openList:
        current = openList[0]
        closedList.add(current[0])
        openList.popleft()
        if current[0]-1 == 0:
            end = (current[0]-1, current[1] + 1)
            break

        n = current[0]
        level = current[1] + 1
        nums = []
        lower = int(math.sqrt(n))
        for j in range(lower, 1, -1):
            if n % j == 0:
                m = max(j, int(n / j))
                nums.append((m, level))
        possibleMoves = nums
        possibleMoves.append((current[0] - 1, current[1] + 1))
        sortedMoves = sorted(possibleMoves, key=lambda tup: tup[0])
        for p in sortedMoves:
            if p[0] not in closedList:
                openList.append(p)
    return end[1]


if __name__ == "__main__":

    f = open("input.txt", "r")
    temp = [int(line[:-1]) for line in f]
    startTime = time.time()
    for i in temp:
        N = i
        result = downToZero(N)
    print("end: " + str(time.time() - startTime))
    print(result)