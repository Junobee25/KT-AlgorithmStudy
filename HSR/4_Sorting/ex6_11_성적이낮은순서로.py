n = int(input())
student = []
for i in range(n):
    s = input().split()
    student.append((s[0], int(s[1]))) # 점수는 숫자형으로
    
# key활용, 점수 기준으로 정렬
result = sorted(student, key = lambda student: student[1])

for i in result:
    print(i[0], end=' ')