n, m = map(int, input().split())
isused = [0] * n
curr = [0] * m


def combination(k):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    st_idx = 1
    if k != 0:
        st_idx = curr[k - 1] + 1

    for i in range(st_idx, n + 1):
        if not isused[i - 1]:
            isused[i - 1] = 1
            curr[k] = i
            combination(k + 1)
            isused[i - 1] = 0


combination(0)
