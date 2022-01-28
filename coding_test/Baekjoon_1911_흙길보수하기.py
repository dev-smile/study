# https://www.acmicpc.net/problem/1911

import sys
import math
customInput = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, customInput().split())
    puddle = []

    count = 0
    boardEnd = 0

    for _ in range(N):
        puddle.append(list(map(int, customInput().split())))
    puddle = sorted(puddle)

    for s, e in puddle:
        if boardEnd >= s:  # 시작점이 널빤지의 마지막보다 앞이라면
            s = boardEnd + 1  # 시작점을 널빤지의 마지막 + 1
            if s > e:  # 그랬는데 끝점이 시작점 보다 앞이라면
                continue

        boardCnt = math.ceil((e-s)/L)  # 사용한 널빤지 갯수
        boardEnd = s + (boardCnt * L) - 1  # 널빤지 끝 위치
        count += boardCnt  # 총 사용 널빤지 갯수

    print(count)
