# n개의 원소가 있는 오름차순 수열에서 고정점 찾기
# 고정점 : 그 값이 인덱스와 동일한 원소

n = int(input())
num = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)//2
    target = array[mid] # 인덱스 번호와 동일한 그 인덱스에 해당하는 값이 target
    
    if mid == target:
        return mid
    elif mid > target: # 인덱스번호가 더 클 경우, 큰 쪽(오른쪽)을 봐야함.
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
    
result = binary_search(num, num[0], 0, n-1)

if result == None:
    print(-1)
else:
    print(result)
    

