# 문제유형
# 아래 오른쪽 대각선 이동하면서 선택된 수의 합이 최대가 되는 경로를 구하는 문제

# 접근
# 부분문제 정의하기


n=int(input())
d=[]
for i in range(n):
  d.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(d[i])):
    # 
    if j==0:
      # 아래와 같은 점화식을 도출하기 위해선 첫번째 요소는 이전 행에서 와야함
      d[i][j]=d[i][j]+d[i-1][j]
    elif j==len(d[i])-1: 
      # 아래와 같은 점화식을 도출하기 위해 마지막 요소는 대각선에서 와야함
      d[i][j]=d[i][j]+d[i-1][j-1]
    else:
      # 점화식 세우기
      d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]
print(max(d[n-1]))