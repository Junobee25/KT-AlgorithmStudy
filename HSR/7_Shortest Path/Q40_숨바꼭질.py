# 1~n번까지의 헛간 중 하나를 정해 숨음.
# 술래는 항상 1번부터 출발, m개의 양방향 통로 존재
# 최단 거리가 가장 먼 헛간

import heapq
INF = int(1e9)

n, m = map(int, input().split())
start = 1 # 시작 노드
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # a->b 이동비용 1, 양방향
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    
distance = [INF] * (n+1) 

# 다익스트라 알고리즘 수행
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

max_node = 0
max_distance = 0
result = []

# 최단 거리 중 거리가 가장 먼 거리 구하기
for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i[0]]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))