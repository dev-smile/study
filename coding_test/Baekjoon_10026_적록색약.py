# https://www.acmicpc.net/problem/10026

# DFS 구현
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 런타임 에러 (RecursionError)

if __name__ == '__main__':
    N = int(input().rstrip())
    grid = []
    for _ in range(N):
        grid.append(list(map(str, input().rstrip())))
    grid2 = copy.deepcopy(grid)

    def dfs(x, y, now, cw):
        if x <= -1 or x >= N or y <= -1 or y >= N:
            return False

        if cw == True :
            if grid2[x][y] == 'G':
                grid2[x][y] = 'R'
            if grid2[x][y] == now:
                grid2[x][y] = 'v'
                dfs(x - 1, y, now, cw)
                dfs(x + 1, y, now, cw)
                dfs(x, y - 1, now, cw)
                dfs(x, y + 1, now, cw)
                return True
        elif cw == False:
            if grid[x][y] == now:
                grid[x][y] = 'v'
                dfs(x - 1, y, now, cw)
                dfs(x + 1, y, now, cw)
                dfs(x, y - 1, now, cw)
                dfs(x, y + 1, now, cw)
                return True
        return False
    
    result1 = 0
    result2 = 0
    for i in range(N):
        if 'R' not in grid[i] and 'G' not in grid[i] and 'B' not in grid[i]:
            continue
        for j in range(N):
            if grid[i][j] != 'v':
                if dfs(i, j, grid[i][j], cw=False) == True:
                    result1 += 1
            if grid2[i][j] != 'v':
                if dfs(i, j, grid2[i][j], cw=True) == True:
                    result2 += 1

    print(result1, result2)
