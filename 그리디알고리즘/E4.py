## 1이 될때 까지.
# 입력 조건 1. N에서 1을 뺀다.
# 입력 조건 N을 K로 나눈다.

n,k = map(int,input('n,k입력').split())
result = 0 ## 총 횟수
#case1 N-1
#case2 N/K
while n >= k :
    while n%k != 0:
        n -= 1
        result +=1
    n //=  k
    result +=1

while n>1:
    n-=1
    result += 1
print(result) ## 횟수 출력
