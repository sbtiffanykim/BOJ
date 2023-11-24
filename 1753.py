# 1753_최단 경로
# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대 값을 대체하는 값 설정

n, m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)  # 각 노드에 대해 최단 거리 초기화


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (최단 경로, 노드 번호) 저장
    distance[start] = 0  # 시작노드로 가는 최단 경로 0으로 설정
    while q:
        dist, cur = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드 정보 꺼내기
        if dist > distance[cur]:  # 해당 노드가 이미 처리 된 적이 있으면 무시
            continue
        for nxt, weight in graph[cur]:
            new_cost = dist + weight
            if new_cost < distance[nxt]:  # 갱신해야하는 값이 저장되어있는 값보다 더 작은 경우
                distance[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))


for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
