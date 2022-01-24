# https://www.acmicpc.net/problem/11047

import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())

    coins = []  # 받는 코인
    minCoins = 0  # 최소로 쓴 코인 갯수 (출력할 변수)

    for _ in range(n):
        coins.append(int(sys.stdin.readline().strip()))

    while k > 0:
        for fromBig in reversed(coins):  # 큰 코인 부터
            if k >= fromBig:  # 코인이 작거나 같으면
                use = k // fromBig  # 몇 개를 사용하는가
                k -= (use * fromBig)  # 사용한 코인만큼 빼주기
                minCoins += use  # 사용 코인 갯수 더하기
                # print("%d원 %d개" % (fromBig, use))

    print(minCoins)
