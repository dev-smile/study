# https://www.acmicpc.net/problem/14891
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    gears = []
    turn = []

    for _ in range(4):
        gears.append(list(map(int, input().rstrip())))

    for _ in range(int(input().rstrip())):
        turn.append(list(map(int, input().rstrip().split())))

    for n, w in turn:
        move = [0, 0, 0, 0]
        if n == 1:
            move[0] = w
            if gears[0][2] != gears[1][6]:
                move[1] = w * -1
                if gears[1][2] != gears[2][6]:
                    move[2] = w
                    if gears[2][2] != gears[3][6]:
                        move[3] = w * -1
        elif n == 2:
            move[1] = w
            if gears[0][2] != gears[1][6]:
                move[0] = w * -1
            if gears[1][2] != gears[2][6]:
                move[2] = w * -1
                if gears[2][2] != gears[3][6]:
                    move[3] = w
        elif n == 3:
            move[2] = w
            if gears[2][2] != gears[3][6]:
                move[3] = w * -1
            if gears[1][2] != gears[2][6]:
                move[1] = w * -1
                if gears[0][2] != gears[1][6]:
                    move[0] = w
        else:
            move[3] = w
            if gears[2][2] != gears[3][6]:
                move[2] = w * -1
                if gears[1][2] != gears[2][6]:
                    move[1] = w
                    if gears[0][2] != gears[1][6]:
                        move[0] = w * -1
        for i in range(4):
            if move[i] == 1:
                gears[i] = [gears[i][7]] + gears[i][0:7]
            elif move[i] == -1:
                gears[i] = gears[i][1:8] + [gears[i][0]]

    score = gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8
    print(score)

'''
# https://www.acmicpc.net/source/38121331
# 재귀함수 이용
from collections import deque

wheels = [deque(map(int, input())) for _ in range(4)]

def cw(num, dir):
    global wheels
    if num == 4:
        return
    if wheels[num - 1][2] != wheels[num][6]:
        cw(num + 1, -dir)
        wheels[num].rotate(dir)
    else:
        return

def ccw(num, dir):
    global wheels
    if num == -1:
        return
    if wheels[num + 1][6] != wheels[num][2]:
        ccw(num - 1, -dir)
        wheels[num].rotate(dir)
    else:
        return

ans = 0
for _ in range(int(input())):
    wheel, dir = map(int, input().split())
    cw(wheel, -dir)
    ccw(wheel - 2, -dir)
    wheels[wheel - 1].rotate(dir)

for i in range(4):
    ans += (2 ** i) * wheels[i][0]

print(ans)
'''