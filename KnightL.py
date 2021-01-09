#!/bin/python3
import math
import os
import random
import re
import sys
from collections import deque


class Node:
    def __init__(self, row=0, col=0, parent=None):
        self.r = row
        self.c = col
        self.p = parent

def isInList(l, n):
    for item in l:
        if isSameNode(item, n):
            return True
    return False

def printList(l):
    s = ""
    for item in l:
        s += "(" + str(item.r) + "," + str(item.c) + ") "
    print(s)

def tracePath(s, e):
    p = []
    curr = e
    while not isSameNode(curr, s):
        curr = curr.p
        p.append(curr)
    return p


def isSameNode(n1: Node, n2: Node) -> []:
    if n1 is None or n2 is None:
        return False
    if n1.r == n2.r and n1.c == n2.c:
        return True
    else:
        return False

def getIJ(n):
    nums = []
    for i in range(1, n):
        for j in range(1, n):
            nums.append((i, j))
    return nums

def getMoves(i, j):
    moves = []
    moves.append((i, j))
    moves.append((i, -1*j))
    moves.append((-1*i, j))
    moves.append((-1*i, -1*j))
    moves.append((j, i))
    moves.append((j, -1*i))
    moves.append((-1*j, i))
    moves.append((-1*j, -1*i))
    return moves

def isValidMove(n, move):
    if -1 < move[0] < n and -1 < move[1] < n:
        return True
    else:
        return False

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    ijs = getIJ(n)
    steps = []
    for ij in ijs:
        moves = getMoves(ij[0], ij[1])
        path = []
        start = Node(0, 0, None)
        end = Node(n - 1, n - 1, None)
        openList = deque()
        closedList = deque()
        openList.append(start)

        while openList:
            current = openList[0]
            closedList.append(current)
            openList.popleft()

            if isSameNode(current, end):
                path = tracePath(start, current)
                break

            #printList(openList)
            for move in moves:
                newMove = (current.r + move[0], current.c + move[1])
                if isValidMove(n, newMove):
                    m = Node(newMove[0], newMove[1], current)
                    if not isInList(openList, m) and not isInList(closedList, m):
                        openList.append(m)

        if len(path) > 0:
            steps.append(len(path))
        else:
            steps.append(-1)

    results = []
    res = []
    i = 1
    for item in steps:
        res.append(item)
        if i % (n-1) == 0:
            #print(res + "\n")
            results.append(res)
            res = []
        #else:
            #res += " "
        i = i + 1

    return results

if __name__ == '__main__':
    result = knightlOnAChessboard(5)
    print('\n'.join([' '.join(map(str, x)) for x in result]))
