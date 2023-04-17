n = input()
letters = ""
num = 0
for i in n: 
    if i.isdigit():
        num += int(i)
    else:
        letters += i

letter_sort = ''.join(sorted(letters))
result = letter_sort + str(num)
print(result)