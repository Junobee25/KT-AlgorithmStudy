n = list(input())
x = len(n) // 2
num1 = 0
num2 = 0
for i in range(x):
    num1 += int(n[i])

for i in range(x,len(n)):
    num2 += int(n[i])

if num1 == num2:
    print("LUCKY")
else:
    print("READY")
