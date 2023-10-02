# 2146_다리 만들기
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 같은 섬 내의 모든 육지를 탐색하는 함수
def find_island(i, j):
    global cnt
    queue = deque()
    queue.append((i, j))
    vis[i][j] = True
    board[i][j] = cnt  # 섬 번호 부여

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재 위치에서 동서남북 방향 좌표 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 입력된 배열 범위 벗어난 좌표는 탐색하지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 육지가 아니거나 이미 방문한 좌표는 탐색하지 않음
            if board[nx][ny] == 0 or vis[nx][ny]:
                continue
            vis[nx][ny] = True  # 방문 여부 체크
            board[nx][ny] = cnt  # 섬 번호 부여
            queue.append((nx, ny))


# 한 섬으로부터 다른 섬까지의 거리를 구하는 함수
def calc_distance(m):
    global answer
    # 각 섬(출발점)에 대해 거리를 저장해야하므로 함수 내부에 dist 리스트를 구현: 전역에 선언하지 않도록 주의!
    dist = [[-1] * n for _ in range(n)]  # 각 섬 사이의 다리의 거리를 기록하기 위한 리스트
    queue = deque()

    for i in range(n):
        for j in range(n):
            # 각 섬에 해당하는 모든 육지로부터 각각 다음 육지까지의 거리를 확인
            if board[i][j] == m:
                queue.append((i, j))
                dist[i][j] = 0  # 거리 늘리기 위한 시작점 설정

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재 좌표에서 동서남북 방향 좌표 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 탐색하지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 다른 섬에 도착하게 되면 최단거리 갱신 후 탐색 종료
            if board[nx][ny] > 0 and board[nx][ny] != m:
                answer = min(answer, dist[x][y])  # 최단 거리 다시 저장
                return
            # 아직 방문하지 않은 바다에 대해 거리 갱신
            if dist[nx][ny] == -1 and board[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]  # 방문 여부 기록하기 위한 리스트
cnt = 1  # 섬 구분 위해 개수를 기록_번호부여하기 위한 변수
answer = sys.maxsize  # 다리의 최단거리를 기록하기 위한 변수

for i in range(n):
    for j in range(n):
        # 방문하지 못한 육지라면
        if board[i][j] == 1 and not vis[i][j]:
            find_island(i, j)
            # 같은 섬 내에 있는 모든 육지를 확인했으므로 섬 개수 증가
            cnt += 1

# 각 섬에 대해 다른 섬 까지의 최단 거리 확인
for i in range(1, cnt):
    calc_distance(i)

# print(board)
print(answer)
