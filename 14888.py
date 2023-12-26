# 14888_연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

from collections import deque

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최솟값, 최댓값 초기화
min_val = int(1e9)
max_val = -int(1e9)


def dfs(num_of_oper, cur_val):
    global min_val, max_val, add, sub, mul, div
    if num_of_oper == n:  # 연산이 모두 종료된 이후
        min_val = min(min_val, cur_val)  # 최솟값 갱신
        max_val = max(max_val, cur_val)  # 최댓값 갱신
        return

    if add > 0:
        add -= 1
        dfs(num_of_oper + 1, cur_val + nums[num_of_oper])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(num_of_oper + 1, cur_val - nums[num_of_oper])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(num_of_oper + 1, cur_val * nums[num_of_oper])
        mul += 1
    if div > 0:
        div -= 1
        dfs(num_of_oper + 1, int(cur_val / nums[num_of_oper]))
        div += 1
    print(num_of_oper, cur_val)


dfs(1, nums[0])
print(max_val)
print(min_val)
