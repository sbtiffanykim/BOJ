n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
curr = [0] * m


def compute(k):
    if k == m:
        for i in range(m):
            print(numbers[curr[i]], end=' ')
        print('')
        return

    for i in range(n):
        curr[k] = i
        compute(k + 1)


compute(0)
