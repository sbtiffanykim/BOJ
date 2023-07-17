n, m = map(int, input().split())
curr = [0] * m


def compute(k):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    st = 1
    if k != 0:
        st = curr[k - 1]

    for i in range(st, n + 1):
        curr[k] = i
        compute(k + 1)


compute(0)
