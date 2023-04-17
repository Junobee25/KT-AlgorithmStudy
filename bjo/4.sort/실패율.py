N = 4
stages = [1,2,3,2,1]
answer = []
for i in range(1,N+1):
    but_not_clear = 0 # 스테이지에 도달했으나 아직 클리어하지 못한 P
    stage_in = 0 # 스테이지에 도달한 P
    for j in stages:
        if j == i:
            but_not_clear += 1
        if j >= i:
            stage_in += 1
    if stage_in == 0:
        answer.append((0.0,i))
        continue
    answer.append((but_not_clear/stage_in,i))

answer.sort(key= lambda x : (-x[0],x[1]))
    
result = []
for i in range(len(answer)):
    result.append(answer[i][1])
print(answer) 
