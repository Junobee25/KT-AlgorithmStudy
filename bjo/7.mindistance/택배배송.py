import heapq

# 노드와 간선 입력받기
n,m = map(int,input().split())

INF = int(1e9)
# 그래프 틀 만들기 => 해당 노드와 연결되어 있는 리스트 정보에 대한 그래프
graph = [[] for _ in range(n+1)]


# 각 노드와 연결 되어있는 노드, 그리고 여물의 양 정보 담기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


# 여물의 양 무한대로 초기화
stover = [INF for _ in range(n+1)]


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    stover[start] = 0
    while q:
        # 큐에서 가장 여물의 양이 작은 노드에 대한 정보 꺼내기
        sto,now = heapq.heappop(q)
        if stover[now] < sto:
            continue
        # 현재 노드와 연결된 다른 인접한 노드를 확인
        for i in graph[now]:
            cost = sto + i[1]
            if cost < stover[i[0]]:
                stover[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익 실행
dijkstra(1)

print(stover[-1])


    


