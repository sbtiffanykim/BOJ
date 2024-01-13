# 11404_플로이드
# https://www.acmicpc.net/problem/11404

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 도시 a에서 b로 가는 비용 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:  # 시작 도시와 도착 도시가 같은 경우
            graph[i][j] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:  # a에서 b로 가는 여러 노선 중 최소 비용을 저장
        graph[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  # floyd-warshall 구현

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:  # 도시 i에서 j로 갈 수 없는 경우 0 출력
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
