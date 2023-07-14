def func(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    # 1
    if r < half and c < half:
        return func(n - 1, r, c)
    # 2
    if r < half and c >= half:
        return half * half + func(n - 1, r, c - half)
    # 3
    if r >= half and c < half:
        return 2 * half * half + func(n - 1, r - half, c)
    # 4
    return 3 * half * half + func(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(func(n, r, c))
