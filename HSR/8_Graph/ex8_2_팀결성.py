# 0 : 팁 합치기 연산(union)과 1 : 같은 팀 여부 확인(find) 연산
# 같은 팀 여부 확인 연산에 대하여 YES/NO 출력
# 서로소 알고리즘

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

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i
    
for i in range(m):
    o, a, b = map(int, input().split())
    
    if o == 0: # union
        union_parent(parent, a, b)
    elif o == 1: # find
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")