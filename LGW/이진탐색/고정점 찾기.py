def b_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return b_search(arr, start, mid - 1)
    
    else :
        return b_search(arr, mid + 1, end)
n = int(input())
arr = list(map(int, input().split()))

idx = b_search(arr,0,n-1)

if idx == None:
    print(-1)
else :
    print(idx)