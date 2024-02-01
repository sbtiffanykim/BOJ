# 18428_감시 피하기
# https://www.acmicpc.net/problem/18428

import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs로 선생님이 학생들을 발견할 수 있는 지 확인하는 함수
def search():
    for teacher in teachers:  # 선생님마다 확인
        for i in range(4):  # 상하좌우 탐색
            nx, ny = teacher
            while 0 <= nx < n and 0 <= ny < n:  # 범위 내에서 탐색
                # 학생을 만나면 false 반환하고 종료
                if board[nx][ny] == "S":
                    return False
                # 장애물 만나면 다음 방향 탐색
                if board[nx][ny] == "O":
                    break
                # 진행방향과 같은 방향으로 더 나아가도록 좌표 갱신
                nx += dx[i]
                ny += dy[i]

    return True  # 모든 선생님이 학생 발견하지 못하면 true 반환하고 종료


# 3개의 장애물을 설치하면서 탐색하는 함수
def dfs(depth):
    global flag

    if depth == 3:  # 장애물 3개를 설치
        res = search()
        if res:  # 탐색 성공한 경우
            flag = True
            return
    else:  # backtracking
        for i in range(n):
            for j in range(n):
                if board[i][j] == "X":
                    board[i][j] = "O"
                    dfs(depth + 1)
                    board[i][j] = "X"


n = int(input())
board = [list(input().split()) for _ in range(n)]
teachers = list()
flag = False

for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))

dfs(0)

if flag:
    print("YES")
else:
    print("NO")
