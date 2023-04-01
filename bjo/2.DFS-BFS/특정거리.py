# 문제 이해
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
# X로부터 출발하여 도달 할 수 있는 도시 중 최단 거리가 K인 모든 도시 번호
# 없으면 -1

# bfs탐색 중 queue에 원소가 들어갈 때마다 cnt += 1 result 리스트에도 원소 담기
# 만약에 k == cnt break걸고 result리스트에 있는 원소 오름차순으로 출력
from collections import deque
n, m, k, x = map(int,input().split())

matrix = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

# 노드까지의 거리를 저장해둘 리스트
dist = [0 for _ in range(n+1)]

# 단방향
for i in range(m):
    a, b = map(int,input().split())
    matrix[a].append(b)

def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    while q:
        node = q.popleft()
        visited[node] = True        
        for i in matrix[node]:
            if visited[i] == False:
                visited[i] = True
                dist[i] += dist[node] + 1 # 처음 방문한 노드는 이전 노드의 거리에서 + 1 
                q.append(i)

    if k in dist: # dist 리스트에 k만큼 떨어진 노드가 있다면
        for i in range(len(dist)): # dist의 인덱스 출력 == 노드
            if dist[i] == k:
                print(i)
    else: # k만큼 떨어진 거리가 없다면 -1 출력
        print(-1)

bfs(x)

# while문이 돌때마다 cnt +1을 해줬더니
# 노드를 탐색할 때마다 길이가 계속 증가해서
# 실제 길이가 2인데도 길이가 2 초과로 설정되어 버려서
# result에 append가 안되는 현상 발생.
# ex 1 -> 2 -> 4, 1 -> 3 -> 5       =====   5는 실제 거리가 2인데 5는 반복문이 돌면서 cnt 가 더 증가해버림

# 해결
# 해당 노드까지의 거리가 얼마인지 결과를 저장해두면서 탐색


