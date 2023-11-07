# 2206_벽 부수고 이동하기
import sys

input = sys.stdin.readline


def bfs():
    # dist[i][j][0]: 벽을 하나도 부수지 않고 (i, j)까지 오는 데 걸리는 시간
    # dist[i][j][1]: 벽을 하나만 부수고 (i, j)까지 오는 데 걸리는 시간
    dist = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    dist[0][0][0] = dist[0][0][1] = 1
    queue.append((0, 0, 0))  # (x, y, 벽 부수지 않음) 으로 시작
    while queue:
        x, y, broken = queue.popleft()
        # (N, M)에 도달한 경우 저장된 거리를 반환
        if x == n - 1 and y == m - 1:
            return dist[x][y][broken]
        nxt_dist = dist[x][y][broken] + 1  # 지금까지의 거리에 1을 더한 변수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어났다면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 방문한 적이 없는 이동 가능한 칸인 경우
            if dist[nx][ny][broken] == -1 and board[nx][ny] == 0:
                dist[nx][ny][broken] = nxt_dist
                queue.append((nx, ny, broken))
            # nx, ny를 부숴야 하는 경우
            if broken != 1 and dist[nx][ny][1] == -1 and board[nx][ny] == 1:
                dist[nx][ny][1] = nxt_dist
                queue.append((nx, ny, 1))
    # 탈출할 수 없는 경우
    return -1


n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]

print(bfs())
