n = int(input())
count = 0

while n != 0:
    if n>=500:
        count += n//500
        n = n%500
    elif n>=100:
        count += n//100
        n = n%100
    elif n>=50:
        count += n//50
        n = n%50
    elif n>=10:
        count += n//10
        n = n%10
        
print(count)