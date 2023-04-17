# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 이름이 사전순으로 증가

n = int(input())
student = []
for _ in range(n):
    s = list(input().split())
    student.append((s[0], int(s[1]), int(s[2]), int(s[3])))
    
name = sorted(student, key = lambda student: student[0])
math = sorted(name, reverse=True, key = lambda name: name[3])
english = sorted(math, key = lambda math: math[2])
korean = sorted(english, reverse=True, key = lambda english: english[1])

# student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in korean:
    print(i[0])