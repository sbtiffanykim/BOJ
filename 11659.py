import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    # prefix sum위한 테이블 정의
    d = [0]

    # 누적합 계산을 위한 변수
    temp = 0
    for k in range(n):
        temp += num[k]
        d.append(temp)

    for _ in range(m):
        i, j = map(int, input().split())
        # num[i] + num[i+1] + ... + num[j]
        # = num[1] + num[2] + ... + num[j] - (num[1] + num[2] + ... + num[i-1])
        # = d[j] - d[i-1]
        print(d[j] - d[i - 1])


if __name__ == '__main__':
    main()
