# 정렬된 배열에서 특정 수의 개수 구하기

# 정렬된 배열에서 특정 수의 개수 구하기
# 특정한 데이터를 찾도록 요구하는 문제에서는 파이썬 라이브러리 중 bisect module을 사용가능
from bisect import bisect_left, bisect_right
import time
start_time = time.time()

n,x = map(int,input().split())
arr = list(map(int,input().split()))

left_index = bisect_left(arr,x)
right_index = bisect_right(arr,x)
result = right_index - left_index

if result == 0:
    print(-1)
else:
    print(result)

end_time = time.time()
print("time:", end_time - start_time)


# import time
# start_time = time.time()

# n,x = map(int,input().split())
# arr = list(map(int,input().split()))

# result = arr.count(x)

# if result == 0: result = -1
    
# end_time = time.time()
# print("time:", end_time - start_time) 


## 시간 초과
# import time
# start_time = time.time()

# n, x = map(int, input().split())
# arr = list(map(int, input().split())) 

# count = 0

# for i in range(n):
#     if x == arr[i]:
#         count+=1
        
# if count == 0:
#     print(-1)
# else:
#     print(count)
    
# end_time = time.time()
# print("time:", end_time - start_time)