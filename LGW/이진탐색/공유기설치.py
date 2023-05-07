n,c = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(int,input().split())
arr.sort()

start = arr[1] - arr[0]
end = arr[-1] - arr[0]
result =0

while(start <= end):
    mid = (start + end)//2
    val = arr[0]
    cnt =1

    for i in range(1,n):
        if arr[i] >= val+mid:
            val = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else :
        end = mid - 1
print(result)
