# 1351_무한 수열

# a의 각 항의 값을 저장하는 dictionary 선언
a = {0: 1}


# dynamic programming 이용
def dp(i):
    # n번째 값이 저장되어있다면 값 반환
    if i in a:
        return a[i]
    # 아니라면 dictionary에 저장된 값 이용해 계산
    else:
        a[i] = dp(i // p) + dp(i // q)
        return a[i]


n, p, q = map(int, (input().split()))
print(dp(n))
