while True:
    n, *nums = map(int, input().split())
    curr = [0] * 6

    if n == 0:
        break

    def compute(k, st):
        if k == 6:
            for i in range(6):
                print(curr[i], end=' ')
            print('')
            return

        for i in range(st, n):
            curr[k] = nums[i]
            compute(k + 1, i + 1)

    compute(0, 0)
    print('')
