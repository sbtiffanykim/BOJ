import sys

input = sys.stdin.readline


def main():
    n = int(input())
    d = [0] * 1001

    d[1], d[2] = 1, 3

    if n <= 2:
        print(d[n])
        return

    for k in range(3, n + 1):
        d[k] = (d[k - 2] + d[k - 2] + d[k - 1]) % 10007

    print(d[n])


if __name__ == '__main__':
    main()
