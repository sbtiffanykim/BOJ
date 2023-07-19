from collections import deque

n = int(input())
board = [[int(s) for s in input()] for _ in range(n)]
vis = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    area = 0
    queue = deque()
    queue.append((i, j))
    vis[i][j] = 1

    while queue:
        x, y = queue.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 이미 방문했거나 집이 없는 곳은 무시
            if vis[nx][ny] == 1 or board[nx][ny] == 0:
                continue
            vis[nx][ny] = 1
            queue.append((nx, ny))

    return area


res = []
for i in range(n):
    for j in range(n):
        # 새로운 시작이 되는 집
        if board[i][j] == 1 and vis[i][j] == 0:
            res.append(bfs(i, j))

res.sort()
print(len(res))
print(*res, sep='\n')
