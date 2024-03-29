#!/bin/python3

import math
import os
import random
import re
import sys

# Sorting: Bubble Sort from HackerRank
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_r=profile
# Complete the countSwaps function below.


def countSwaps(a):
    count = 0
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(len(a) - 1):
            # print(i)
            aa = a[i]
            bb = a[i + 1]
            # print(aa,bb)

            if aa > bb:
                a[i], a[i + 1] = bb, aa
                count += 1
                is_sorted = False
                # print(a)

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

    return


print(str([1, 2, 3, 4, 3] + [1, 23, 4, 5]).strip('[]'))

# if __name__ == '__main__':
#     n = int(input())

#     a = list(map(int, input().rstrip().split()))

#     countSwaps(a)
