inf = int(1e9)

n,m = map(int,input().split())


graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1 , n+1):
        if i ==j :
            graph[i][j] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
#    graph[b][a] = 1
# 비교에만 초점을 두지말고 대소비교 할 때 한방향으로만 해야 순위를 예측 가능 
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])
            
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != inf or graph[j][i] != inf:
            count +=1
            
        if count == n: # 모든 학생과 비교 가능 하다면 추가
            result +=1
print(result)
            