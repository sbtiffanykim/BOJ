# 14499_주사위 굴리기

import sys
from collections import deque

input = sys.stdin.readline


# pos방향으로 주사위를 굴리는 함수
def roll_the_dice(pos):
    temp_dice = [0] * 6  # 굴린 후 각 면의 주사위에 쓰인 수를 저장할 리스트
    # pos방향으로 굴릴 때 원래의 index가 어느 곳에 위치하는 지 알려주는 index indicator
    status = {
        1: [3, 1, 0, 5, 4, 2],
        2: [2, 1, 5, 0, 4, 3],
        3: [4, 0, 2, 3, 5, 1],
        4: [1, 5, 2, 3, 0, 4],
    }
    for i in range(6):
        temp_dice[i] = dice[status[pos][i]]
    return temp_dice


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0] * 6  # 주사위 각 면에 쓰여있는 숫자(0: 윗면, 2: 오른쪽, 3: 왼쪽, 6: 바닥면)
move = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}  # 동, 서, 북, 남으로 각각 이동할 때 더할 좌표

for c in commands:
    # 주어진 명령대로 이동
    nx = x + move[c][0]
    ny = y + move[c][1]
    # 범위가 넘어가면 이동하지 않고 무시함
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    # 주사위 굴리기
    dice = roll_the_dice(c)
    # 이동한 칸에 쓰인 수가 0이라면 주사위 바닥면의 수 복사해 칸에 넣기
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    # 0이 아니라면
    else:
        dice[5] = board[nx][ny]  # 주사위 바닥면에 이동한 칸의 수 복사
        board[nx][ny] = 0  # 보드판의 수는 0으로 바꾸기
    x, y = nx, ny  # 이동한 위치로 현재 주사위 위치 갱신
    print(dice[0])  # 주사위 윗면에 쓰인 수 출력
