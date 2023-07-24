import sys

input = sys.stdin.readline

n = int(input())
d = list()

for _ in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 오른쪽 바깥쪽에 있으면 그 윗 레벨의 가장 오른쪽 값을 더하기
        if j == i:
            d[i][j] += d[i - 1][j - 1]
        # 왼쪽 바깥쪽에 있으면 그 윗 레벨의 가장 왼쪽 값을 더하기
        elif j == 0:
            d[i][j] += d[i - 1][0]
        # 그 이외 경우 그 윗 레벨의 왼쪽 / 오른쪽 값 중 큰 것을 더하기
        else:
            d[i][j] += max(d[i - 1][j - 1], d[i - 1][j])

# 마지막 레벨에서 가장 큰 값이 정답
print(max(d[n - 1]))
