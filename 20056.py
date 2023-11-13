# 20056_마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056


import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
balls = deque()
for _ in range(M):
    _r, _c, _m, _s, _d = map(int, input().split())
    balls.append((_r - 1, _c - 1, _m, _s, _d))

for _ in range(K):
    # 파이어볼 이동
    while balls:
        x, y, bm, bs, bd = balls.popleft()
        # d방향으로 s만큼 이동
        nx = (x + dx[bd] * bs) % N
        ny = (y + dy[bd] * bs) % N
        board[nx][ny].append((bm, bs, bd))

    # 각 칸에 파이어볼이 2개 이상 있는 지 체크
    for i in range(N):
        for j in range(N):
            # 2개 이상 파이어볼이 있는 칸 -> 4개로 쪼개기
            if len(board[i][j]) > 1:
                new_m, new_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[i][j])
                # 해당 칸의 모든 파이어볼에 대해
                while board[i][j]:
                    bm, bs, bd = board[i][j].pop()
                    new_m += bm  # 질량 합치기
                    new_s += bs  # 속도 합치기
                    if bd % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                new_dir = [1, 3, 5, 7]
                if cnt_odd == cnt or cnt_even == cnt:
                    new_dir = [0, 2, 4, 6]
                if new_m // 5 != 0:  # 질량이 0이 아닌 경우에만
                    for t in range(4):
                        balls.append((i, j, new_m // 5, new_s // cnt, new_dir[t]))
            # 파이어볼이 1개만 있는 칸
            if len(board[i][j]) == 1:
                bm, bs, bd = board[i][j].pop()
                balls.append((i, j, bm, bs, bd))

ans = sum([ball[2] for ball in balls])
print(ans)
