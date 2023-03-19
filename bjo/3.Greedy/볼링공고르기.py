# 문제 이해
# 무게가 다른 모든 볼링공의 조합 개수 구하기
# 순서만 바뀐것은 카운트 x

# 접근
# flag를 잡고 이중포문을 돌면서 같으면 추가하지 않기

n, m = map(int,input().split())
boling = list(map(int,input().split()))

cnt = 0

for i in range(len(boling)):
    for j in range(i+1,len(boling)):
        if boling[i] != boling[j]:
            cnt +=1
print(cnt)            

