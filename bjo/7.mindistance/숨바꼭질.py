import heapq
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(1)
for i in range(len(distance)):
    distance[i] = (distance[i],i)
idx = 0
max_val = -1
cnt = 0
distance.sort()
print(distance)
for i in range(len(distance)):
    if distance[i][0] >= INF:
        continue
    if distance[i][0] > max_val:
        max_val = distance[i][0]
        idx = distance[i][1]

for i in range(len(distance)):
    if distance[i][0] >= INF:
        continue
    if distance[i][0] == max_val:
        cnt += 1
print(idx,max_val,cnt)

