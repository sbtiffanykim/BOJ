import sys

input = sys.stdin.readline


def upper_bound(target):
    st, en = 0, n
    while st != en:
        mid = (st + en) // 2
        if a[mid] <= target:
            st = mid + 1
        elif a[mid] > target:
            en = mid
    return st


def lower_bound(target):
    st, en = 0, n
    while st != en:
        mid = (st + en) // 2
        if a[mid] < target:
            st = mid + 1
        elif a[mid] >= target:
            en = mid
    return st


if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    targets = list(map(int, input().split()))
    for target in targets:
        print(upper_bound(target) - lower_bound(target), end=' ')
