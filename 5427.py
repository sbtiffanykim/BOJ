from collections import deque

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    board = [[c for c in input()] for _ in range(n)]
    dist1 = [[-1] * m for _ in range(n)]
    dist2 = [[-1] * m for _ in range(n)]
    q1 = deque()
    q2 = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == "*":
                dist1[i][j] = 0
                q1.append((i, j))
            if board[i][j] == "@":
                dist2[i][j] = 0
                q2.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        while q1:
            x, y = q1.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny] == "#":
                    continue
                if dist1[nx][ny] != -1:
                    continue
                dist1[nx][ny] = dist1[x][y] + 1
                q1.append((nx, ny))

        while q2:
            x, y = q2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 탈출 성공
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    return dist2[x][y] + 1
                if board[nx][ny] == "#":
                    continue
                if dist2[nx][ny] != -1 or dist1[nx][ny] <= dist2[x][y] + 1:
                    continue
                dist2[nx][ny] = dist2[x][y] + 1
                q2.append((nx, ny))

        return "IMPOSSIBLE"

    print(bfs())
