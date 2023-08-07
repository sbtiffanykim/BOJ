import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


# [x, y] 범위에 있는 숫자 개수를 구하는 함수
def count_by_range(x, y):
    left_idx = bisect_left(arr2, x)
    right_idx = bisect_right(arr2, y)
    return right_idx - left_idx


n, m = map(int, input().split())
# 오름차순으로 답 출력하기 위해 arr1도 정렬
arr1 = sorted(list(map(int, input().split())))
# binary search위해 arr2 정렬
arr2 = sorted(list(map(int, input().split())))
ans = []
for num in arr1:
    # arr1에 있고, arr2에는 존재하지 않는 경우
    if count_by_range(num, num) == 0:
        ans.append(num)

if ans:
    print(len(ans))
    print(*ans, end=' ')
else:
    print(0)
