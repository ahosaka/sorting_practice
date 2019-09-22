#!/bin/python3

import math
import os
import random
import re
import sys

# Insertion Sort - Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=false
# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    sorted_area = [arr[0]]
    unsorted_area = arr[1:]

    for i in range(len(unsorted_area)):
        sorted_area.append(unsorted_area[i])

        for j in range(len(sorted_area)):
            if sorted_area[-1] < sorted_area[j]:
                sorted_area.insert(j,sorted_area[-1])
                sorted_area.pop()
        print(' '.join(map(str,sorted_area + unsorted_area[i+1:])))

    return


# if __name__ == '__main__':
#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort2(n, arr)
