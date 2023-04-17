N, M = map(int, input().split())

num = []
for i in range(N):
    num.append(list(map(int, input().split())))
  
# 각 행에서 가장 작은 것들을 저장할 리스트  
count = [0 for _ in range(M)]

for i in range(N):
     count[i] = min(num[i])
     
print(max(count))

### for문 하나로 처리하기
# result = 0
# for i in range(N):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
    
# print(result)