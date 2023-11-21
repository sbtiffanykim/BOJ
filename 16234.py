# 16234_인구 이동
# https://www.acmicpc.net/problem/16234

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x1, y1, x2, y2):
    if l <= abs(board[x1][y1] - board[x2][y2]) <= r:
        return True
    return False


def bfs(x, y):
    global moved
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    total_population = board[x][y]
    union = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if in_range(x, y, nx, ny):
                queue.append((nx, ny))
                union.append((nx, ny))
                total_population += board[nx][ny]
                visited[nx][ny] = True

    if len(union) > 1:  # 연합을 이룰 수 있는 경우
        moved = True
        avg_population = total_population // len(union)
        for union_x, union_y in union:
            board[union_x][union_y] = avg_population


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
days = 0  # 인구 이동이 있는 지 여부
moved = True  # 인구 이동 기록

while moved:  # 인구 이동이 더 이상 일어나지 않을 때 까지 반복
    moved = False  # 인구 이동 발생하는 지 알기 위해 false로 설정
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    if moved:
        days += 1

print(days)
