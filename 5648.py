n, *arr = input().split()

while int(n) > len(arr):
    temp = input().split()
    arr.extend(temp)

res = sorted([int(n[::-1]) for n in arr])
print(*res, sep='\n')
