print('네개의 정수중에 최댓값을 구합니다')
a = int(input('정수 a의 값을 입력하세요. : '))
b = int(input('정수 b의 값을 입력하세요. : '))
c = int(input('정수 c의 값을 입력하세요. : '))
d = int(input('정수 d의 값을 입력하세요. : '))

maximum = a
if maximum < b :
    maximum = b
if maximum < c :
    maximum = c
if maximum < d :
    maximum = d

print(f'최댓값인 정수는 {maximum}입니다.')