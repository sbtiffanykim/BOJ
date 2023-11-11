# 21610_마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610

import sys

input = sys.stdin.readline

dx8 = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 1-indexed
dy8 = [0, -1, -1, 0, 1, 1, 1, 0, -1]  # 1-indexed

dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, -1, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = []  # m만큼 이동시킬 때의 방향, 속력 저장

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]  # 초기 비구름 좌표

for i in range(m):
    d, s = map(int, input().split())
    moves.append((d, s))  # 움직임 방향, 속력 저장

# m만큼 반복
for d, s in moves:
    once_cloud = [[False] * n for _ in range(n)]  # 구름이었던 곳 기록하기 위한 리스트
    tmp = []
    # 1. 구름 이동
    for x, y in clouds:
        nx = (x + s * dx8[d]) % n
        ny = (y + s * dy8[d]) % n
        board[nx][ny] += 1  # 2. 옮겨진 구름 위치에 물 1씩 증가
        once_cloud[nx][ny] = True  # 구름 표시
        tmp.append((nx, ny))  # 현재 단계에서 옮겨진 구름 좌표 저장

    # 4. 대각선 방향 체크
    for x, y in tmp:
        buckets = 0  # 대각선 방향에 물이 있는 바구니 개수 저장
        for i in range(4):
            nx = x + dx4[i]
            ny = y + dy4[i]
            # 범위 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 대각선 바구니 수 확인
            if board[nx][ny] > 0:
                buckets += 1
        board[x][y] += buckets  # 바구니 개수 만큼 물 양 증가

    new_clouds = []
    # 5. 구름 생성
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not once_cloud[i][j]:
                new_clouds.append((i, j))  # 새로운 구름의 좌표 저장
                board[i][j] -= 2  # 물의 양 2씩 빼기
    clouds = new_clouds  # 새로운 구름으로 대체

ans = 0
# 바구니에 들어있는 물의 양 합 구하기
for i in range(n):
    ans += sum(board[i])

print(ans)
