# 문제 유형
# 도달 할 수 있는 노드 중에서 최소비용의 최댓값을 찾는 문제

# 접근
# 모든 노드에서 모든 노드까지의 고려를 했는데
# 출발노드에서 갈 수있는 노드들의 최소 비용을 구한 다음 그 중에서 최댓값을 구하면 되는 문제였음

import heapq

n,m,start = map(int,input().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

distance = [INF * (n+1)]

def dijkstar(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # q가 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkstar(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)

print(count-1,max_distance)


