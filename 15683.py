# 15683_감시

import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# cctv 종류와 위치 기록할 배열
cctv = []
# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 cctv가 관찰 가능한 방향
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 3], [1, 2, 3], [0, 2, 3], [0, 1, 2]],
    [[0, 1, 2, 3]],
]
# 최소 사각지대 기록하기 위해 큰 수로 초기화
area = float('inf')


def watch(graph, direction, x, y):
    for d in direction:
        nx = x
        ny = y
        # 멈춤 조건 보기 전까지 계속 감시 진행
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위 넘어가면 감시 못함
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            # 벽 만나면 그 앞 영역은 감시 못함
            if graph[nx][ny] == 6:
                break
            # 감시 가능 영역에 감시 표시
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 7


# cctv마다 회전 가능한 경우 모두 확인
def dfs(graph, depth):
    global area
    # dfs 종료 조건
    if depth == len(cctv):
        cnt = 0
        # 사각지대 영역 계산
        for i in range(n):
            cnt += graph[i].count(0)
        # 더 작은 수로 저장 후 종료
        area = min(area, cnt)
        return

    # 진행방향 기록하기 위해 지도 복사
    dup = copy.deepcopy(graph)
    type, x, y = cctv[depth]
    for cctv_dir in mode[type]:
        # 감시방향 기록
        watch(dup, cctv_dir, x, y)
        # 다음 cctv 살피기
        dfs(dup, depth + 1)
        # 다음 사이클 진행 위해 배열 초기화
        dup = copy.deepcopy(graph)


for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            # cctv의 type, x_cord, y_cord 기록
            cctv.append((board[i][j], i, j))

dfs(board, 0)
print(area)
