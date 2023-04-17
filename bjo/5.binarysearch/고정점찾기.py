# Amazon 인터뷰
# arr[mid] == mid 

n = int(input())
arr = list(map(int,input().split()))

l = 0
r = len(arr) - 1

while l <= r:
    mid = (l+r)//2
    # 고정점 찾으면 출력 후 exit()
    if arr[mid] == mid:
        print(mid)
        exit()
    
    if arr[mid] > mid:
        r = mid - 1

    else:
        l = mid + 1

# 고정점 없으면 -1 출력
print(-1)