# 15686_치킨 배달

from itertools import combinations


# 두 좌표 사이의 거리를 구하는 함수
def calc_distance(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# 선택한 m개의 치킨집에 대한 도시 치킨거리를 구하는 함수
def simulate(candidates):
    dist = [10000] * len(home_loc)  # 각 집의 최소 치킨거리를 저장할 리스트
    # 각 집마다
    for idx, home in enumerate(home_loc):
        # 치킨거리가 가장 짧은 치킨집 찾기
        for cand in candidates:
            temp_dist = calc_distance(chicken_loc[cand][0], home[0], chicken_loc[cand][1], home[1])
            if temp_dist < dist[idx]:
                dist[idx] = temp_dist
    # 계산한 도시 치킨거리 반환
    return sum(dist)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
home_loc = []  # 집들의 위치정보를 저장하는 리스트
chicken_loc = []  # 치킨집들의 위치정보를 저장하는 리스트
min_dist = int(1e9)  # 도시 치킨거리 최솟값을 저장할 변수

# 치킨집과 집의 위치 좌표를 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home_loc.append((i, j))
        elif board[i][j] == 2:
            chicken_loc.append((i, j))

# 최대 m개의 치킨집 조합 구하기
cand = list(combinations([i for i in range(len(chicken_loc))], m))

# 각 조합마다 실행
for c in cand:
    # 총 도시의 치킨거리 구하기
    temp_dist = simulate(c)
    # 최솟값 갱신
    if temp_dist < min_dist:
        min_dist = temp_dist

print(min_dist)  # 정답 출력
