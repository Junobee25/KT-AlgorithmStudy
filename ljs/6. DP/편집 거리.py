# 편집 거리
str1=list(map(str,input()))
str2=list(map(str,input()))
  
n, m =len(str1),len(str2)

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0]=i
for j in range(1,m+1):
    dp[0][j]=j
    
for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i-1]==str2[j-1]:
      #첫번째 문자열의 i번째 문자와 두번째 문자열에 j번째 문자가 동일하다면 
          dp[i][j]=dp[i-1][j-1]#빨간색 원
      #이번 번째까지 변화시키는데 들었던 비용을 그대로 가져온다.
        else:
      #첫번째 문자열의 i번째 문자와 두번째 문자열에 j번째 문자가 다르다면
          dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
      #이전 번째까지 변화시켰던 최소의 비용에 지금 문자 변형시키는 비용 1을 추가.

print(dp[n][m])
