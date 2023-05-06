# G개의 탑승구, P개의 비행기


# g = int(input())
# p = int(input())

# graph = [0] * (g+1)
# count = 0
# for i in range(p):
#     a = int(input())
#     for j in range(a, 1, -1):
#         if graph[j] == 0:
#             graph[j] = 1
#             count += 1
#             break
#         else:
#             continue
        
# print(count)

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
        
g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(g+1):
    parent[i] = i
    
count = 0
for _ in range(p):
    x = int(input())
    # 들어오는 비행기의 탑승 루트 확인
    d = find_parent(parent, x)
    # 0이라면 이미 꽉차있으므로 종료
    if d == 0:
        break
    # 자기 자신의 바로 왼쪽 집합과 합치기
    union_parent(parent, d, d-1)
    count += 1
    
print(count)