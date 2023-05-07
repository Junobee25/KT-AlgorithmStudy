def find (parent, x):
    # 루트노드가 아니라면 루트노드를 찾을떄 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union (parent,a, b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b

n, m =map(int,input().split())
parent = [0] * (n +1)

for i in range(m):
    oper, a,b = map(int,input().split())
    if oper == 0:
        union(parent,a,b)
    elif oper == 1:
        if find(parent,a) == find(parent,b):
            print('YES')
        else: 
            print('NO')
