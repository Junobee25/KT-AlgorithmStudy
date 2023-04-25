# 정수 삼각형
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
            if j>0:
                left = arr[i-1][j-1]
            else:
                left = 0
                
            if j<len(arr[i])-1 :
                right = arr[i-1][j] 
            else:
                right = 0
                
            arr[i][j] += max(left, right)

res = 0
for i in arr[n-1]:
    res = max(res, i)

print(res)
