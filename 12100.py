# 12100_2048(Easy)

import sys
from copy import deepcopy

input = sys.stdin.readline


# 보드를 오른쪽으로 90도 회전시키는 함수
def rotate(graph):
    rotated = [[0] * n for _ in range(n)]  # 회전시킨 결과를 저장할 리스트
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = graph[i][j]
    return rotated


# 이동을 수행하는 함수
def move(graph, pos):
    # 왼쪽으로의 이동이 default로, 다른 방향으로의 이동은 보드를 회전해 수행
    new_board = []  # 이동을 끝낸 후 최종 결과를 저장할 리스트
    for _ in range(pos):
        graph = rotate(graph)
    for i in range(n):
        temp_row = [0] * n  # 각 row별로 이동한 후 결과를 담을 리스트
        idx = 0  # 진행 위치를 알려줄 인덱스
        for j in range(n):
            curr = graph[i][j]  # 보드 내에서 현재 보고 있는 숫자
            # 숫자가 없고 빈칸이면 아무런 작업 수행하지 않음
            if curr == 0:
                continue
            # 빈칸이 아닌 경우
            else:
                # 왼쪽으로 갈 칸에 아무 숫자도 없으면 해당 자리에 숫자 넣기
                if temp_row[idx] == 0:
                    temp_row[idx] = curr
                else:
                    # 갈 칸의 숫자가 현재 숫자와 같다면 더해주기
                    if temp_row[idx] == curr:
                        temp_row[idx] *= 2
                        idx += 1  # idx 증가시켜서 다음 칸에 더하기가 진행될 수 있도록 조정
                    # 갈 칸의 숫자가 현재 숫자와 다르다면
                    else:
                        # 그 다음칸에 숫자 넣기
                        idx += 1
                        temp_row[idx] = curr
        # 해당 row에서 모든 작업을 수행했으면 새로운 보드에 결과 저장
        new_board.append(temp_row)
    return new_board


# depth번 동안 게임을 수행하는 함수
def dfs(graph, depth):
    global ans
    # 5번 모두 수행했다면 종료
    if depth == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, graph[i][j])  # 보드 내에 가장 큰 수 저장
        return

    # 각 단계마다 상하좌우 각각 한번씩 이동
    for pos in range(4):
        dup = deepcopy(graph)
        temp_board = move(dup, pos)  # 이동
        dfs(temp_board, depth + 1)  # 다음 단계 게임 진행


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0  # 가장 큰 수를 저장하기 위한 변수

dfs(board, 0)  # 5번 2048 게임 수행
print(ans)
