# 1389_케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [[n] * n for _ in range(n)]

for i in range(n):
    board[i][i] = 0  # 대각선은 0

for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = board[b - 1][a - 1] = 1  # 서로 아는 사람끼리는 1로 표시

for k in range(n):  # 기준점 유저
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])  # Floyd-Marshall 최단경로 갱신: Dab = min(Dab, Dac+Dcb)

metrics = [None] * n  # (유저 번호, 케빈베이컨 지수) 저장
for i in range(n):
    metrics[i] = [i + 1, sum(board[i])]
metrics.sort(key=lambda x: (x[1], x[0]))  # 지수가 가장 작은 순, 유저 번호가 작은 순으로 정렬
print(metrics[0][0])
