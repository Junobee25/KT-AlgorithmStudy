# n >= 3
# 중심에서 가장 가까운 인덱스가 정답

n = int(input())
arr = list(map(int,input().split()))

# if n == 1 or n == 2:
#     print(arr[0])
#     exit()

# # 정렬

# arr = list(set(arr))
arr.sort()


# # 중심과의 거리
# dist_from_center = []


# for i in range(arr[0],arr[-1]+1):
#     if i in arr :     
#         dist_from_center.append(abs(i-((arr[0]+arr[-1])//2)))


# dist_from_center.remove(0)
# # 중심과의 거리가 제일 작은 인덱스찾기
# target = dist_from_center.index(min(dist_from_center))

# print(arr[target])

print(arr[(n-1)//2])
