from collections import deque

n, m = map(int, input().split())
fmap = [[c for c in input()] for _ in range(n)]

q1 = deque()  # 불
q2 = deque()  # 지훈

dist1 = [[-1] * m for _ in range(n)]  # 불
dist2 = [[-1] * m for _ in range(n)]  # 지훈
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if fmap[i][j] == "F":
            q1.append((i, j))
            dist1[i][j] = 0
        if fmap[i][j] == "J":
            q2.append((i, j))
            dist2[i][j] = 0


def bfs():
    # 불에 대한 bfs
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist1[nx][ny] >= 0 or fmap[nx][ny] == "#":
                continue
            dist1[nx][ny] = dist1[x][y] + 1
            q1.append((nx, ny))

    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지훈이가 범위 벗어난 것은 탈출에 성공했다는 것
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                # 마지먹 거리에 +1 해야 탈출할 때의 시점
                return dist2[x][y] + 1
            # 벽이거나 한번 방문했던 경우 무시
            if dist2[nx][ny] >= 0 or fmap[nx][ny] == "#":
                continue
            # dist1에서 -1은 길이라서 지나가야됨
            # 불이 도착하는 시간보다 내가 동시에 가거나 더 늦으면 이동 불가
            # 만약 불이 없는 경우, 길(-1)인데도 두번째 조건에 의해 통과되므로 and 써야함
            if dist1[nx][ny] != -1 and dist1[nx][ny] <= dist2[x][y] + 1:
                continue
            dist2[nx][ny] = dist2[x][y] + 1
            q2.append((nx, ny))
    return "IMPOSSIBLE"


print(bfs())
