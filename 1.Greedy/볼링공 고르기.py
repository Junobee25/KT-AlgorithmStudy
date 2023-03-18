# A와 B는 서로 다른 볼링공 고르기
# 볼링공은 n개, 각 볼링공마다 무게 적혀있고 공의 번호는 1번부터 순서대로
# 같은 무게의 공이 여러개 있을수도 있지만 서로 다른 공으로 간주
# 볼링공의 무게는 1부터 m까지

# 내 풀이
n, m = map(int,input().split()) # n = 볼링공 수, m = 공의 최대무게
k =  list(input().split())      # 각 볼링공의 무게
count = 0

for i in range(n):
    for j in range(i, n):
        if k[i] != k[j]: # 서로 다른 무게의 볼링공을 고르기 위해 다르면
            count += 1   # count +1
       
print(count)