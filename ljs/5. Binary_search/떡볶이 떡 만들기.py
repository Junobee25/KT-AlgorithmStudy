# 떡볶이 떡 만들기
# n, m = map(int,input().split())
# arr = list(map(int, input().split()))
# count = 0
# max_arr = max(arr)

# for i in range(max_arr):
#     arr = sorted(arr, reverse = True)
#     if arr[0] >= arr[1]:
#         value = arr[0] - 1
#         del arr[0]
#         arr.insert(0, value)
#         count += 1
#         if count == m:
#             print(arr[0])
#             break

# 떡볶이 떡 만들기 
n, m = map(int,input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)