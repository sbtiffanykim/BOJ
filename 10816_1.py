# using the bisect library

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def count_by_range(a, t):
    right_idx = bisect_right(a, t)
    left_idx = bisect_left(a, t)
    return right_idx - left_idx


if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    targets = list(map(int, input().split()))
    for target in targets:
        print(count_by_range(a, target), end=' ')
