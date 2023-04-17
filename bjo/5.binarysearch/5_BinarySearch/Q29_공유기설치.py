# C개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대
# 집의 개수 N, 공유기 개수 C

#### 다시 풀어보기 ####

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
    
house.sort()

result = 0
start = 1
end = house[n-1] - house[0] # 최대 길이 설정

while start<=end:
    mid = (start + end)//2
    value = house[0]
    count = 1
    
    for i in range(1, n):
        if house[i] >= value + mid:
            value = house[i]
            count += 1
    
    if count >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1
        
print(result)