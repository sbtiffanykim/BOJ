# 17219_비밀번호 찾기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()

for _ in range(n):
    address, pw = input().split()
    memo[address] = pw

for _ in range(m):
    print(memo[input().rstrip()])
