# https://www.acmicpc.net/problem/19236

# pm 1:34 시작
# pm 2:36 못품 (알고리즘 확인 https://jjangsungwon.tistory.com/54)
# pm 4:10 완료

import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def food(fishes, fishMoveNum, x, y):  # 상어가 먹을 수 있는 후보 위치 반환
    positions = []
    direction = fishMoveNum[x][y]
    for _ in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= fishes[nx][ny] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions


# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(fishes, index):
    for i in range(4):
        for j in range(4):
            if fishes[i][j] == index:
                return (i, j)
    return None


def move_fish(fishes, fishMoveNum, now_x, now_y):  # 물고기 이동
    position = []
    for i in range(1, 17):
        position = find_fish(fishes, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        dir = fishMoveNum[x][y]  # 방향
        for _ in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y):  # 공간의 경계, 상어 있는 칸 확인
                    # 값 교체
                    fishes[x][y], fishes[nx][ny] = fishes[nx][ny], fishes[x][y]
                    fishMoveNum[x][y], fishMoveNum[nx][ny] = fishMoveNum[nx][ny], dir
                    break
            dir = (dir + 1) % 8 # 반시계방향 45도


def dfs(fishes, fishMoveNum,  x, y, total):
    global answer
    fishes = [item[:] for item in fishes]
    fishMoveNum = [item2[:] for item2 in fishMoveNum]

    # 해당 위치 물고기 먹기
    number = fishes[x][y]
    fishes[x][y] = -1

    # 물고기 이동
    move_fish(fishes, fishMoveNum, x, y)

    # 상어 이동할 수 있는 후보 확인
    result = food(fishes, fishMoveNum, x, y)

    # 해당 먹이 먹는 모든 과정 탐색
    answer = max(answer, total + number)
    for next_x, next_y in result:
        dfs(fishes, fishMoveNum, next_x, next_y, total + number)


if __name__ == "__main__":
    fishes = [] # 물고기 위치
    fishMoveNum = [] # 물고기 방향
    
    for _ in range(4):
        fishTemp = list(map(int, input().rstrip().split()))
        fishes.append([fishTemp[0],fishTemp[2],fishTemp[4],fishTemp[6]])
        fishMoveNum.append([fishTemp[1]-1,fishTemp[3]-1,fishTemp[5]-1,fishTemp[7]-1])

    # dfs 탐색
    answer = 0
    dfs(fishes, fishMoveNum, 0, 0, 0)
    print(answer)


'''
# 혼자 풀던 코드
import sys
input = sys.stdin.readline

fishes = []
fishMoveNum = []
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark = 0
sharkOut = False

def sharkMove(x, y):
    global fishes, fishMoveNum, shark, sharkOut

    if shark != 0:
        # 상어 움직이기
        print(shark)
    fishes[x][y] = 0
    shark = fishMoveNum[x][y]

def fishMove():
    order = 0
    
    while order < 16:
        for i in range(4):
            for j in range(4):
                if fishes[i][j] == order:
                    mx, my = move[fishMove[i][j]-1]
                    if i+mx <= -1 or i+mx >= 4 or j+my <= -1 or j+my >= 4:



if __name__ == "__main__":
    for _ in range(4):
        fishTemp = list(map(int, input().rstrip().split()))
        fishes.append([fishTemp[0],fishTemp[2],fishTemp[4],fishTemp[6]])
        fishMoveNum.append([fishTemp[1],fishTemp[3],fishTemp[5],fishTemp[7]])

    while not sharkOut:
        print(fishes, fishMove)
        sharkOut = True
'''