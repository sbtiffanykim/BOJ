t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))

    idx, cnt = 0, 0

    for i in range(n):
        while True:
            if idx == m or arr1[i] <= arr2[idx]:
                cnt += idx
                break
            else:
                idx += 1

    print(cnt)
