# 2295_세 수의 합
import sys
from collections import defaultdict

input = sys.stdin.readline


def check():
    global ans
    # 가장 큰 원소와 가장 작은 원소부터 빼서 확인
    for l in range(n - 1, -1, -1):
        for k in range(l):
            if nums[l] - nums[k] in sums:
                ans = max(nums[l], ans)
    return ans


n = int(input())
nums = sorted([int(input()) for _ in range(n)])
# 주어진 원소들의 합 저장 - 해쉬테이블 사용하기 위해 dict 사용
sums = defaultdict(int)

for i in nums:
    for j in nums:
        sums[i + j] += 1

ans = 0
check()
print(ans)
