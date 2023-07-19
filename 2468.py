from collections import deque

n = int(input())
board = [[int(s) for s in input().split()] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def paint(t, dist):
    for i in range(n):
        for j in range(n):
            # 주어진 높이보다 작거나 같을 때 침수
            if board[i][j] <= t:
                dist[i][j] = 0
    return dist


def bfs(i, j, dist):
    queue = deque()
    queue.append((i, j))
    dist[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = 1
            queue.append((nx, ny))


# 주어진 지역 내 최대 높이, 최저 높이 갱신 위한 변수
min_h = 101
max_h = 0

for i in range(n):
    for j in range(n):
        min_h = min(min_h, board[i][j])
        max_h = max(max_h, board[i][j])

res = 0  # 안전한 영역 최대 개수 저장 위한 변수

# 최저높이부터 최대 높이까지
for h in range(min_h, max_h + 1):
    # 모든 지역 높이가 같으면 다 잠기거나, 다 잠기지 않거나 두개 경우만 존재
    # 안전지역의 최대 개수: 다 잠기지 않는 경우
    if min_h == max_h:
        res = 1
        break
    dist = [[-1] * n for _ in range(n)]
    cnt = 0
    dist = paint(h, dist)
    for i in range(n):
        for j in range(n):
            # 방문한 적 없고 강수량보다 높은 지역일 경우
            if dist[i][j] == -1 and board[i][j] > h:
                # 새로운 영역 시작
                cnt += 1
                bfs(i, j, dist)
    res = max(res, cnt)

print(res)
