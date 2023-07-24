def main():
    n = int(input())
    d = [0] * (n + 1)

    if n == 1:
        print(1)
        return

    d[1], d[2] = 1, 2

    for k in range(3, n + 1):
        d[k] = d[k - 1] + d[k - 2]

    print(d[n] % 10007)


if __name__ == '__main__':
    main()
