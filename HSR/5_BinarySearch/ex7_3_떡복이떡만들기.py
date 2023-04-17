# 손님이 요청한 총 길이가 M일 때, 절단기에 설정할 수 있는 높이의 최댓값 구하기

n, m = map(int, input().split())
r = list(map(int, input().split())) # 떡의 길이

r.sort()

start = 0
end = r[n-1] # 끝 값을 제일 긴 떡의 길이로

# 절단기 이진 탐색
while start <= end:
    mid = (start + end)//2
    result = 0
    
    # 모든 떡을 절단기로 절단 후, 남은 떡 값 더하기
    for i in range(n):
        a = r[i] - mid
        # 떡이 남았을 경우만 더하기
        if a > 0:
            result += a
            
    if result == m:
        break
    # 남은 떡의 길이가 더 크므로 절단기 값 늘리기
    elif result > m:
        start = mid + 1
    # 남은 떡의 길이가 더 작으므로 절단기 값 줄이기
    else:
        end = mid - 1
        
print(mid)