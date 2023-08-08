# 1806_부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
st, en = 0, 0
cnt = 10 ** 6
tot = nums[0]

while True:
    if tot >= s:
        tot -= nums[st]
        cnt = min(cnt, en - st + 1)
        st += 1
    else:
        en += 1
        if en == n:
            break
        tot += nums[en]

print(0) if cnt == 10 **6 else print(cnt)