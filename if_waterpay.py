def waterPay(a, b):
    
    if a == 'A':
        pay = 100 * b
        return pay
    elif a == 'B':
        if b < 50 :
            pay = b * 150
            return pay
        else :
            pay = (150 * 50) + (75 * (b-50))
            return pay
    elif a == 'a':
        pay = 100 * b
        return pay
    elif a == 'b':
        if b < 50 :
            pay = b * 150
            return pay
        else :
            pay = (150 * 50) + (75 * (b-50))
            return pay
        
print ('수도 요금을 계산하겠습니다.')
a = input('수도 회사를 입력해주세요. : ')
b = int(input('사용한 수도량을 입력해 주세요. : '))
print (f'내야할 수도 요금은 {waterPay(a, b)}원 입니다.')