import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ordered_nums = sorted(nums)
# 중복 제거 위한 임시배열
temp = [ordered_nums[0]]

# 중복된 숫자 제거한 배열
for i in range(1, len(ordered_nums)):
    if ordered_nums[i] != ordered_nums[i-1]:
        temp.append(ordered_nums[i])

# nums돌면서 해당 숫자가 temp에서 이분탐색한 결과 반환
for n in nums:
    print(bisect_left(temp, n), end = ' ')
