import heapq
# import sys
# input = sys.stdin.readline
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
# 최소힙으로 만들기
heapq.heapify(arr)
result = 0

if len(arr) == 1:
    print(result)
# k = 10 + 자식의 최소
# k가 힙에 들어옴 이진트리를 만들고 더하기
 
else:
    for _ in range(n-1): # 2개씩 꺼내는게 왜 n-1 인가?
        pre = heapq.heappop(arr)
        cur = heapq.heappop(arr)
        
        result += pre + cur
        heapq.heappush(arr,pre+cur)
    print(result)

    

    
    