from collections import defaultdict

cnt = defaultdict(int)
n = int(input())

while n > 0:
    num = int(input())
    cnt[num] += 1
    n -= 1

res = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
print(res[0][0])
