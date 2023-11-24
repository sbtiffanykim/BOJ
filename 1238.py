# 1238_파티
# https://www.acmicpc.net/problem/1238

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cost = [[INF] * (n + 1) for _ in range(n + 1)]  # cost[i][j]: i에서 출발 -> j에 도착할 때까지의 최소 비용


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost[start][start] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if cost[start][cur] < dist:
            continue
        for nxt, weight in graph[cur]:
            new_cost = dist + weight
            if cost[start][nxt] > new_cost:
                cost[start][nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n + 1):
    dijkstra(i)

max_val = 0  # 가장 오래걸리는 소요 시간
for i in range(1, n + 1):
    if i == x:
        continue
    time = cost[i][x] + cost[x][i]  # '집 -> x -> 집'의 최소 소요시간 더하기
    max_val = max(max_val, time)  # 가장 큰 소요시간으로 갱신

print(max_val)
