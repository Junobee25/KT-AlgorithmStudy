n = int(input())
data = list(map(int, input().split()))

data.sort()

member = 1 # 포함된 멤버 수
count = 0 # 그룹 수

for i in range(n):
    if data[i] <= member:
        count+=1
        member = 1
    else:
        member+=1
        
print(count)