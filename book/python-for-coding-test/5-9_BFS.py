# 너비 우선 탐색
# 가까운 노드부터 탐색하는 알고리즘

from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # print('queue : ', queue)
        # 큐에서 원소 하나 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결되어 있고 아직 방문하지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],  # 1
    [1, 7],     # 2
    [1, 4, 5],  # 3
    [3, 5],     # 4
    [3, 4],     # 5
    [7],        # 6
    [2, 6, 8],  # 7
    [1, 7]      # 8
]

visited = [False] * 9

bfs(graph, 1, visited)