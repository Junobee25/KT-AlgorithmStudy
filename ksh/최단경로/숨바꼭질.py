inf = int(1e9)

n = int(input())
m = int(input())

graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1 , n+1):
        if i ==j :
            graph[i][j] = 0
    
for _ in range(m):
    a,b,c = map(int,input().split())
    if c < graph[a][b]: # 동일한 경로 존재 가능하기에 더 작은 값을 넣어준다
        graph[a][b] = c
    
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])
            

for i in range(1, n+1):
    for j in range(1 , n+1):
        if graph[i][j] == inf:
            print(0 , end = ' ')
        else:
            print(graph[i][j], end= ' ')
    print()            