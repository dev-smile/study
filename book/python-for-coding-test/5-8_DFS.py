# 깊이 우선 탐색
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

def dfs(graph, v, visited):
    # 현재 노드 방문
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 2, visited)