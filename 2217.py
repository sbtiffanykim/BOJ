import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

ans = 0
for i in range(1, n + 1):
    # 높은 무게를 들 수 있는 로프(뒤에서)부터 한 개싹 늘려가면서 선택
    # 고른 로프 중 작은 무게 * 로프 개수
    ans = max(ans, arr[n - i] * i)

print(ans)
