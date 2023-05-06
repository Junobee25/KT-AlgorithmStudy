import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 상 하 좌 우
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

def dijkstra(graph, start):
    n = len(graph)
    distance = [[INF] * n for _ in range(n)]
    
    x, y = start
    distance[x][y] = graph[x][y]
    
    q = []
    heapq.heappush(q, (distance[x][y], start))

    while q:
        dist, now = heapq.heappop(q)
        x, y = now

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    return distance[n-1][n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(dijkstra(graph, (0, 0)))
