# 11559_Puyo Puyo

import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# board[i][j]와 상하좌우로 이어진 같은 뿌요를 찾아 좌표를 반환하는 함수
def bfs(i, j):
    same_puyos = [(i, j)]  # 같은 종류 뿌요의 좌표를 저장하는 리스트
    queue = deque()
    queue.append((i, j))
    vis[i][j] = True
    color = board[i][j]  # 현재 뿌요 종류

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 넘어서면 탐색하지 않음
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            # 이미 방문한 좌표거나 현재 색깔 뿌요와 다르면 탐색하지 않음
            if vis[nx][ny] or board[nx][ny] != color:
                continue
            vis[nx][ny] = True
            queue.append((nx, ny))
            same_puyos.append((nx, ny))

    return same_puyos


# 중력을 받아 위에서부터 아래로 내려가는 함수
def gravitate():
    for i in range(11):
        for j in range(6):
            k = i
            # 지금 보는 좌표에 뿌요가 있고, 그 밑의 행이 비어있을 때 까지 반복해서 실행
            while k >= 0 and board[k][j] != '.' and board[k + 1][j] == '.':
                # 밑에 칸에 뿌요를 이동시키고, 원래 칸은 빈칸으로 만들기
                board[k + 1][j], board[k][j] = board[k][j], board[k + 1][j]
                # 위칸이 연쇄적으로 내려올 수 있도록 k를 하나 빼줌
                k -= 1


# 뿌요가 터지는 함수
def pop(loc):
    for x, y in loc:
        board[x][y] = '.'


board = [list(input().rstrip()) for _ in range(12)]
ans = 0

while True:
    is_popped = False  # 뿌요를 터뜨릴 수 있는 지 확인하는 변수
    vis = [[False] * 6 for _ in range(12)]  # 방문 여부 확인하기 위한 리스트

    for i in range(12):
        for j in range(6):
            # 뿌요가 있으면 상하좌우로 이어져있는 같은 뿌요의 좌표 얻기
            if board[i][j] != '.' and not vis[i][j]:
                puyos_loc = bfs(i, j)

                # 같은 종류 뿌요가 4개 이상 있으면 터뜨리기
                if len(puyos_loc) >= 4:
                    is_popped = True  # 뿌요 터뜨리기 가능
                    pop(puyos_loc)

    # 터뜨린 후에는 뿌요들을 중력으로 떨어뜨린 후, 연쇄횟수 추가하기
    if is_popped:
        gravitate()
        ans += 1
    # 터뜨릴 뿌요 없으면 종료
    else:
        break

print(ans)
