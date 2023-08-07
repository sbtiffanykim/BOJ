import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
temp = sorted(list(set(nums)))

# nums돌면서 해당 숫자가 temp에서 이분탐색한 결과 반환
for n in nums:
    print(bisect_left(temp, n), end = ' ')
