import sys

input = sys.stdin.readline

n = int(input())
# d[i] = 1에서 1까지 가는 최소 횟수 저장
d = [0] * (n + 1)
# 경로 복원 위한 리스트
# prev[i]: i번까지 올때까지 바로 전에 거친 숫자를 저장
prev = [0] * (n + 1)

d[1], prev[1] = 0, 0

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    prev[i] = i - 1

    # i가 2로 나누어떨어지는 경우
    # i//2 숫자에서 오는 게 i-1로부터 오는 것보다 더 최소 경로일 때
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        # d[i]와 prev[i] 새로 갱신
        d[i] = d[i // 2] + 1
        prev[i] = i // 2

    # i가 3으로 나누어떨어지는 경우
    # i//3 숫자에서 오는 게 i-1로부터 오는 것보다 더 최소 경로일 때
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        # d[i]와 prev[i] 새로 갱신
        d[i] = d[i // 3] + 1
        prev[i] = i // 3

print(d[n])
cur = n
print(cur, end=' ')
while cur > 1:
    print(prev[cur], end=' ')
    # 거슬러 올라가기 위해 cur 갱신
    cur = prev[cur]
