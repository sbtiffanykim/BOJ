from collections import deque

m, n = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]  # 일수 저장하기 위한 배열
queue = deque()

for i in range(n):
    for j in range(m):
        # 익은 토마토들을 기점으로 bfs 수행 예정
        if tomatoes[i][j] == 1:
            queue.append((i, j))
        # 안 익은 토마토 dist 배열 값 변경
        if tomatoes[i][j] == 0:
            dist[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] >= 0:
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))


def solution():
    ans = 0
    for i in range(n):
        for j in range(m):
            # 안익은 토마토 존재
            if dist[i][j] == -1:
                return -1
            elif dist[i][j] >= 0 and tomatoes[i][j] != -1:
                ans = max(ans, dist[i][j])
    return ans


print(solution())
