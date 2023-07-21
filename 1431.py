n = int(input())
cereals = []

for _ in range(n):
    temp_s = input()
    temp_d = 0
    for c in temp_s:
        if c.isdigit():
            temp_d += int(c)
    cereals.append((temp_d, temp_s))

cereals.sort(key=lambda x: (len(x[1]), x[0], x[1]))

for idx, c in cereals:
    print(c)
