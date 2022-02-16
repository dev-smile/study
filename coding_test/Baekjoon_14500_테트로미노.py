# https://www.acmicpc.net/problem/14500

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    papers = []
    check = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 0
    for _ in range(n):
        check.append([False]*m)
        papers.append(list(map(int, input().rstrip().split())))
            
    def dfs(x, y, sum, length):
        global result, papers, check
        # 길이가 4가 되면 종료
        if length >= 4:
            result = max(result, sum)
            # print(result, sum)
            return
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 주어진 범위를 벗어나는 경우에는 종료
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
           # print(n, ny, m, nx)
            if check[ny][nx] == True:
                continue
            
            check[ny][nx] = True
            dfs(nx, ny, sum + papers[ny][nx], length+1)
            check[ny][nx] = False

    for i in range(n):
        for j in range(m):
            check[i][j] = True     
            dfs(j, i, papers[i][j], 1)
            check[i][j] = False

            if j+2 < m: #ㅓㅏㅗㅜ 검사
                temp = papers[i][j] + papers[i][j+1] + papers[i][j+2]
                if i-1 >= 0:
                    result = max(result, temp+papers[i-1][j+1])
                if i+1 < n:
                    result = max(result, temp+papers[i+1][j+1])
            if i+2 < n:
                temp = papers[i][j] + papers[i+1][j] + papers[i+2][j]
                if j-1 >= 0:
                    result = max(result, temp+papers[i+1][j-1])
                if j+1 < m:
                    result = max(result, temp+papers[i+1][j+1])

    print(result)
