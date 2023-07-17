import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = [0] * 3  # -1, 0, 1로 채워진 종이 개수


def cut(x, y, n):
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                k = n // 3
                cut(x, y, k)
                cut(x, y + k, k)
                cut(x, y + 2 * k, k)
                cut(x + k, y, k)
                cut(x + k, y + k, k)
                cut(x + k, y + 2 * k, k)
                cut(x + 2 * k, y, k)
                cut(x + 2 * k, y + k, k)
                cut(x + 2 * k, y + 2 * k, k)
                return

    cnt[color + 1] += 1


cut(0, 0, N)
for c in cnt:
    print(c)
