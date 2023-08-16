# 9375_패션왕 신해빈

from collections import Counter

t = int(input())
for _ in range(t):
    clothes = Counter()
    cnt = 1

    n = int(input())
    for _ in range(n):
        _, c_type = input().split()
        clothes[c_type] += 1

    for c_type in clothes:
        # 각 옷 종류 당 입어도 되고 안 입어도 되므로, 안 입어도 되는 케이스를 고려하기 위해 1을 더함
        cnt = cnt * (clothes[c_type] + 1)
    # 아무것도 입지 않고 있는 케이스 한 개를 제외
    cnt -= 1
    print(cnt)
