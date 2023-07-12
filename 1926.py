from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

mx = 0 # 최대 넓이
cnt = 0 # 그림 개수

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    # 현재 그림 면적
    area = 0
    
    while queue:
        x, y = queue.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 그림 아니거나 이미 방문했어도 무시
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    
    return area

for i in range(n):
    for j in range(m):
        # 0이나 이미 방문한 곳은 새로운 그림 시작이 될 수 없음
        if graph[i][j] == 0 or visited[i][j]:
            continue
        # 새로운 그림 시작
        cnt += 1
        curr_area = bfs(i, j)
        mx = max(curr_area, mx)

print(cnt)
print(mx)
        
        