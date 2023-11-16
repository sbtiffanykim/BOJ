# 20058_마법사 상어와 파이어스톰
# https://www.acmicpc.net/problem/20058

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 좌표 회전 후 얼음 녹이는 과정을 수행하는 함수
def firestorm(board, size):
    new_board = [[0 for _ in range(n)] for _ in range(n)]  # 각 격자 회전키고 난 후의 결과
    # 1. 격자 나누기
    for x in range(0, n, size):  # row_start
        for y in range(0, n, size):  # column_start
            for i in range(size):  # row
                for j in range(size):  # column
                    # 2. 회전하기
                    new_board[x + j][y + size - i - 1] = board[x + i][y + j]

    # 3. 얼음 녹이기
    melting = []  # 녹일 얼음칸 좌표 저장
    for x in range(n):
        for y in range(n):
            cnt = 0  # 인접한 얼음칸 저장
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if new_board[nx][ny] > 0:
                    cnt += 1
            if cnt < 3 and new_board[x][y] > 0:
                melting.append((x, y))

    for x, y in melting:
        new_board[x][y] -= 1

    return new_board


# 덩어리를 이루는 얼음칸수를 체크하는 함수
def find_block(x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 0  # 덩어리 이루는 칸 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and board[nx][ny] > 0:
                area += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return area


n, q = map(int, input().split())
n = 2**n
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
total = 0  # 남아있는 얼음 총 합
max_area = 0  # 가장 큰 덩어리

# q만큼 파이어스톰 실행
for command in commands:
    board = firestorm(board, 2**command)

for i in range(n):
    for j in range(n):
        total += board[i][j]
        if board[i][j] > 0:
            cur = find_block(i, j)
            if cur:  # 덩어리가 존재하면
                max_area = max(max_area, cur + 1)  # 출발점도 덩어리 구성 칸수에 넣기

print(total)
print(max_area)
