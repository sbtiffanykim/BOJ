# 1912_연속 합

import sys

input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]

for i in range(1, n):
    # i번째 수까지 더한 값과 i번째 값을 비교해 더 큰 값을 i번째에 갱신해 저장
    # i번째 더한 값이 더 작으면 앞의 수를 더하는 의미가 없음
    nums[i] = max(nums[i], nums[i - 1] + nums[i])

print(max(nums))
