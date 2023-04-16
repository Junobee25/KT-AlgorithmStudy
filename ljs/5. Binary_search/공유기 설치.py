# 공유기 설치

N,C = list(map(int, input().split()))
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

result = -1 
start = 1
end = array[-1] - array[0]

while start <= end:
    mid = (start+end)//2

    base = array[0]
    modems = 1
    for target in array[1:]:
        if base + mid <= target:
            modems +=1
            base = target
    
    if C <= modems : 
        start = mid +1
        result = mid
    else : 
        end = mid -1

print(result)


### 답지 방법
# n, c = list(map(int, input().split()))

# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# arr.sort()

# start = arr[1]-arr[0]
# end = arr[1]-arr[0]
# result = 0

# while(start<=end):
#     mid = (start+end)//2
#     value = arr[0]
#     count = 1
    
#     for i in range(1, n):
#         if arr[i] >= value+mid:
#             value = arr[i]
#             count += 1
#     if count >= C:
#         start = mid+1
#         result = mid
#     else:
#         end = mid-1