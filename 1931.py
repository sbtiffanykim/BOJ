import sys

input = sys.stdin.readline

n = int(input())
arr = []
# [시작 시점, 종료 시점]
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 현재 시점 t에서 가장 빨리 끝날 수 있는 회의를 먼저 배정
# 회의 시작시간과 끝나는 시간이 같은 경우 때문에 끝나는 시간 -> 시작시간 기준으로 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# t: 현재 시점
t, ans = 0, 0

for i in range(n):
    # 현재시점 t가 후보 회의 시작지점을 지났을 때 회의 배정하지 않음
    if t > arr[i][0]:
        continue
    ans += 1
    # 회의 배정 후 현재시점 t를 배정한 회의 끝나는 시간으로 갱신
    t = arr[i][1]

print(ans)
