# 11286_절댓값 힙

import sys
import heapq

input = sys.stdin.readline

nums = []  # 숫자 저장을 위한 리스트
n = int(input())

for _ in range(n):
    num = int(input())
    if num != 0:  # 입력한 정수가 0이 아닌 경우
        heapq.heappush(nums, (abs(num), num))  # (절댓값, 입력받은 정수) 순으로 최소힙 구성
    else:  # 입력한 정수가 0일 경우
        if nums:  # 저장 되어있는 정수가 있다면
            print(heapq.heappop(nums)[1])  # 작은 수부터 출력
        else:
            print(0)
