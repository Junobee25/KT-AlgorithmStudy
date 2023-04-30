# 위에서 아래로
n = int(input())
arr = []

for i in range(n):
    num = input()
    arr.append(num)
    
result = ' '.join(sorted(arr, reverse=True))
print(result)