### 탑승구
n = int(input())
p = int(input())
plane = [int(input()) for _ in range(p)]

team = [0]*(n+1)
for i in range(1,n+1): team[i]=i

def find_root(team, x):
    if team[x]!=x:
        return find_root(team,team[x])
    return team[x]

def union_parent(team, a, b):
    a = find_root(team, a)
    b = find_root(team, b)
    if a<b:
        team[b]=a
    else:
        team[a]=b


count = 0
for p in plane:
    root = find_root(team, p)
  
  # 탑승구 루트가 0이면 더 못들어가므로 break
    if root==0:
        break
    
  # 탑승구 최대 번호에 도킹하고, -1만큼 작은 탑승구를 root로
    union_parent(team, root, root-1)
    count += 1

print(count)