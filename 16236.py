# 16236_아기 상어
# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global shark_size, fish_count, time, shark_x, shark_y
    queue = deque()
    dist = [[-1] * n for _ in range(n)]
    dist[shark_x][shark_y] = 0  # 초기 상어 위치 기준으로 거리 갱신하기 위해 0으로 초기화
    queue.append((shark_x, shark_y))
    target = []  # 먹을 수 있는 물고기 후보

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 칸이거나 이미 방문한 칸이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n or dist[nx][ny] > -1:
                continue
            # 상어 크기보다 작거나 같을 경우, 빈칸인 경우 이동 가능
            if 0 <= board[nx][ny] <= shark_size:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                # 잡아먹을 수 있는 물고기라면
                if 0 < board[nx][ny] < shark_size:
                    target.append((nx, ny, dist[nx][ny]))  # target에 추가

    # 먹을 수 있는 물고기가 없는 경우
    if not target:
        return False

    # 먹을 수 있는 물고기가 있는 경우
    target.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, 위, 왼쪽 순으로 정렬
    tx, ty, t_dist = target[0]  # 먹어야 하는 물고기
    board[shark_x][shark_y] = 0  # 상어 위치 빈칸으로 처리 이동
    board[tx][ty] = 9  # 먹은 물고기 자리로 상어 이동
    shark_x, shark_y = tx, ty  # 상어 좌표 갱신

    time += t_dist  # 시간 증가
    fish_count += 1

    if fish_count == shark_size:
        fish_count = 0  # 물고기 먹은 수 초기화
        shark_size += 1  # 상어 크기 증가

    return True


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
time = 0  # 총 걸린 시간
shark_size = 2  # 아기 상어 크기
eat_count = 0  # 먹은 물고기 개수
shark_x, shark_y = 0, 0  # 아기 상어 위치

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:  # 아기 상어 위치
            shark_x, shark_y = i, j
            board[i][j] = 0  # 아기 상어 위치 초기화

while True:
    if not bfs():
        break

print(time)
