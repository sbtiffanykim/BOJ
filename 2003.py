# 2003_수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 누적합 계산을 위한 변수
tot = arr[0]
ans = 0
# 투포인터 변수
st, en = 0, 0

while True:
    if tot < m:
        en += 1
        # 범위 넘어가면 종료
        if en == n:
            break
        tot += arr[en]  
    elif tot > m:
        tot -= arr[st]
        st += 1
    if tot == m:
        ans += 1
        tot -= arr[st]
        st += 1

print(ans)