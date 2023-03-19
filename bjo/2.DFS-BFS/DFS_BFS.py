# 인접행렬 => 모든 관계 저장
# 인접리스트 => 연결된 관계 정보만 저장 => 메모리가 훨씬 효율적
# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 할당
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
            
from collections import deque
# BFS 메서드 정의
def bfs(graph,start,visited):
    # 큐(Queue)구현을 위해 deque 라이브러리 사용
    q = deque([start])
    # 현재 노드를 방문 처리
    visited[v] = True
    # 큐가 빌때 까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력
        v = q.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
            

            

    