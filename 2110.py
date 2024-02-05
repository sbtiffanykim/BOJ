# 2110_공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline


ans = 0  # 최대 거리 저장
n, c = map(int, input().split())
locs = [int(input()) for _ in range(n)]
locs.sort()  # 좌표 오름차순으로 정렬

st = 1  # 가장 작은 갭 차이
en = locs[-1] - locs[0]  # 가장 큰 갭 차이

while st <= en:
    cur = locs[0]  # 첫번째 집에는 반드시 공유기 설치
    cnt = 1  # 항상 첫번째 집에는 공유기 설치
    mid = (st + en) // 2  # 가장 인접한 공유기 사이의 거리

    for i in range(1, n):  # 두번째부터 마지막까지
        if locs[i] - cur >= mid:  # mid보다 거리가 더 긴 경우
            cur = locs[i]  # 해당 위치에 공유기 설치
            cnt += 1

    if cnt >= c:  # 설치한 공유기가 c보다 많은 경우
        st = mid + 1
        ans = mid  # 결과 저장

    else:  # 더 적게 설치되는 경우
        en = mid - 1

print(ans)
