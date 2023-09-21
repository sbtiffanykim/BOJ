# 1202_보석 도둑

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    heapq.heappush(jewels, tuple(map(int, input().split())))  # 보석별로 (무게, 가격) 으로 최소힙으로 저장
bags = [int(input()) for _ in range(k)]  
bags.sort()  # 가방 최대 무게 오름차순으로 정렬

result = 0  # 최종적으로 담길 보석들 가격 저장할 변수
temp = []  # 보석 담길 과정 저장할 리스트

for bag in bags:  # 각 가방(무게)에 대해
    while jewels and jewels[0][0] <= bag:  # 가방 무게가 허용할 때까지 보석 가격 저장(보석 넣기)를 반복
        heapq.heappush(temp, -jewels[0][1])  # 보석 가격을 최대힙으로 저장
        heapq.heappop(jewels)  # 가격 저장 후에는 보석 제거
    if temp:  # 가방 무게가 허용할 때까지 보석 가격 모두 저장 한 후에눈
        result += (-heapq.heappop(temp))  # 최종적으로 가장 비싼 보석의 가격 저장

print(result)
