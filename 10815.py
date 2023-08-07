import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    # 존재하지 않으면 두 index가 같움
    if bisect_left(arr1, num) == bisect_right(arr1, num):
        print(0, end=' ')
    else:
        print(1, end=' ')
