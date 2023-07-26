n = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = list(map(int, input().split()))

ans = 0

# arr1 작은 수 * arr2 큰 수
for k in range(n):
    max_val = max(arr2)
    arr2.pop(arr2.index(max_val))
    ans += arr1[k] * max_val

print(ans)
