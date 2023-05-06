# n개의 도시, x->y로 보내려면 둘다 통로가 존재해야 함.
# c도시에서 보낸 메시지를 받게 되는 도시수와 걸리는 시간

import heapq
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 특정 도시 x에서 다른 특정도시 y로 이동하는 시간 z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush((cost, i[0]))
                
dijkstra(c)

#######################################
count = 0 # 도달 할 수 있는 곳의 개수
max_distance = 0 # 최단 거리 중 가장 먼 곳
for d in distance:
    if d!=INF:
        count += 1
        max_distance = max(d, max_distance)
        
print(count-1, max_distance)