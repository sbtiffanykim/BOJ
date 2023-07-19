from collections import deque

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 1
    area = 0

    while queue:
        x, y = queue.popleft()
        # 흰 구간마다 넓이 증가시킴
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != 0:
                continue
            board[nx][ny] = 1
            queue.append((nx, ny))

    return area


# 직사각형 페인트하기
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            # bfs로 탐색하지 못하게 -1 처리
            board[i][j] = -1

res = []
for i in range(n):
    for j in range(m):
        # 방문한 적이 없고, 직사각형이 아닌 경우 -> 분리된 구획의 시작
        if board[i][j] == 0:
            res.append(bfs(i, j))

res.sort()
print(len(res))
print(*res, sep=' ')
