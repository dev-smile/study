# https://www.acmicpc.net/problem/2531

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, d, k, c = map(int, input().rstrip().split())
    dish = []
    for _ in range(N):
        dish.append(int(input().rstrip()))

    maxSushi = 0

    for i in range(N):
        if i+k < N+1:
            temp = dish[i:i+k]+[c]
            temp = list(set(temp))
            if len(temp) > maxSushi:
                maxSushi = len(temp)
        else:
            temp = dish[i:N]+dish[:i+k-N]+[c]
            temp = list(set(temp))
            if len(temp) > maxSushi:
                maxSushi = len(temp)

    print(maxSushi)
