import sys

N = int(sys.stdin.readline())
video = [[int(c) for c in sys.stdin.readline().strip()] for _ in range(N)]
answer = ''


def compress(x, y, n):
    global answer
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != video[x][y]:
                k = n // 2
                answer += '('
                compress(x, y, k)
                compress(x, y + k, k)
                compress(x + k, y, k)
                compress(x + k, y + k, k)
                answer += ')'
                return

    answer += str(video[x][y])


compress(0, 0, N)
print(answer)
