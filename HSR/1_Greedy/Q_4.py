n = int(input())
money = list(map(int, input().split()))

money.sort()

result = 1
for i in money:
    if result < i:
        break
    else:
        result += i
        
print(result)