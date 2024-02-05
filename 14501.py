# 14501_퇴사
# https://www.acmicpc.net/problem/14501

import sys

input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]  # (시간, 비용)
dp = [0] * (n + 1)  # i일까지 일했을 때의 최대 수익 저장
max_val = 0  # 최대 수익

for i in range(n - 1, -1, -1):  # 날짜를 거슬러 올라가면서 탐색
    day = i + info[i][0]  # i일에 상담한 후 다음 상담을 할 수 있는 날
    if day <= n:  # 다음 상담이 가능한 날이 n번째 날보다 작은 경우
        dp[i] = max(dp[day] + info[i][1], max_val)
        max_val = dp[i]  # 최대수익 갱신
    else:  # 넘은 경우 현재까지의 최대 수익으로 갱신
        dp[i] = max_val

print(max_val)
