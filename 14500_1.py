# 14500_테트로미노
# DFS 이용

import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 테트로미노를 놓는 탐색 과정을 수행하는 함수
def dfs(x, y, length, temp):
    global answer

    # 나머지 놓을 곳이 모두 최댓값이라고 가정해도 현재 더한 값보다 작다면 탐색 안하고 조기 종료
    if answer >= temp + max_val * (4 - length):
        return

    # 퍼즐 4개가 다 이어진 경우 탐색 종료
    if length == 4:
        answer = max(answer, temp)  # 최댓값 갱신
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        # t자형 블록 만들기 위해 기준점 고정
        if length == 2:
            visited[nx][ny] = True  # 길이 3 지점 방문 처리
            dfs(x, y, length + 1, temp + board[nx][ny])  # 길이 2 지점에서 탐색해 길이 4 탐색
            visited[nx][ny] = False
        # 다른 블록
        visited[nx][ny] = True
        dfs(nx, ny, length + 1, temp + board[nx][ny])
        visited[nx][ny] = False
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    answer = 0
    max_val = max(map(max, board))  # 보드 내에 가장 큰 값

    for i in range(n):
        for j in range(m):
            visited[i][j] = True  # 기준점 설정
            dfs(i, j, 1, board[i][j])  # 테트로미노 놓았을 때 가장 큰 합 구하기
            visited[i][j] = False  # 기준점 해제

    print(answer)
