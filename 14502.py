# 14502_연구소
# https://www.acmicpc.net/problem/14502

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스 전파 탐색을 위한 함수
def bfs():
    virus_spread = 0  # 전파된 바이러스를 저장하기 위한 변수
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        virus_spread += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 전파 가능한 지역인 경우
            # 여러번 탐색해야 하므로 board값 자체를 바꾸지는 않음
            if not visited[nx][ny] and board[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return virus_spread


# depth번째 벽을 세운 후, idx번째 빈칸에 대해 탐색
def dfs(depth, idx):
    global ans
    # 벽 3개를 다 세운 경우
    if depth == 3:
        # 바이러스 전파
        tmp = bfs()
        # 안전지대 = 빈칸 - 바이러스 퍼진 영역의 수 + 원래 바이러스의 수 - 세운 벽의 개수(=3)
        # bfs의 리턴값에 원래 바이러스가 있던 칸도 포함되므로, 원래 바이러스가 있던 칸 개수를 더해주어야 함
        ans = max(ans, (len(blank) - tmp + len(virus) - 3))
        return
    # i번째 빈칸에 대해 벽으로 바꾸면서 백트래킹 진행
    for i in range(idx, len(blank)):
        board[blank[i][0]][blank[i][1]] = 1  # 벽 세우기
        dfs(depth + 1, i + 1)  # 다음 빈칸에 대해 탐색
        board[blank[i][0]][blank[i][1]] = 0  # 벽 해제


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
blank = list()
virus = list()
ans = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 빈칸 좌표 저장
            blank.append((i, j))
        elif board[i][j] == 2:  # 바이러스 좌표 저장
            virus.append((i, j))

dfs(0, 0)
print(ans)
