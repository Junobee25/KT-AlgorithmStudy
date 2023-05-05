n , m = map(int,input().split())
array = list(map(int,input().split()))


dp = []

index = 0

for i in range(n):
    dp.append(array[index:index + m]) # 처음에는 새로운 리스트에 계속 추가 해서 그 후 dp에 넣으려고 했지만 인덱싱을 하니 매우 편했음
    index+=m
    
    
for j in range(1,m):
    for i in range(n):
        if i ==0: # 제일 위
            l_u = 0
        else:
            l_u = dp[i - 1][j - 1]
        
        if i == n-1: # 맨 밑칸
            l_d = 0
        else:
            l_d = dp[i+1][j-1]
            
        l = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(l_u,l_d,l)
        
result = 0
for i in range(n):
    result = max(result , dp[i][m-1])
    
    
print(result)