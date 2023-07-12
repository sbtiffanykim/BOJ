from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([int(c)for c in input()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동할 수 없는 칸 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문한 칸만 이동
            if graph[nx][ny] == 1:
                # 이후 최단거리 갱신
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))