import sys

input = sys.stdin.readline


def binary_search(t):
    st, en = 0, (n - 1)
    while st <= en:
        mid = (st + en) // 2
        if a[mid] > t:
            en = mid - 1
        elif a[mid] < t:
            st = mid + 1
        else:
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    targets = list(map(int, input().split()))
    for target in targets:
        print(binary_search(target))
