# 18352_특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())
graph = {i: [] for i in range(n + 1)}
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)


# start node에서 각 node까지의 최단 거리를 계산하는 함수
def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        cur_node = queue.popleft()
        for v in graph[cur_node]:
            if dist[v] == -1:  # 방문한 적이 없는 노드인 경우
                dist[v] = dist[cur_node] + 1
                queue.append(v)


dist = [-1] * (n + 1)  # kth vertex까지 가는 최단 거리를 저장
dist[x] = 0  # 출발점의 최단 거리를 0으로 설정

bfs(x)  # x에서 출발해 각 vertex까지의 최단 거리 계산

check = False  # 최단 거리가 k인 도시가 있는 지 확인하는 flag
for i in range(n + 1):
    if dist[i] == k:
        check = True
        print(i, end="\n")

if not check:
    print(-1)
