from collections import deque

m, n, h = map(int, input().split())
# 3차원 배열
board = [[[int(x) for x in input().split()] for _ in range(n)] for _ in range(h)]
dist = [[[0] * m for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익은 토마토를 기점으로 bfs 돌리기
            if board[i][j][k] == 1:
                queue.append((i, j, k))
            # 익지 않은 토마토 값 초기화
            if board[i][j][k] == 0:
                dist[i][j][k] = -1

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
answer = 0


def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 토마토가 없거나 이미 방문한 곳은 제외
            if dist[nz][nx][ny] >= 0:
                continue
            dist[nz][nx][ny] = dist[z][x][y] + 1
            queue.append((nz, nx, ny))


def search():
    global answer
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if dist[i][j][k] == -1:
                    return -1
                elif board[i][j][k] != -1 and dist[i][j][k] >= 0:
                    answer = max(answer, dist[i][j][k])
    return answer


bfs()
print(search())
