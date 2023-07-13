from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    # 그래프, 방문기록 셋업
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
        dist[x][y] = -1

    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(i, j):
        queue.append((i, j))
        dist[i][j] = 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 방문했던 적이 있으면 제외
                if dist[nx][ny] >= 0:
                    continue
                dist[nx][ny] = 1
                queue.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            # 배추가 있고 방문기록이 없을 때 새로운 밭이라고 생각
            if graph[i][j] == 1 and dist[i][j] == -1:
                cnt += 1
                bfs(i, j)

    print(cnt)
