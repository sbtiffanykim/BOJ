import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = [0] * 2


def cut(x, y, n):
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                k = n // 2
                cut(x, y, k)  # 1st quadrant
                cut(x, y + k, k)  # 2nd quadrant
                cut(x + k, y, k)  # 3rd quadrant
                cut(x + k, y + k, k)  # 4th quadrant
                return

    if color == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


cut(0, 0, N)
for c in cnt:
    print(c)
