# 성적이 낮은 순서로 학생 출력하기
n = int(input())
arr = []
for i in range(n):
    name_score = list(map(str,input().split()))
    arr.append(name_score)
    
def student(data):
    return data[1]

result = sorted(arr, key=student)

for i in result:
    print(i[0], end=' ')