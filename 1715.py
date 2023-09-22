# 1715_카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

res = 0

if len(cards) == 1:  # 카드묶음이 1개만 있을 경우 비교 필요 없음
    print(res)
else:
    while len(cards) > 1:  # 카드묶음이 1개만 남을 때까지 비교 반복
        temp_1 = heapq.heappop(cards)
        temp_2 = heapq.heappop(cards)
        res += temp_1 + temp_2
        heapq.heappush(cards, temp_1 + temp_2)
    print(res)
