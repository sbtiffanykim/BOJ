from collections import deque

n, k = map(int, input().split())
dist = [-1] * 100001
dist[n] = 0
queue = deque()
queue.append(n)


def bfs():
    while dist[k] == -1:
        curr = queue.popleft()
        for nxt in [curr - 1, curr + 1, curr * 2]:
            if nxt < 0 or nxt > 100000:
                continue
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[curr] + 1
            queue.append(nxt)

    return dist[k]


print(bfs())
