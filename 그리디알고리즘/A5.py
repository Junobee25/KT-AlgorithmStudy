n,m = map(int,input('입력:').split())
data = list(map(int, input('입력:').split()))

array = [0]*11 # 리스트 11개 생성
for i in data:
    array[i] += 1 # 볼링공 카운트 증가
result = 0
for j in range(1, m+1) : #1부터 m까지의 개수에 대해서
    n -= array[i]
    result += array[i] * n

print(result)

