# n개의 부품과 정수 형태의 고유 번호
# 문의한 부품 m개 종류 확인

n = int(input())
part = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

# 부품을 번호순으로 정렬
part.sort()

# 재귀함수로 이진 탐색
def binary_search(array, target, start, end):
    mid = (start + end)//2
    
    if start > end:
        return None
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
    # while start <= end:
    #     mid = (start + end)//2
        
    #     if array[mid] == target:
    #         return mid
    #     elif array[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    # return None
    
        
for i in want:
    r = binary_search(part, i, 0, n-1)
    if r != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')