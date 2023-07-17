n, m = map(int, input().split())
isused = [False] * n  # 해당 숫자가 사용되었는지 확인하기 위함
curr = [0] * m


def permutation(k):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    for i in range(n):
        if not isused[i]:
            curr[k] = i + 1
            isused[i] = True
            permutation(k + 1)
            isused[i] = False


permutation(0)
