#1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서
#   값이 0이면서 아직 방문하지 않은 지점이 있따면 해당 지점 방문
#2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시
#   진행하면, 연결된 모든 지점을 방문할 수 있다.
#3. 1~2번의 과정을 모든 노드에 반복하여 방문하지 않은 지점의 수를 센다.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().rstrip())))
    
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 종료
        if x <= -1 or x >= N or y <= -1 or y >= M:
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            graph[x][y] = 1
            # 상, 하, 좌, 우 위치 확인
            dfs(x, y - 1) # 상
            dfs(x, y + 1) # 하
            dfs(x - 1, y) # 좌
            dfs(x + 1, y) # 우
            return True
        return False

    # 모든 노드에 음료수 채우기
    result = 0
    for i in range(N):
        for j in range(M):

            if dfs(i,j) == True:
                result += 1

    print(result)
