# 못생긴수 = 2,3,5를 소인수로 가지는 수
# 즉, 2, 3, 5를 약수로 가지는 합성수
# n번째 못생긴 수 찾기

n = int(input())

# 못생긴 수에 2, 3, 5의 배수 구하기

ugly = [0]*n
ugly[0] = 1 # 첫 번째 못생긴 수

i2=i3=i5 = 0 # 인덱스
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2]*2
    if ugly[l] == next3:
        i3 += 1
        next2 = ugly[i3]*3
    if ugly[l] == next5:
        i5 += 1
        next2 = ugly[i5]*2
        
print(ugly[n-1])