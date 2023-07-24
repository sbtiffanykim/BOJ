# d[i][j] = fibonacci(i)를 실행했을 때 fibonacci(j)가 호출되는 횟수
# j는 0 또는 1
d = [[0] * 2 for _ in range(41)]
d[0][0], d[0][1] = 1, 0
d[1][0], d[1][1] = 0, 1

# 주어지는 N이 0~40까지의 작은 수이므로 미리 저장
for k in range(2, 41):
    d[k][0] = d[k - 1][0] + d[k - 2][0]
    d[k][1] = d[k - 1][1] + d[k - 2][1]


t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n][0], d[n][1])
