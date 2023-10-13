# 18808_스티커 붙이기

import sys

input = sys.stdin.readline


# 오른쪽으로 90도 회전하는 함수
def rotate():
    global r, c, sticker
    temp = [[0] * r for _ in range(c)]  # 회전하고 난 후의 모양을 저장하는 리스트
    for i in range(r):
        for j in range(c):
            temp[j][r - i - 1] = sticker[i][j]  # 오른쪽으로 90도 회전
    sticker = temp[:]  # sticker에 회전시킨 모양 저장
    r, c = c, r  # 회전 후 가로-세로가 서로 바뀜


# 모눈 종이에 스티커가 붙을 수 있는 지 판단하는 함수
def is_pastable(x, y):
    for i in range(r):
        for j in range(c):
            # 스티커가 모눈종이의 범위를 벗어나면 붙일 수 없음
            if x + i >= n or y + j >= m:
                return False
            # 붙이고 싶은 자리에 이미 스티커가 붙어있다면 새로운 스티커를 붙일 수 없음
            if sticker[i][j] == 1 and board[x + i][y + j] == 1:
                return False

    # 모눈종이에 빈칸이 있어서 스티커를 붙일 수 있는 경우
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                board[x + i][y + j] = 1
    return True


n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]  # 모눈종이

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    # 0, 90, 180, 270도 돌리면서 스티커를 붙일 수 있는 지 체크
    for rot in range(4):
        paste = False  # 회전 중단을 위한 flag 설정
        for i in range(n - r + 1):
            if paste:
                break
            for j in range(m - c + 1):
                if is_pastable(i, j):
                    paste = True
                    break

        # 정해진 범위의 모눈종이에서 스티커를 붙일 수 있으면 회전 안함
        if paste:
            break

        # 스티커를 붙일 수 없다면 회전
        rotate()

cnt = 0  # 스티커가 붙은 칸 수를 저장하기 위한 변수
# 붙어있는 칸 수 출력
for i in range(n):
    for j in range(m):
        cnt += board[i][j]
print(cnt)
