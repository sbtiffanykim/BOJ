n = int(input())
arr = []

for i in range(n):
    curr = input()
    if curr not in arr:
        arr.append(curr)

arr.sort(key=lambda x: (len(x), x))
print(*arr, sep='\n')
