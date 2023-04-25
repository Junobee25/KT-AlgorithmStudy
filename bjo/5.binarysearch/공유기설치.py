import sys
input = sys.stdin.readline
def Count(len):  # 가장인접한길이의 최댓값이
    cnt = 1
    end = Line[0]
    for i in range(1,n):
        if Line[i] - end >= len:
            cnt +=1 # 공유기 설치
            end = Line[i]
    return cnt

n,c = map(int,input().split())
Line = []
for _ in range(n):
    location = int(input())
    Line.append(location)
Line.sort()
lt = 1 # 인접한 길이 최솟값
rt = Line[n-1] # 인접한 길이 최대 값
while lt <= rt:
    mid= (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)