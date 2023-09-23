# 9663_N-Queen

import sys

input = sys.stdin.readline
n = int(input())

# 진행방향에 퀸이 놓여 있는 지 아닌 지 저장하는 리스트들
vertical = [False] * n  # column
diagonal_1 = [False] * (2 * n)  # 왼쪽 아래로 가는 대각선 방향
diagonal_2 = [False] * (2 * n)  # 오른쪽 아래로 가는 대각선 방향
cnt = 0  # 경우의 수 저장 위한 변수


# k번째 줄에 퀸을 놓았을 때 다른 퀸을 확인하는 함수
def search(k):
    global cnt
    # 모든 퀸을 놓을 수 있으면
    if k == n:
        # 경우의 수 추가
        cnt += 1
        return
    # (k, i)에 퀸을 놓았을 때
    for i in range(n):
        # 퀸의 진행 방향에 다른 퀸이 있다면 무시
        if vertical[i] or diagonal_1[k + i] or diagonal_2[k - i + n - 1]:
            continue
        # 아니라면 탐색 진행
        vertical[i] = True
        diagonal_1[k + i] = True
        diagonal_2[k - i + n - 1] = True
        search(k + 1)
        # 다음 row까지 탐색 끝났으면 위치 해제
        vertical[i] = False
        diagonal_1[k + i] = False
        diagonal_2[k - i + n - 1] = False


search(0)  # (0, 0)부터 퀸 놓기 시작
print(cnt)
