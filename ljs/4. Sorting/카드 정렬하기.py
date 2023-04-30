# 카드 정렬하기
n = int(input())
data = []
for _ in range(n): 
    data.append(int(input()))

data.sort()

len_data = len(data)
count = data[0] * (len_data-1)
for i in range(1, len_data):
    count += data[i] * (len_data-i)
    
print(count)