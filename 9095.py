# 테이블 초기화
d = [0] * 11
# 초기값 설정 후
d[1], d[2], d[3] = 1, 2, 4

# t에 의해 테이블 값이 변하지 않고, t가 11미만의 양수이므로 미리 테이블값을 구해두고 풀기
for i in range(4, 11):
    # 점화식
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
