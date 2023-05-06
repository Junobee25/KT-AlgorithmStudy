# n명의 성적 분실
# 성적 비교, 성적 순위를 정확히 알 수 있는 학생 출력
# A->B : A보다 B가 성적이 더 낮음을 의미
# 서로 향하는 경로가 없을 경우, 순위를 알 수 없음을 의미

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
            
for _ in range(1, n+1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
# 플루이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
result = 0

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    # 한 사람의 순위를 정확하게 안 것
    if count == n:
        result += 1

print(result)