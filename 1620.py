# 1620_나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())
characters = dict()
numbers = dict()

for i in range(1, n + 1):
    temp = input()
    characters[i] = temp
    numbers[temp] = i

for _ in range(m):
    val = input()
    if val.isdigit():
        print(characters[int(val)])
    else:
        print(numbers[val])
