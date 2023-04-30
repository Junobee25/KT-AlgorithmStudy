# 1번부터 N번까지의 회사
# 도로로 연결된 회사는 1만큼의 시간으로 이동
# K번 회사에 먼저 방문 후 X번 회사 방문

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향이므로
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())
    
# 모든 노드 방문, 2차원 => 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 1번 -> k번 -> x번
result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)