#!/bin/python3

import math
import os
import random
import re
import sys

# Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=false
# Complete the insertionSort1 function below.


def insertionSort1(n, arr):
    test = arr[-1]
    for i in reversed(range(n - 1)):
        if arr[i] >= test and i != 0:
            arr[i + 1] = arr[i]

            a = ' '.join(map(str, arr))
            print(a)
            arr[i] = test

        elif arr[i] > test and i == 0:
            arr[i + 1] = arr[i]
            # arr[i] = test
            b = ' '.join(map(str, arr))
            print(b)
            arr[i] = test
            b2 = ' '.join(map(str, arr))
            print(b2)

        else:
            arr[i + 1] = test
            c = ' '.join(map(str, arr))
            print(c)
            break
    return


# if __name__ == '__main__':
#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort1(n, arr)
