# 문제: https://www.acmicpc.net/problem/1697
# 풀이 과정: https://velog.io/@dev-smile/백준-1697-숨바꼭질
# 풀이 참고: https://wook-2124.tistory.com/273

from collections import deque  # deque


def bfs():
    q = deque()  # deque는 양쪽에서 입출력 가능
    q.append(n)  # q = deque([5])
    while q:
        x = q.popleft()  # 처음 시작점은 x = 5, q = deque([])
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):  # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)  # q = deque([4, 6, "10"])


if __name__ == "__main__":
    MAX = 10**5  # 제한 조건
    dist = [0] * (MAX + 1)  # 이동 거리 리스트
    n, k = map(int, input().split())

    bfs()
