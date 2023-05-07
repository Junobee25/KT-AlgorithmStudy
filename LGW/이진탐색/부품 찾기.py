def b_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            start = mid - 1
        else:
            end = mid + 1
        return None
n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x :
    result = b_search(arr, i, 0, n-1)
    if result!= None :
        print('yes',end=' ')
    else:
        print('no',end=' ')