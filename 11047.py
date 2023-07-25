n, k = map(int, input().split())
coins = []
ans = 0

for _ in range(n):
    coins.append(int(input()))

# 큰 단위의 동전부터 사용
for i in range(n - 1, -1, -1):
    ans += k // coins[i]
    k %= coins[i]

print(ans)
