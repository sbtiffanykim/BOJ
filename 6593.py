from collections import deque


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nz < 0 or nz >= l or nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            # 길일 때만 이동 가능
            if dist[nz][nx][ny] != -1:
                continue
            # 출구 도착하면 최단 거리 반환
            if board[nz][nx][ny] == 'E':
                return dist[z][x][y] + 1
            dist[nz][nx][ny] = dist[z][x][y] + 1
            queue.append((nz, nx, ny))
    return False  # 출구 도달 못하면 탈출 못함


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:  # 셋 다 0 나오면 중단
        break
    board = []
    for _ in range(l):
        board.append([[s for s in input()] for _ in range(r)])
        temp = input()  # \n 입력받은 거 무시
    dist = [[[-2] * c for _ in range(r)] for _ in range(l)]
    queue = deque()

    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dz = [-1, 1, 0, 0, 0, 0]

    # 초기화 작업
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    queue.append((i, j, k))
                    dist[i][j][k] = 0  # 최단거리 계산 위해 0으로 초기화
                elif board[i][j][k] == '.' or board[i][j][k] == 'E':
                    dist[i][j][k] = -1  # 지나갈 수 있는 곳을 -1로 초기화

    res = bfs()
    if res:
        print(f'Escaped in {res} minute(s).')
    else:
        print('Trapped!')
