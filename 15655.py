n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
isused = [0] * n
curr = [0] * m


def compute(k):
    if k == m:
        for i in range(m):
            print(numbers[curr[i]], end=' ')
        print('')
        return

    st = 1
    if k != 0:
        st = curr[k - 1] + 1

    for i in range(st, n + 1):
        if not isused[i - 1]:
            isused[i - 1] = 1
            curr[k] = i - 1
            compute(k + 1)
            isused[i - 1] = 0


compute(0)
