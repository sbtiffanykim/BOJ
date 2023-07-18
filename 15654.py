n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
isused = {num: 0 for num in numbers}
curr = [0] * m


def compute(k):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    for i in numbers:
        if not isused[i]:
            isused[i] = 1
            curr[k] = i
            compute(k + 1)
            isused[i] = 0


compute(0)
