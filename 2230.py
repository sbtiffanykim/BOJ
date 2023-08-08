# 2230_수 고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
# 투 포인터 사용
st, en = 0, 0
# 두 수의 차이를 담을 변수
sub = 2000000001

while True:
    # en이나 st의 범위가 넘어가면 종료
    if en >= n or st >= n:
        break
    # 두 수의 차가 m 미만일 때
    elif nums[en] - nums[st] < m:
        # en을 증가시키면서 값 비교
        en += 1
    # 두 수의 차가 m 이상이 되면
    elif nums[en] - nums[st] >= m:
        # 차가 더 작은 값 갱신
        sub = min(sub, nums[en] - nums[st])
        # en의 뒷부분은 어차피 sub보다 큰 값이 나오므로 en을 키워가면서 확인할 필요가 없음
        # st를 증가시킴
        st += 1

print(sub)