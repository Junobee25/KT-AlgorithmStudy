n = int(input())
bupum = list(map(int,input().split()))
m = int(input())
request = list(map(int,input().split()))

# 이진탐색하기 위해 부품 정렬
bupum.sort()

# target이 여러개 이므로 for을 통해서 이진 탐색
for i in request:
    l = 0
    r = len(bupum)-1
    flag = False # 원하는 값이 없으면 no출력하기 위한 flag
    while l<=r:
        mid = (l+r)//2
        if bupum[mid] > i:
            r = mid - 1
        else:
            l = mid + 1
        if bupum[mid] == i: # target이 나오면
            flag = True
            print("yes", end = " ")
    if flag == False:
        print("no", end = " ")