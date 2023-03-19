# 행의 개수 n, 열의 개수 m
# n개의 줄에 걸쳐 각 카드에 적힌 숫자

# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수

n, m = map(int, input().split())
arr = []

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data) # 행당 가장 작은수 저장
    arr.append(min_value) # 배열에 작은 수 하나씩 저장
    
#  arr은 각 행에서 가장 작은 값의 배열
print(max(arr))  # 작은 수중 가장 큰수 출력