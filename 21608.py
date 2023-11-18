# 21608_상어 초등학교
# https://www.acmicpc.net/problem/21608

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = [[0] * n for _ in range(n)]  # 학생들이 앉을 자리
inputs = {idx: [] for idx in range(n**2 + 1)}  # 선호학생 저장

for _ in range(n**2):
    s_idx, *nums = map(int, input().split())
    inputs[s_idx] = nums

    cand = [[] for _ in range(5)]  # 전체 후보 좌표 저장
    for x in range(n):
        for y in range(n):
            pref = 0  # 인접칸에 위치한 선호학생 수
            if board[x][y] == 0:  # 빈칸이면 인접칸에 선호학생 있는 지 찾기
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] in inputs[s_idx]:  # 인접하는 칸에 선호하는 학생이 있는 경우
                        pref += 1
                cand[pref].append((x, y))
    # 01. 좋아하는 학생이 가장 많이 인접한 칸 구하기
    new_cand = deque()
    for c_idx in range(4, -1, -1):
        if cand[c_idx]:
            new_cand = deque(cand[c_idx])  # 선호학생이 가장 많이 인접한 칸 좌표 저장
            break

    # 02. 1의 후보칸이 한개만 있을 경우
    if len(new_cand) == 1:
        x, y = new_cand.popleft()
        board[x][y] = s_idx
    # 02. 1이 여러칸 있는 경우
    else:
        next_cand = []
        while new_cand:
            x, y = new_cand.popleft()
            cnt = 0  # 인접칸 중 빈칸 개수
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 0:
                    cnt += 1
            next_cand.append((cnt, x, y))
        # 인접한 빈칸이 많은 순서 -> 행 번호가 작은 순서 -> 열 번호가 작은 순서 대로 정렬
        next_cand = list(sorted(next_cand, key=lambda x: (-x[0], x[1], x[2])))

        # 자리 앉히기
        nx, ny = next_cand[0][1], next_cand[0][2]
        board[nx][ny] = s_idx

pref_sum = 0  # 모든 학생의 선호도 합
# 선호도 계산
for x in range(n):
    for y in range(n):
        st = board[x][y]
        pref = 0  # 인접칸에 선호하는 학생이 몇 명 앉아있는 지 저장
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] in inputs[st]:
                pref += 1
        if pref > 0:
            pref_sum += 10 ** (pref - 1)

print(pref_sum)
