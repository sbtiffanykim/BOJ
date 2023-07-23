# 1차원 배열로 memoization


def main():
    n = int(input())
    tot = 0
    steps = [0]  # 1-indexed위해 0번째 dummy값 설정

    # i번째 계단 올라갔을 때 밟지 않을 계단의 합의 최솟값, i번째 계단은 밟지 않음
    d = [0] * (n + 1)  # 1-indexed위해 0번째 dummy값 설정

    for _ in range(n):
        val = int(input())
        steps.append(val)
        tot += val

    # 2번째 이하 계단일 때는 점화식때문에 index error 날수 있으므로 예외처리
    if n <= 2:
        print(tot)
        return

    d[1], d[2], d[3] = steps[1], steps[2], steps[3]

    for k in range(4, n + 1):
        # k번째 계단을 밟지 않을 때, k-2, k-3번째 계단 중 한 개는 밟지 않음
        d[k] = min(d[k - 3], d[k - 2]) + steps[k]

    # 모든 계단에 있는 점수 합에서 밟지 않은 계단 합의 최솟값을 빼야 밟은 계단의 합의 최댓값이 나옴
    # d[n]은 마지막 계단을 밟지 않은 경우의 수
    # 마지막 계단은 무조건 밟아야 하므로, k-1, k-2번째 계단 중 하나는 밟지 않아야 함
    res = tot - min(d[n - 1], d[n - 2])
    print(res)


if __name__ == '__main__':
    main()
