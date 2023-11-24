# 11779_최소비용 구하기 2
# https://www.acmicpc.net/problem/11779

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
cost = [INF] * (n + 1)
move = [0] * (n + 1)  # 경로 역추적을 위한 리스트

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

departure, destination = map(int, input().split())


def dijkstra(start):
    global route
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if cost[cur] < dist:
            continue
        for nxt, weight in graph[cur]:
            new_cost = dist + weight
            if cost[nxt] > new_cost:
                cost[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
                move[nxt] = cur  # nxt에 도달했을 때 최소비용이 되기 위해 거친 노드(cur) 저장
        if cur == destination:  # 힙에서 꺼낸 노드의 비용 최소값은 다음 반복에서 갱신되지 않음
            break


dijkstra(departure)  # 최소 비용 탐색

route = []  # 경로 거꾸로 추적
idx = destination
while idx:
    route.append(idx)
    idx = move[idx]  # idx로 오기 바로 전 노드

print(cost[destination])  # 도착 도시까지 가는데 드는 최소 비용
print(len(route))  # 경로에 포함된 도시 개수
print(*route[::-1], sep=" ")  # 경로에 포함된 도시
