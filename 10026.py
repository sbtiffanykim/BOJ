# 10026_적록색약

import sys
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 같은 구역 내에 좌표들을 탐색하는 함수
def bfs(x, y, board):
    queue = deque()  # bfs탐색을 위한 큐
    queue.append((x, y, board[x][y]))  # 그 전 좌표의 색깔과 비교 위해 색깔도 큐에 함께 넣음
    board[x][y] = '#'  # 큐에 넣은 좌표 방문 표시
    while queue:
        x, y, prev_color = queue.popleft()
        for i in range(4):  # 현재 좌표에서 동서남북 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 탐색할 좌표가 범위를 넘어 서면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 이미 방문한 좌표라면 탐색에서 제외
            # 다음 좌표에서의 색깔이 그 전 좌표의 색깔과 다르다면 같은 구역이 될 수 없으므로 무시
            if board[nx][ny] == '#' or board[nx][ny] != prev_color:
                continue
            queue.append((nx, ny, board[nx][ny]))  # 같은 구역 내에 있다면 큐에 삽입
            board[nx][ny] = '#'  # 방문 표시


input = sys.stdin.readline

n = int(input())
# 정상인 사람이 보는 그림
board1 = [[*input().rstrip()] for _ in range(n)]
# 적록색맹인 사람이 보는 그림
board2 = deepcopy(board1)
for i in range(n):
    for j in range(n):
        # 적록색맹인 사람은 G와 R을 구분하지 못함
        if board2[i][j] == 'G':
            board2[i][j] = 'R'

area1 = 0  # 정상인 사람이 구분하는 구역
area2 = 0  # 적록색맹인 사람이 구분하는 구역

for i in range(n):
    for j in range(n):
        # 방문한 적이 없는 좌표라면 bfs로 같은 구역 탐색
        if board1[i][j] != '#':
            bfs(i, j, board1)
            # 같은 구역 탐색이 모두 끝났으므로 구역 개수 추가
            area1 += 1

for i in range(n):
    for j in range(n):
        # 방문한 적이 없는 좌표라면 bfs로 같은 구역 탐색
        if board2[i][j] != '#':
            bfs(i, j, board2)
            # 같은 구역 탐색이 모두 끝났으므로 구역 개수 추가
            area2 += 1

print(area1, area2)
