import sys

sys.setrecursionlimit(10**7)

a, b, m = map(int, input().split())


def pow(a, b):
    if b == 1:
        return a % m
    val = pow(a, b // 2)  # k 계산 가능
    if b % 2 == 0:  # 짝수일 때
        return val * val % m  # 2k도 계산 가능
    else:
        return val * val * a % m  # 2k+1도 계산 가능


print(pow(a, b))
