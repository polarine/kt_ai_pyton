n = int(input('숫자를 입력하세요.: '))
root=1
flag = 0

while root < n+1:
    for pwr in range(2, 6):
        if (root**pwr) == n:
            print(f'{root}**{pwr} = {n}입니다.')
            flag = 1
    
    root += 1

if flag == 0:
    print('해당하는 수가 없습니다.')