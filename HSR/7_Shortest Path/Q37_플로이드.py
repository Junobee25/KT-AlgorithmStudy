# n개의 도시, m개의 버스
# 모든 도시의 쌍(A, B)에 대해 필요한 비용의 최솟값

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())
    # 간선 정보가 여러개 입력되므로 가장 짧은 간선만 저장.(주의)
    if c < graph[a][b]:
        graph[a][b] = c
    
# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()