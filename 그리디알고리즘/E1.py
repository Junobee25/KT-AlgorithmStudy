##거스름돈

n  = int(input('금액 입력:'))  # 거스름돈 입력
coin_list = [500,100,50,10]  # 동전의 종류 리스트
cnt = 0  # 개수 세기

for coin in coin_list:
    cnt += n // coin
    n %= coin
    
print(cnt)




