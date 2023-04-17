# O(logN)으로 해결해야 되는 문제
from bisect import bisect_left,bisect_right
n,m = map(int,input().split())
arr = list(map(int,input().split()))
result = bisect_right(arr,m) - bisect_left(arr,m)
if result != 0 :
    print(result)
else:
    print(-1)