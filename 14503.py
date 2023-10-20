# 14503_로봇 청소기

import sys
from collections import deque

input = sys.stdin.readline

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0  # 청소 횟수 기록하기 위한 변수

while True:
    if board[x][y] == 0:
        board[x][y] = -1  # 청소 완료 표시
        ans += 1  # 청소 횟수 증가

    cleaned = False
    # 주변 상하좌우 4칸 살피기
    for i in range(4):
        d = (d + 3) % 4  # 반시계방향 90도(왼쪽)로 회전
        # 회전 후 한칸 전진한 곳이 청소가 가능한 칸이라면
        if board[x + dx[d]][y + dy[d]] == 0:
            cleaned = True  # 청소 가능한 곳임을 표시
            # 한칸 전진
            x, y = x + dx[d], y + dy[d]
            break

    # 청소 가능하다면 위의 과정 반복
    if cleaned:
        continue
    # 청소 불가능일 때
    # 한 칸 후진한 후 벽이 있다면 청소기 작동 중지
    if board[x - dx[d]][y - dy[d]] == 1:
        break
    # 벽이 없다면 한 칸 후진한 후 위의 과정 다시 진행
    x, y = x - dx[d], y - dy[d]

print(ans)
