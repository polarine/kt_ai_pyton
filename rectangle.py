area = int(input('직사각형의 넓이를 입력하시오. : '))

for i in range(1, area+1) :
    if area%i == 0:
        print (f'{i} x {area//i}')

