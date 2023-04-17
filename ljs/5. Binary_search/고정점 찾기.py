# 고정점 찾기
import time
start_time = time.time()

n = int(input())
arr = list(map(int, input().split()))
value = 0
left = n//2 

for i in range(left):
    if i == arr[i]:
        value = i
        print(value)
        break
    if value == 0:
        for i in reversed(range(left, n)):
            if i == arr[i]:
                value = i
                print(value)
                break
if value == 0:
    print(-1)
    
    
end_time = time.time()
print("time:", end_time - start_time)
