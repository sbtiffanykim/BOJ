# 17140_이차원 배열과 연산
# https://www.acmicpc.net/problem/17140


import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]


# function: operation R
def oper_r():
    size = len(board)
    new_board = [[0 for _ in range(size * 2)] for _ in range(size)]
    max_col_len = 0  # the longest column length
    for i in range(size):
        is_zero = False
        t = Counter(board[i])
        t = sorted(t.items(), key=lambda x: (x[1], x[0]))
        if list(filter(lambda x: x[0] == 0, t)):  # 수를 정렬할 때 0을 무시해야 함
            is_zero = True
        if is_zero:
            max_col_len = max(max_col_len, (len(t) - 1) * 2)
        else:
            max_col_len = max(max_col_len, len(t) * 2)

        idx = 0
        for j in range(size):
            try:
                num, freq = t[j]
                if num == 0:
                    continue
                new_board[i][idx] = num
                new_board[i][idx + 1] = freq
                idx += 2
            except IndexError:
                continue

    size = min(size, 100)
    max_col_len = min(max_col_len, 100)

    # adjust the board length to the longest column length
    new_board = [new_board[i][:max_col_len] for i in range(size)]

    return new_board


# function: operation C
def oper_c():
    size_r, size_c = len(board), len(board[0])
    new_board = [[0 for _ in range(size_c)] for _ in range(2 * size_r)]
    max_row_len = 0  # the longest row lenth
    for c in range(size_c):
        is_zero = False
        tmp = []
        for r in range(size_r):
            tmp.append(board[r][c])
        t = Counter(tmp)
        t = sorted(t.items(), key=lambda x: (x[1], x[0]))
        if list(filter(lambda x: x[0] == 0, t)):
            is_zero = True
        if is_zero:
            max_row_len = max(max_row_len, (len(t) - 1) * 2)
        else:
            max_row_len = max(max_row_len, len(t) * 2)

        idx = 0
        for i in range(size_r):
            try:
                num, freq = t[i][0], t[i][1]
                if num == 0:
                    continue
                new_board[idx][c] = num
                new_board[idx + 1][c] = freq
                idx += 2
            except IndexError:
                continue

    max_row_len = min(max_row_len, 100)

    new_board = [new_board[k] for k in range(max_row_len)]
    return new_board


def simulate():
    global answer, board

    while True:
        try:
            if board[r - 1][c - 1] == k:
                return answer
        except:
            pass
        len_r, len_c = len(board), len(board[0])
        if len_r >= len_c:
            board = oper_r()
        elif len_r < len_c:
            board = oper_c()
        answer += 1

        if answer > 100:
            return -1


answer = 0
print(simulate())
