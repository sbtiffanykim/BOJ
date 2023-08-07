import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


# 길이를 x로 잘랐을 때 m명 이상의 조카에게 나누어 줄 수 있는 지 확인하는 함수
def check(x):
    if x == 0:
        return True
    cnt = 0
    for num in arr:
        cnt += num // x
    return cnt >= m


# 나누어 줄 수 없을 때 0을 출력해야 하기 때문에 길이가 1부터라도 st를 0부터 시작
st, en = 0, arr[-1]
while st < en:
    mid = (st + en + 1) // 2
    if check(mid):
        st = mid
    else:
        en = mid - 1

print(st)
