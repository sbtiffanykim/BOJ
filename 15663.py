n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
isused = [0] * n
curr = [0] * m


def compute(k):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    temp = 0  # 중복숫자 확인 위한 변수
    for i in range(n):
        if not isused[i] and temp != nums[i]:
            isused[i] = 1
            curr[k] = nums[i]
            temp = curr[k]
            compute(k + 1)
            isused[i] = 0


compute(0)
