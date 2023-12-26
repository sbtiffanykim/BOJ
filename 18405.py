# 18405_경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스가 퍼지는 과정을 나타내는 함수
def bfs():
    queue = deque(virus)

    while queue:
        virus_num, cur_time, cur_x, cur_y = queue.popleft()

        if cur_time == s:  # s초가 지나면 종료
            break

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = virus_num
                queue.append((virus_num, cur_time + 1, nx, ny))


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = list()
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            virus.append((board[i][j], 0, i, j))  # (바이러스 번호, 현재 시간, x좌표, y좌표) 저장

virus.sort()  # 바이러스 번호 순서대로 정렬
bfs()  # 바이러스 감염

print(board[x - 1][y - 1])  # 정답 출력
