from collections import deque

F, S, G, U, D = map(int, input().split())
dist = [-1] * (F + 1)


def bfs(S):
    queue = deque()
    queue.append((S))
    dist[S] = 0

    while queue:
        curr = queue.popleft()
        for nxt in [curr + U, curr - D]:
            if nxt <= 0 or nxt > F:
                continue
            if dist[nxt] != -1:
                continue
            if nxt == G:
                return dist[curr] + 1
            dist[nxt] = dist[curr] + 1
            queue.append(nxt)

    return 'use the stairs'


if S == G:
    print(0)
else:
    print(bfs(S))
