#문자열 비교 해서 서로 같게 하는 최소의 수 구하기 --> 2차원 행렬로 만들어서 하기 --> 왼쪽(삽입) 위쪽(삭제) 왼쪽 위(교체)
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
        
    for i in range(1, n+1):
        for j in range(1,m+1):
            if str[i-1] == str[j -1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1] , dp[i-1][j], dp[i-1][j-1])
                
str1 = input()
str2 = input()

print(edit_dist(str1,str2))