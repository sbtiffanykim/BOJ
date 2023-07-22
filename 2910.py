def main():
    n, c = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = dict()

    for idx, num in enumerate(nums):
        if num not in cnt:
            # [등장 횟수, 처음 등장한 idx, 숫자]
            cnt[num] = [1, idx, num]
        else:
            # 등장 횟수를 갱신
            cnt[num][0] += 1

    # 등장 횟수는 내림차순, 등장 idx는 오름차순으로 정렬
    frequency = sorted(cnt.values(), key=lambda x: (-x[0], x[1]))

    res = []
    for freq in frequency:
        # 등장 횟수만큼 숫자 넣기
        res += [freq[2]] * freq[0]

    print(*res)


if __name__ == '__main__':
    main()
