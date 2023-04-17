# 파라메트릭 서치(결정문제)
# 절단기 높이를 이분탐색으로 찾는다
# 잘라낸 떡의 길이의 합이 m이 될때 return을 하고 높이를 반환

n,m = map(int,input().split())
food = list(map(int,input().split()))

l = 0
r = max(food)

while l<=r:
    mid = (l+r)//2
    f_len = 0 # 잘라내고 남은 떡의 길이
    for i in food:
        if i >= mid:
            f_len += i-mid
    # 최소 m만큼에 떡을 얻기 위해서 절단기의 최댓값은 f_len == m을 만족해야함
    if f_len == m:
        print(mid)
        break
    # 이분탐색 로직
    if f_len > m:
        l = mid + 1
    else:
        r = mid -1
