print('세 정수의 최댓값을 구합니다')
a= int(input('정수a의 값을 입력하세요.:'))
b= int(input('정수b의 값을 입력하세요.:'))
c= int(input('정수c의 값을 입력하세요.:'))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
    
print(f'최댓값은 {maximum}입니다.')

def max3(a, b, c): #함수화
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum #최댓값 반환

print(f'최댓값은 {max(a, b, c)}입니다.')