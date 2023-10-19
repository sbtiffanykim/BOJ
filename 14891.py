# 14891_톱니바퀴


# 시계방향 회전
def rotate_c(board):
    temp = [0] * 8
    for i in range(8):
        temp[(i + 1) % 8] = board[i]
    return temp


# 반시계방향 회전
def rotate_cc(board):
    temp = [0] * 8
    for i in range(8):
        if i > 0:
            temp[i - 1] = board[i]
        else:
            temp[7] = board[i]
    return temp


# idx: 번호, direc: 방향 // 회전을 처리하는 함수
def simulate(idx, direc):
    global gears
    dirs = {i: 0 for i in range(4)}  # 각 톱니바퀴의 회전 방향을 저장하는 dict
    dirs[idx] = direc
    # 오른쪽으로 회전 전파
    while idx < 3 and (gears[idx][2] != gears[idx + 1][6]):  # 서로 맞닿은 극이 다르면 계속 회전
        dirs[idx + 1] = -dirs[idx]  # 반대방향으로 회전
        idx += 1

    # 왼쪽으로 회전 전파
    while idx > 0 and (gears[idx][6] != gears[idx - 1][2]):  # 서로 맞닿은 극이 다르면 계속 회전
        dirs[idx - 1] = -dirs[idx]  # 반대방향으로 회전
        idx -= 1

    # 각 톱니바퀴를 회전
    for i in range(4):
        if dirs[i] == 1:
            gears[i] = rotate_c(gears[i])
        elif dirs[i] == -1:
            gears[i] = rotate_cc(gears[i])


gears = [list(map(int, [*input()])) for _ in range(4)]
k = int(input())
for _ in range(k):
    idx, direc = map(int, input().split())
    simulate(idx - 1, direc)

# 점수 계산
points = 0
for i in range(len(gears)):
    if gears[i][0] != 0:
        points += 2**i

print(points)
