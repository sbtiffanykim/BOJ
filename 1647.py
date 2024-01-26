# 1647_도시 분할 계획
# https://www.acmicpc.net/problem/1647


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
roads = list()  # 모든 길의 정보 저장
parent = [i for i in range(n + 1)]  # 부모 테이블 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))


roads.sort()  # 유지비 오름차순 정렬
total_cost = 0  # 유지비 합 저장을 위한 변수
largest_cost = 0  # 가장 큰 유지비 저장을 위한 변수


# minimum spanning tree 찾기
for cost, a, b in roads:
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 발생하지 않는 경우
        union_parent(parent, a, b)
        total_cost += cost
        largest_cost = cost  # 오름차순 정렬이라 가장 마지막 cost가 가장 큰 유지비

print(total_cost - largest_cost)  # 그 중에 가장 큰 유지비를 가진 길 없애기
