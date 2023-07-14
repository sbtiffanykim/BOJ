import sys

sys.setrecursionlimit(10**7)

n = int(input())


def move(a, b, n):
    if n == 1:
        print(a, b)
        return
    move(a, 6 - a - b, n - 1)
    print(a, b)
    move(6 - a - b, b, n - 1)


print(2**n - 1)
move(1, 3, n)
