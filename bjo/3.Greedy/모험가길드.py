# 문제 이해
# 공포도가 x => 반드시 그룹 수 x명 이상
# 그룹 수의 최댓 값

# 접근
# 공포도가 작은 인원부터 그룹핑을 해보기
# 공포도만큼 그룹핑을 하는게 최적의 해이다.
n = int(input())
fear = list(map(int,input().split()))

# 1 2 3 일 때 생각 (1) // (1,2) // (1,2,3) => 1
fear.sort()
print(fear)
# 공포도만큼 그룹핑을 하는게 최적의 해이다.
group = 0 # 그룹 수를 카운트 해줄 전역 변수 선연
for i in range(len(fear)):
    cnt = 0 # 그룹의 최소인원 카운트 변수
    for j in range(i,fear[i]+1): # 공포도 만큼 for문 돌리기
        if fear[j] == fear[i]:
            cnt += 1
            if cnt == fear[i]: # 최소인원 다 채워지면 그룹핑
                group += 1
        else:
            break
print(group)



