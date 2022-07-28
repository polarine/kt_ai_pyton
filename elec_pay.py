def electricPay(usage):
    if usage < 100:
        pay = 410 + (usage * 60.7)
    elif usage <= 200:
        pay = 910 + 6070 + ((usage-100)*125.9) 
    else :
        pay = 1600 + 6070 + 12590 + ((usage-200)*187.9)
    
    pay = pay + (0.1 * pay) + (0.037 * pay)
    
    return int(pay//1)

usage = int(input('전기사용량을 입력하세요. :'))
print (f'전기요금은 {electricPay(usage)}원 입니다.')
