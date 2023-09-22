n, m = map(int, input().split())
isused = [False] * n  # 해당 숫자가 사용되었는 지 확인하기 위한 리스트
curr = [0] * m  # 현재 조합을 저장하기 위한 리스트


def search(k):
    # base condition
    if k == m:
        print(*curr, sep=' ')
        return

    for i in range(n):
        if not isused[i]:
            curr[k] = i + 1
            isused[i] = True  # 중복 없이 구하기 위해 숫자 i는 사용했다는 표시를 남김
            search(k + 1)
            isused[i] = False  # k+1번째 숫자 탐색 후에 i 사용했다는 표시 해제


search(0)
