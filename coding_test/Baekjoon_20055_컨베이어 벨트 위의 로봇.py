# https://www.acmicpc.net/problem/20055

import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    A = deque(list(map(int, input().rstrip().split())))
    robots = deque([False] * (N*2))
    step = 0

    while A.count(0) < K:
        A.rotate(1)
        robots.rotate(1)
        if robots[N-1] == True:
            robots[N-1] = False
        for i in range(N-2, 0, -1):
            # 로봇이 있는데 다음에 로봇이 없고 내구도가 남아있을 때
            if robots[i] == True and robots[i+1] == False and A[i+1] > 0 : 
                robots[i] = False
                A[i+1] -= 1
                # 내리는 위치
                if i == N-2:
                    continue
                robots[i+1] = True
            # 로봇이 있는데 내구도가 없을 때 or 다음 자리에 로봇이 있을 때
            elif (robots[i] == True and A[(i+1)%(N*2)] == 0) or (robots[i] == True and robots[i+1] == True) : 
                robots[i] = True # 멈춤

        if A[0] > 0 and robots[0] == False:
            robots[0] = True
            A[0] -= 1

        step += 1
        
    print(step)
