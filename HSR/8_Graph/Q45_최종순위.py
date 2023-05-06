# 1~n개의 팀, 올해 순위 만들기
# 정해진 우선순위에 맞게 전체 팀들의 순서를 나열 -> 위상정렬 알고리즘
# 위상 정렬 수행 과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유 순위 존재

from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for i in range(n+1)]
    
    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
            
    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
            
    # 위상정렬 시작
    result = [] # 알고리즘 수행 결과
    q = deque
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내 사이클이 존재하는지 여부
    
    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러개라는 의미
        if len(q) >= 2:
            certain = False
            break
        
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드들 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)
                    
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()