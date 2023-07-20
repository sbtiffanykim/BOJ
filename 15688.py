n = int(input())
arr = []
base_idx = 1000000
cnt = [0] * 2000001

while n > 0:
    num = int(input())
    cnt[base_idx + num] += 1
    n -= 1

for i, t in enumerate(cnt):
    for _ in range(t):
        print(i - base_idx)
