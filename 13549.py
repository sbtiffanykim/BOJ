from collections import deque


def bfs(n):
    queue = deque()
    queue.append(n)

    while queue:
        curr = queue.popleft()
        # 0초 걸리는 순간이동 경우를 먼저 이동
        if curr * 2 <= 100000 and dist[curr * 2] == -1:
            # 0초 걸림
            dist[curr * 2] = dist[curr]
            # +1, -1한 것보다 더 먼저 방문되어야 하므로, appendleft 수행
            queue.appendleft(curr * 2)

        for nxt in [curr - 1, curr + 1]:
            if nxt < 0 or nxt > 100000:
                continue
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[curr] + 1
            queue.append(nxt)

    return dist[k]


if __name__ == '__main__':
    n, k = map(int, input().split())
    # 동생을 찾는 가장 빠른 시간을 구하므로, 수빈이가 (-) 방향으로 가는 경우는 배제
    dist = [-1] * 100001
    dist[n] = 0

    print(bfs(n))
