n = int(input())
m = int(input())

INF = int(1e9)

# 무한 그래프
graph = [[INF]*(n) for _ in range(n)]

# 간선정보 인접행렬
for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] >= c:
        graph[a-1][b-1] = c

# 자기자신 0
for i in range(n):
    for j in range(n):
        if i == j :
            graph[i][j] = 0


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end = " ")
    print()
