# 문제 : https://www.acmicpc.net/problem/1074
# 코드 참고 : https://donggoolosori.github.io/2020/09/22/boj-1074-Z/

import sys
input = sys.stdin.readline

def getz(x, y, size):
    global N, r, c, ans
    if x == c and y == r:
        print(int(ans))
        return

    # r, c가 현재 사분면에 존재한다면
    if y + size > r >= y and x + size > c >= x:
        # 1사분면 탐색
        getz(x, y, size/2)
        # 없으면 2사분면 탐색
        getz(x + size / 2, y, size / 2)
        # 없으면 3사분면 탐색
        getz(x, y + size / 2, size / 2)
        # 없으면 4사분면 탐색
        getz(x + size / 2, y + size / 2, size / 2)

    # r, c가 현재 사분면에 존재하지 않으면 탐색 필요 x
    # ans 에 현재 사분면^2 의 크기를 더해준다.
    else:
        ans += size ** 2

if __name__ == '__main__':
    global N, r, c, ans
    ans = 0
    N, r, c = map(int, input().rstrip().split())
    getz(0, 0, 2 ** N)
