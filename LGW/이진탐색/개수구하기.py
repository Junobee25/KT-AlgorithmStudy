def cnt_val(arr,x):
    n = len(arr)

    a = first(arr,x,0,n-1)
    if a == None:
        return 0
    b = last(arr,x,0,n-1)
    return b-a+1


def first(arr,target,start,end):
    if start > end:
        mid = (start+end) //2
        if (mid==0 or target>arr[mid-1]) and arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            return first(arr,target,start,mid-1)
        else :
            return first(arr,target,mid+1,end)
        
def last(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end) //2
    if (mid==0 or target<arr[mid-1]) and arr[mid] == target:
            return mid
    elif arr[mid] > target:
            return last(arr,target,start,mid-1)
    else :
            return last(arr,target,mid+1,end)
    
n,x = map(int,input().split())
arr = list(map(int,input().split()))

cnt = cnt_val(arr,x)

if cnt == 0:
     print(-1)
else :
     print(cnt)