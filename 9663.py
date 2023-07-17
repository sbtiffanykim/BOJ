n = int(input())
# 퀸의 이동 경로에 있는 다른 퀸 저장
straight = [False] * n
horizontal1 = [False] * (2 * n)
horizontal2 = [False] * (2 * n)

cnt = 0  # 경우의 수 저장


def search(k):  # k번째 row에 퀸 배치
    global cnt
    if k == n:  # n개 다 놓는 데에 성공한 경우
        cnt += 1
        return

    for i in range(n):  # (k, i)에 퀸 배치
        if straight[i] or horizontal1[k + i] or horizontal2[i - k]:
            continue
        straight[i] = True
        horizontal1[k + i] = True
        horizontal2[i - k] = True
        search(k + 1)
        straight[i] = False
        horizontal1[k + i] = False
        horizontal2[i - k] = False


# (0,0)에 놓는 경우부터 탐색
search(0)
print(cnt)
