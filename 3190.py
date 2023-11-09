# 3190_뱀
# https://www.acmicpc.net/problem/3190

import sys

input = sys.stdin.readline


def play(board):
    x, y, head, time, tail_idx = 0, 0, 0, 0, 0
    board[0][0] = 0  # 뱀의 몸이 걸치는 곳은 0으로 기록
    snake = [(0, 0)]  # 뱀의 몸이 걸쳐있는 좌표를 기록

    while True:
        # 1. 몸 길이 늘리기(머리 좌표 이동)
        nx = x + dx[head]
        ny = y + dy[head]
        # 2. 벽이나 자기 몸을 치면 끝내기
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 0:
            return time + 1  # 이동 후에 부딪히므로 1 더하기
        # 3-1. 이동한 칸에 사과 있으면 사과 먹기
        if board[nx][ny] == 1:
            # head 전진
            board[nx][ny] = 0
        # 3-2. 이동한 칸에 사과 없으면 꼬리 길이 줄이기
        elif board[nx][ny] != 1:
            tail = snake[tail_idx]
            board[tail[0]][tail[1]] = -1  # 뱀, 사과 아닌 indicator로 바꾸기
            tail_idx += 1  # 꼬리 다음 위치로 바꾸기
            # head 전진
            board[nx][ny] = 0
        snake.append((nx, ny))  # 이동 후 뱀 몸 좌표 저장
        # 4. 시간 증가
        time += 1
        # 5. 회전
        if time in dir_change:
            head = turn[head][dir_change[time]]  # 새로운 머리방향 설정
        # 6. 좌표 갱신
        x, y = nx, ny


n = int(input())
board = [[-1] * n for _ in range(n)]
dir_change = dict()  # 뱀 회전 저장
# E: 0, S: 1, W: 2, N: 3
# 뱀 머리가 E, S, W, N 방향으로 향할 때 이동 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# (L, D)로 회전했을 때의 뱀의 머리 방향
turn = {0: (3, 1), 1: (0, 2), 2: (1, 3), 3: (2, 0)}

# 입력받기
apples = int(input())
for _ in range(apples):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1  # 사과의 위치에 1표시
dirs = int(input())
for _ in range(dirs):
    t, d = input().split()
    if d == "D":
        d = 1
    else:
        d = 0
    dir_change[int(t)] = d

print(play(board))
