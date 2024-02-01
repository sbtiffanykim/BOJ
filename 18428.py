# 18428_감시 피하기
# https://www.acmicpc.net/problem/18428

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == "T":  # 선생님이 있는 좌표 큐에 삽입
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            possible = False
            for j in range(1, n):
                nx = x + j * (dx[i])
                ny = y + j * (dy[i])
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == "S":  # 학생을 발견한 경우
                    return False  # 감시 피할 수 없음
                elif board[nx][ny] == "O":
                    possible = True
                    break
            if possible:  # 장애물에 가려져 있으면 다른 선생님으로 넘어감
                break

    return True  # 큐가 빌 때까지 모든 선생님이 학생을 발견할 수 없으면 종료


def search():
    for teacher in teachers:
        x, y = teacher
        for i in range(4):
            for j in range(1, n):
                nx = x + j * dx[i]
                ny = y + j * dy[i]
                # 범위 넘어가면 다음 방향 탐색
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                # 학생을 만나면 false 반환하고 종료
                if board[nx][ny] == "S":
                    return False
                # 장애물 만나면 다음 방향 탐색
                if board[nx][ny] == "O":
                    break

    return True  # 모든 선생님이 학생 발견하지 못하면 true 반환하고 종료


# 탐색
def dfs(idx, depth):
    global flag
    if depth == 3:
        res = search()
        if res:
            flag = True
            return
    else:
        for i in range(idx, len(blank)):  # 백트래킹
            board[blank[i][0]][blank[i][1]] = "O"
            dfs(i + 1, depth + 1)
            board[blank[i][0]][blank[i][1]] = "X"


n = int(input())
board = [list(input().split()) for _ in range(n)]
blank = list()
teachers = list()
flag = False

for i in range(n):
    for j in range(n):
        if board[i][j] == "X":
            blank.append((i, j))
        elif board[i][j] == "T":
            teachers.append((i, j))

dfs(0, 0)
if flag:
    print("YES")
else:
    print("NO")
