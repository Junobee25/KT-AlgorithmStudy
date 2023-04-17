# n개의 원소를 포함한 수열에서 x가 등장하는 횟수

# 1. 원하는 것 찾고 -> 제거하기 -> 시간복잡도
# 2. 원하는 것 첫 시작점, 끝 시작점 찾기
 
n, x = map(int, input().split())
num = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)//2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    

result = 0

while True:
    # x가 들어있는 인덱스 반환
    r = binary_search(num, x, 0, n-1)
    
    if r == None:
        break
    else:
        result+=1
        del num[r] # x가 들어있는 인덱스 리스트에서 삭제
        n -= 1 # 삭제했으므로 리스트 길이도 줄어듦
        
if result == 0:
    print(-1)
else:
    print(result)
    
# 시간복잡도 O(logN) 초과할 듯 -> 첫 번째 위치 찾기, 마지막 위치 찾기

# from bisect import bisect_left, bisect_right

# def count_by_range(array, left_value, right_value):
#     right_index = bisect_right(array, right_value)
#     left_index = bisect_left(array, left_value)
#     return right_index - left_index

# count = count_by_range(array, x, x)