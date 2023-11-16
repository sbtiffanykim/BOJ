# 20057_마법사 상어와 토네이도
# https://www.acmicpc.net/problem/20057

import sys

input = sys.stdin.readline

# L -> D -> R -> U
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 토네이도 이동 방향에 따른 모래가 흩날리는 비율
left = [
    (0, -2, 0.05),
    (-1, -1, 0.10),
    (1, -1, 0.10),
    (-2, 0, 0.02),
    (-1, 0, 0.07),
    (1, 0, 0.07),
    (2, 0, 0.02),
    (-1, 1, 0.01),
    (1, 1, 0.01),
    (0, -1, 0),  # 앞의 비율로 모래 옮긴 후에 나머지를 고려해야 하므로 맨 뒤 요소로 정해야 함
]

down = [(-y, x, z) for x, y, z in left]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
trans = {0: left, 1: down, 2: right, 3: up}


def move_sand(x, y, sand):
    global answer
    total_sand = 0  # 현재까지 이동한 모래 양 더해주기
    if y < 0:
        return
    for i, j, prop in sand:
        nx = x + i
        ny = y + j
        if prop == 0:  # a칸으로 이동한 경우
            moved_sand = board[x][y] - total_sand
        else:  # 다른 칸으로 이동했을 경우
            moved_sand = int(board[x][y] * prop)  # 현재 칸에 옮겨져야 하는 모래 무게
            total_sand += moved_sand  # 옮겨진 모래의 양 더하기
        if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 범위를 벗어났을 때
            answer += moved_sand
        else:
            board[nx][ny] += moved_sand
    board[x][y] = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x = y = n // 2
d = 0  # 토네이도 회전 방향
step = 0  # 움직여야하는 칸 수
is_stopped = False
answer = 0  # 밖으로 나간 모래의 양

# 토네이도 회전
while not is_stopped:
    d %= 4
    # R, L로 진입할 때 한칸 씩 더 이동
    if d % 2 == 0:
        step += 1
    for _ in range(step):
        x += dx[d]
        y += dy[d]
        move_sand(x, y, trans[d])
        if x == 0 and y == 0:
            is_stopped = True
    d += 1

print(answer)
