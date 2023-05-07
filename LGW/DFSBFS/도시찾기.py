from collections import deque ## deque는  앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

n,m,k,x = map(int, input('입력').split()) #도시 개수 도로개수 거리 정보 도시번호
graph = [[]for _  in range(n+1)] #인접리스트로 그래프만 표현..
# 도로 정보 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
#현재도시에 이동할수 있는 도시확인
    for next_node in graph[now]:
    #최단거리 갱신
        if distance[next_node] == -1:
            distance[next_node] = distance[now] +1
            q.append(next_node)
    # 최단거리가 K인 도시의 번호 출력
check = False
for i in range(1,n+1):
    if distance[i] ==k:
        print(i)
        check =  True
if check == False:
    print(-1)