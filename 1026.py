n = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for k in range(n):
    ans += arr1[k] * arr2[k]

print(ans)
