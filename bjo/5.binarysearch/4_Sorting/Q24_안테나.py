# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치
# 중간위치에 설치

n = int(input())
house = list(map(int, input().split()))

house.sort()
print(house[(n-1)//2])