# N개의 여행지, 여행지 계획이 가능한지의 여부 판별
# 여행지가 같은 집합에 속하는가(부모 노드 확인)
# 서로소 집합 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 여행지의 수, 여행 계획에 속한 도시 수
n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

# 여행지가 연결되어 있는지 여부    
travel = []
for _ in range(n):
    travel.append(list(map(int, input().split())))

# 여행 계획
plan = list(map(int, input().split()))

for a in range(n):
    for b in range(n):
        if travel[a][b] == 1:
            union_parent(parent, a+1, b+1)
 
check = False           
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        check = False
        break
    else:
        check = True
        
if check:
    print("YES")
else:
    print("NO")