from collections import deque

T = int(input())

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] > 0:
                continue
            if nx == dst_x and ny == dst_y:
                return dist[x][y] + 1
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))


for _ in range(T):
    n = m = int(input())
    dist = [[0] * m for _ in range(n)]
    curr_x, curr_y = map(int, input().split())
    dst_x, dst_y = map(int, input().split())
    if (curr_x, curr_y) == (dst_x, dst_y):
        print(0)
    else:
        print(bfs(curr_x, curr_y))
