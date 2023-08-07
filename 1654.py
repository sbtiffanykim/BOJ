# 1654_랜선 자르기
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lines = sorted([int(input()) for _ in range(k)])


# 길이가 l인 랜선으로 잘랐을 때, n개 이상의 랜선 조각이 나오는 지 확인하는 함수
def check(l):
    tot = 0
    for line in lines:
        tot += line // l
    return tot >= n


# 1부터 N의 최대까지 binary search 진행
st, en = 1, ((2**31) - 1)
while st < en:
    # 균등 분배 위해 st+en에 1을 더해 나눠줌
    mid = (st + en + 1) // 2
    # 랜선의 길이가 mid가 되도록 잘랐을 때 n개 이상의 조각이 나오면
    if check(mid):
        # st를 mid로 변경해 탐색범위 줄임
        st = mid
    # 아니면 mid이상의 길이에서는 n개 이상의 조각이 나올 수 없으므로
    else:
        # en을 mid 앞부분으로 옮겨 탐색범위 줄임
        en = mid - 1

print(st)
