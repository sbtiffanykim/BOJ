# 아래에서 사용하는 모든 list: 1-indexed
n = int(input())
r = [0] * (n + 1)
g = [0] * (n + 1)
b = [0] * (n + 1)

# d[i][0]: i번째 집까지 칠하는 비용 합의 최솟값, i는 빨강색으로 칠함
# d[i][1]: i번째 집까지 칠하는 비용 합의 최솟값, i는 초록색으로 칠함
# d[i][2]: i번째 집까지 칠하는 비용 합의 최솟값, i는 파란색으로 칠함
d = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    r_val, g_val, b_val = map(int, input().split())
    r[i] = r_val
    g[i] = g_val
    b[i] = b_val

d[1][0] = r[1]
d[1][1] = g[1]
d[1][2] = b[1]

for k in range(2, n + 1):
    d[k][0] = min(d[k - 1][1], d[k - 1][2]) + r[k]
    d[k][1] = min(d[k - 1][0], d[k - 1][2]) + g[k]
    d[k][2] = min(d[k - 1][0], d[k - 1][1]) + b[k]

print(min(d[n][0], d[n][1], d[n][2]))
