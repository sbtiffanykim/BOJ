# 7662_이중 우선순위 큐

import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = list()
    max_heap = list()
    visited = [False] * k

    for i in range(k):
        oper, val = input().split()
        num = int(val)

        # 삽입
        if oper == 'I':
            visited[i] = True
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))

        # 최댓값 삭제
        elif num == 1:
            # min_heap에서 이미 지워진 값이 있다면
            while max_heap and not visited[max_heap[0][1]]:
                # max_heap에서도 지워주기
                heapq.heappop(max_heap)
            # max_heap에 값이 아직 남아있고, min_heap에서도 지워지지 않은 값(최대)이라면
            if max_heap:
                # 삭제표시 해주고 max_heap에서 지우기
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        # 최솟값 삭제
        else:
            # max_heap에서 이미 지워진 값이 있다면
            while min_heap and not visited[min_heap[0][1]]:
                # min_heap에서도 지워주기
                heapq.heappop(min_heap)
            # min_heap에 값이 아직 남아있고, max_heap에서도 지워지지 않은 값(최소)이라면
            if min_heap:
                # 삭제 표시 해주고 min_heap에서도 지우기
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    # 위에서 연산이 끝나도, 각 힙에서 삭제된 원소(visited==false)가 반대 힙에서 남아 있을 수 있음
    # 어느 한 쪽에서라도 삭제된 원소를 각 힙에서 삭제시킴
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap and not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
